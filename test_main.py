import main     #student solution to the hw
import TA_main  #ta's solution to the hw
from session import Session  #import the session object

sess = Session(TA_main, main)
basic_compare = sess.compare()

if basic_compare:
  sess.score_key('basic_compare', 20)
  test_count = main.count(5)
  TA_COUNT = TA_main.count(5)
  if test_count == TA_COUNT:
    sess.i_log('test_count(5)', "PASSED")
    sess.i_log('test_count(5)', "booyah")
    sess.score_key('testcount5', 5)

else:
  sess.x_log("WHOOPS", "ERROR: your function/class names did not match up with those provided in the solution key. please look over your work and resubmit")
final = sess.finalize()

