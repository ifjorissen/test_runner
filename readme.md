####Test runner:

sanity.py: tiny utilitity lib
main.py: student submitted code
ta_main.py: TA solution to the hw problem in main.py
test_main.py: testing script for the hw that imports session, main, and ta_main. 

(this *should/could* eventually all get broken into one fileset per problem, not problem set)

try it out:
  * clone the repo
  * in the repo directory run `python3 test_main.py`

what you'll see:
```
________________________
{
    "sanity_compare": {
        "top_lvl_funcs": [
            "PASSED@get5: 0 args defined in ta-TA_main.get5. 0 args in submitted-main.get5",
            "PASSED@count: 1 args defined in ta-TA_main.count. 1 args in submitted-main.count",
            "PASSED@test: 0 args defined in ta-TA_main.test. 0 args in submitted-main.test"
        ],
        "Count_funcs": [
            "PASSED@__init__: 2 args defined in ta-Count.__init__. 2 args in submitted-Count.__init__",
            "PASSED@addX: 2 args defined in ta-Count.addX. 2 args in submitted-Count.addX",
            "PASSED@addOne: 1 args defined in ta-Count.addOne. 1 args in submitted-Count.addOne"
        ],
        "SquareInt_funcs": [
            "PASSED@__init__: 2 args defined in ta-SquareInt.__init__. 2 args in submitted-SquareInt.__init__",
            "PASSED@square: 1 args defined in ta-SquareInt.square. 1 args in submitted-SquareInt.square",
            "PASSED@sqsq: 1 args defined in ta-SquareInt.sqsq. 1 args in submitted-SquareInt.sqsq"
        ],
        "classes": "PASSED: all the classes in ta-TA_main exist in main"
    },
    "info": {
        "timedelta": 0,
        "start_time": "Tuesday, 07. July 2015 12:23:36PM",
        "attempts": 3,
        "end_time": "Tuesday, 07. July 2015 12:23:36PM"
    },
    "internal_log": {
        "test_count(5)": [
            "PASSED",
            "booyah"
        ]
    },
    "score_sum": 25,
    "score_key": {
        "testcount5": 5,
        "basic_compare": 20
    },
    "external_log": {}
}


_________________________

end test_main.py
```

####How to use it
 * import Session from session.py
 * create a new session based on the solution and the submission
 * run a basic compare with Session.compare()
 * send messages to the student with Sessions.x_log(key, message), the external log
 * log internal messages with Session.i_log(key, message)
 * add to the score with Session.scorekey(key, <score int>)
 * output the report as a json object with Session.finalize()

 (For the logging, an appropriate key might be the name of the test that yielded the error, message, or score)