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

'''
returns the names of the function arguments
'''
def getFunctionArgNames(obj, function_name):
  f = getattr(obj, function_name)
  arg_names = f.__code__.co_varnames
  return arg_names

'''
returns the number of args in a function
'''
def getFunctionArgCount(obj, function_name):
  f = getattr(obj, function_name)
  arg_count = f.__code__.co_argcount
  return arg_count

'''
listFunctionNames takes an object(e.g: module, class) and returns an array of the function names (strings)
''' 
def listFunctionNames(obj):
  all_functions = inspect.getmembers(obj, inspect.isfunction)
  names = [x[0] for x in all_functions]
  return names

'''
functionDict takes a module and returns an array of the function names (strings) and the number of args they take
''' 
def functionArgDict(obj):
  f_dict = {}
  names = listFunctionNames(obj)
  for func in names:
    arg_count = getFunctionArgCount(obj, func)
    f_dict[func] = arg_count
  return f_dict

'''
listClassNames takes a module and returns an array of the class names (strings)
''' 
def listClassNames(module):
  all_classes = inspect.getmembers(module, inspect.isclass)
  names = [x[0] for x in all_classes]
  return names

'''
classDict takes a module and returns a dict of {(className:classObject), (...)}
''' 
def classDict(module):
  all_classes = inspect.getmembers(module, inspect.isclass)
  classes = {x[0]:x[1] for x in all_classes}
  return classes

