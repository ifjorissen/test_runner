import main     #student solution to the hw
import TA_main  #ta's solution to the hw
from session import Session  #import the session object

MAX_SCORE = 100

sess = Session(TA_main, main)
sess.set_max_score(MAX_SCORE)
basic_compare = sess.compare()

if basic_compare:
  sess.set_score(50)
  sess.test_hw_function('count', [0, -5, 10], [-1, 2, 7])
  sqInt = main.SquareInt(4)
  ta_sqInt = TA_main.SquareInt(4)
  ta_sqit = ta_sqInt.square()
  hw_sqit = sqInt.square()
  if ta_sqit == hw_sqit:
    sess.x_log("PASSED Public Test: squareInt(4).square()")
    sess.set_score(80)
  sess.update_score(10)

else:
  sess.x_log("ERROR: your function/class names did not match up with those provided in the solution key. please look over your work and resubmit")
final = sess.finalize()

