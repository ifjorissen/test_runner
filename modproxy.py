import json
import sys
import subprocess
import re

class ModuleProxy():
  """
  This class provides a simple sandbox that allows code from arbitrary Python
  modules to be evaluated in a subprocess. Said code cannot access the state
  of the calling process, though it has the same user privileges as the caller.
  """
  def __init__(self, module_name):
    self.module_name = module_name

  def __getattr__(self, symbol_name):
    return ObjectProxy(self, symbol_name)

  def _get(self, symbol_name, call=False, *args):
    if call:
      script_tmpl = "import {}; print(repr({}.{}(*{})))"
      script = script_tmpl.format(
        self.module_name,
        self.module_name,
        symbol_name,
        repr(args)
      )
    else:
      script_tmpl = "import {}; print(repr({}.{}))"
      script = script_tmpl.format(self.module_name, self.module_name, symbol_name)

    raw_output = subprocess.check_output([sys.executable, '-c', script])
    # the Python JSON module won't parse string literals enclosed by single-quote
    # characters, so...
    output = re.sub(r"'", '"', raw_output.decode("utf-8").rstrip())
    # allows for simple scalar types and lists to be returned by evaluated code
    # without breaking sandbox
    return json.loads(output)

class ObjectProxy():
  def __init__(self, mod_proxy, symbol_name):
    self.mod_proxy = mod_proxy
    self.symbol_name = symbol_name

  def __call__(self, *args):
    return self.mod_proxy._get(self.symbol_name, True, *args)

  def __repr__(self):
    return repr(self.value())

  def value(self):
    return self.mod_proxy._get(self.symbol_name)

if __name__ == "__main__":
  # simple tests of this module
  fake_sys = ModuleProxy('sys')
  assert isinstance(fake_sys.executable.value(), str)
  fake_math = ModuleProxy('math')
  assert fake_math.floor(3.5) is 3
  print("tests ok")

