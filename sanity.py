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
def functionDict(obj):
  f_dict = {}
  names = listFunctionNames(obj)
  for func in names:
    arg_count = getFunctionArgCount(obj, func)
    f_dict[func] = arg_count
  return f_dict

'''
listClassnNames takes a module and returns an array of the class names (strings)
''' 
def listClassNames(module):
  all_classes = inspect.getmembers(module, inspect.isclass)
  names = [x[0] for x in all_classes]
  return names

'''
getClasses takes a modules and returns an array of the classes
''' 
def getClasses(module):
  all_classes = inspect.getmembers(module, inspect.isclass)
  classes = [x[1] for x in all_classes]
  return classes

'''
listAllMethodNames takes a module and returns a dictionary (<className>, [class functions])
the method names (strings) that will be present on an instance of each described class in the module
''' 
def listAllMethodNames(module):
  cls_methods = {}
  for cls in getClasses(module):
    all_methods = inspect.getmembers(cls, inspect.isfunction)
    cls_name = cls.__name__
    cls_methods[cls_name] = [x[0] for x in all_methods]
  return cls_methods

'''
checkForFunctions: takes a module and a dictionary (<function name>:<function arg count>), 
and checks to see if the functions exist & take the right number of arguments
returns the intersection of the two dicts
''' 
def checkFunctionDict(module, expected_dict):
  intersection_dict = {}
  hw_dict = functionDict(module)
  for func_name, arg_count in expected_dict.items():
    if (func_name in hw_dict) and (arg_count == hw_dict[func_name]):
      intersection_dict[func_name] = arg_count
  return intersection_dict



'''
checkForFunctions: takes a module and an array of function names (strings), and checks 
to see if each one exists
''' 
def checkForFunctions(module, expected):
  results = ''
  common_functions = []
  func_names = listFunctionNames(module)
  results += "Functions Found: {!s}\n".format(func_names)
  for function in expected:
    if function in func_names:
      results += "PASS: {!s} is defined as a function in {!s}\n".format(function, module.__name__)
      common_functions.append(function)
    else:
      results += "FAIL: {!s} was not defined as a function in {!s}\n".format(function, module.__name__)
  summary = "{!r}/{!r} PASSED\n".format(len(common_functions), len(expected))
  results += summary
  return results, common_functions

'''
checkForMethods: given a class and an array of expected methods, returns a string of which methods
were found in the class and the list of expected methods (this is not working yet, need to cooperate with classes)
'''
def checkForMethods(cls, expected):
  results = ''
  common_methods = []
  method_names = listFunctionNames(cls)
  results += "Methods Found: {!s}\n".format(method_names)
  for method in expected:
    if method in method_names:
      results+= "PASS: {!s} is defined as a method in {!s}\n".format(method, cls.__name__)
      common_methods.append(method)
    else:
      results+= "FAIL: {!s} was not defined as a method in {!s}\n".format(method, cls.__name__)
  summary = "{!r}/{!r} PASSED".format(len(common_methods), len(expected))
  results += summary

  return results, common_methods


