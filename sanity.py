#function finder
#function argument count
#check expected
#a timer
#class list
#methods in a class list

#6.30.15
#@ifjorissen
#sanity.py: a small utility library for user submitted python file verification

import inspect

# def genDict(module):
#   exp_func = listFunctionNames(module)
#   exp_func_arg = [getFunctionArgCount(module, func) for func in exp_func]
#   EXPECTED_FUNCTION_DICT = dict(zip(exp_func, exp_func_arg))


def listfunction_names(obj):
  '''
  listfunction_names takes an object(e.g: module, class) and returns an array of the function names (strings)
  ''' 
  all_functions = inspect.getmembers(obj, inspect.isfunction)
  names = [x[0] for x in all_functions]
  return names

def getfunction_argnames(obj, function_name):
  '''
  getfunction_argnames returns the names of the function arguments
  '''
  f = getattr(obj, function_name)
  arg_names = f.__code__.co_varnames
  return arg_names

def getfunction_argcount(obj, function_name):
  '''
  getfunction_argcount returns the number of args in a function
  '''
  f = getattr(obj, function_name)
  arg_count = f.__code__.co_argcount
  return arg_count

def getfunction(obj, function_name):
  '''
  given a function name and an object return the function itself
  '''
  f = getattr(obj, function_name)
  return f

def getfunction_argdict(obj):
  '''
  getfunction_argdict takes a module and returns dict of {(functionName:functionArgCount), (...)}
  ''' 
  f_dict = {}
  names = listFunctionNames(obj)
  for func in names:
    arg_count = getFunctionArgCount(obj, func)
    f_dict[func] = arg_count
  return f_dict

def listclass_names(module):
  '''
  listclass_names takes a module and returns an array of the class names (strings)
  ''' 
  all_classes = inspect.getmembers(module, inspect.isclass)
  names = [x[0] for x in all_classes]
  return names

def getclass_dict(module):
  '''
  getclass_dict takes a module and returns a dict of {(className:classObject), (...)}
  ''' 
  all_classes = inspect.getmembers(module, inspect.isclass)
  classes = {x[0]:x[1] for x in all_classes}
  return classes

def describe_function(obj):
  print("describe_function")
  print(obj)
  obj_dict = {}
  obj_dict["obj_name"] = obj.__name__
  obj_dict["obj_args"] = obj.__code__.co_argcount
  # obj_dict["funcs"] = getfunction_argdict(obj)
  return obj_dict

