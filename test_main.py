import sanity   #basic tests
import main     #student solution to the hw
import TA_main  #ta's solution to the hw
#import hw_logger  --> logger to score and generate internal and external reports 
# as temporary logging, enjoy the i_log and x_log objects
import pprint

EXPECTED_FUNCTIONS = ['count']
EXPECTED_SQUAREINT_METHODS = ['square']
EXPECTED_COUNT_METHODS = ['infiniteCount']

EXPECTED_DICT = {'count':1}

i_log = {}
x_log = {}

#sanity testing
funcs = sanity.listFunctionNames(main)
classes = sanity.listClassNames(main)
all_methods = sanity.listAllMethodNames(main)
f_dict = sanity.functionDict(main)

results, commonfunctions = sanity.checkForFunctions(main, EXPECTED_FUNCTIONS)

if 'SquareInt' in classes:
  results, commonmethods = sanity.checkForMethods(main.SquareInt, EXPECTED_SQUAREINT_METHODS)
  i_log["squareInt_MC"] = results
else:
  i_log["squareInt_MC"] = "FAILED, SquareInt did not exist"


if 'Count' in classes:
  results, commonmethods = sanity.checkForMethods(main.SquareInt, EXPECTED_COUNT_METHODS)
  i_log["count_MC"] = results
else:
  i_log["count_MC"] = "FAILED, Count class did not exist"

intersection_dict = sanity.checkFunctionDict(main, EXPECTED_DICT)
i_log["intersection_dict"] = intersection_dict

#testing against the TA_main.py file
test_count = main.count(5)
TA_COUNT = TA_main.count(5)
if test_count == TA_COUNT:
  i_log["test_count"] = "PASSED"


#log generation (feel free to ignore, it's just to some output form sanity's results & testing)
i_log["function_args_dict"] = f_dict
i_log["functions"] = funcs
i_log["classes"] = classes
i_log["all_methods"] = all_methods


print("\n_________________________\n")
print("function dictionary:")
pprint.pprint(f_dict)
print("\n_________________________\n")
print("internal log:")
pprint.pprint(i_log)
print("\n_________________________\n")
print("end test_main.py")

