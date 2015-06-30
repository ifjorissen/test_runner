####Test runner:

sanity.py hold the basic utilities
main.py would be student submitted code
ta_main.py would be the TA solution to the hw problem in main.py
test_main.py is the testing script for the hw that imports sanity, main, and ta_main. 

There's no logging set up yet, so a small dictionary is just being used for now. 

(this *should* eventually all get broken into one fileset per problem, not problem set)

try it out:
  * clone the repo
  * in the repo directory run `python3 test_main.py`

what you'll see:
```
_________________________

function dictionary:
{'count': 1, 'get5': 0, 'test': 0}

_________________________

internal log:
{'all_methods': {'Count': ['__init__', 'addOne', 'addX'],
                 'SquareInt': ['__init__', 'square']},
 'classes': ['Count', 'SquareInt'],
 'count_MC': "Methods Found: ['__init__', 'square']\n"
             'FAIL: infiniteCount was not defined as a method in SquareInt\n'
             '0/1 PASSED',
 'function_args_dict': {'count': 1, 'get5': 0, 'test': 0},
 'functions': ['count', 'get5', 'test'],
 'intersection_dict': {'count': 1},
 'squareInt_MC': "Methods Found: ['__init__', 'square']\n"
                 'PASS: square is defined as a method in SquareInt\n'
                 '1/1 PASSED',
 'test_count': 'PASSED'}

_________________________

end test_main.py
```