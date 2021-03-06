import json
import sanity
import datetime
# from modproxy import ModuleProxy, ObjectProxy

class Session():
  '''
  Session object: a session object takes in two modules (a key, or solution module, and a submission module)
  it stores the results of the compare() function and maintains various logs and score information
  '''
  def __init__(self, ta_obj, hw_obj):
    self.start_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S%p")
    self.ta_obj = ta_obj
    self.hw_obj = hw_obj
    self.DATA_DIR = ''
    self.DATA_FILE = 'data.json'
    self.log = {"info":{}, "internal_log":[], "external_log":[], "sanity_compare":{}, "score_sum": None, "max_score": None}
    self._load_data()

  def get_module_proxy(self):
    return self.hw_proxy

  def test_hw_function_single(self, name, pub_inputs, priv_inputs):
    '''
    compares a given submitted function against a correctly implemented
    version of the same function over two sets of inputs. The first failure
    of a public input is reported if it occurs. Private input failures are
    only reported as having failed a private test but not the input the caused
    it to fail. Ive included name for now as an easy way to display the function
    being tested.
    '''
    try:

      hw_func = sanity.getfunction(self.hw_obj, name)
 
      ta_func = sanity.getfunction(self.ta_obj, name)

      pub_count = 0
      fail = False
    
      for i in pub_inputs:
        hw_func_result = hw_func(i)
        if hw_func_result == ta_func(i):

          pub_count += 1
          self.i_log("{!s} returned correct result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))

        else:
     
          self.x_log("{!s} returned incorrect result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))
          self.i_log("{!s} returned incorrect result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))
          fail = True
          return False
          # break
      if pub_count == len(pub_inputs):
        self.x_log("All public tests for {!s} passed. So far so good.".format(name))
        self.i_log("All public tests for {!s} passed.".format(name))
        

      priv_count = 0
      if not fail:
        for i in priv_inputs:
          if hw_func(i) == ta_func(i):
            priv_count += 1
            self.i_log("Correct result on input {!s}.".format(str(i)))
          else:
            self.x_log("Your code ran incorrectly on a private test. Please try again")
            self.i_log("Incorrect result on input {!s}.".format(str(i)))
            return False
            # break
        if priv_count == len(priv_inputs):
          self.x_log("All tests for {!s} passed. Good job!".format(name))
          self.i_log("All tests for {!s} passed.".format(name))
          return True
    except:
      self.x_log("Exception raised while running tests on {!s}. Try testing to see if you can recreate the exception and solve it.".format(name))
      self.i_log("Exception raised... hopefuly not our fault.")
      return False

  def test_hw_function_multi(self, name, pub_inputs, priv_inputs):
    '''
    compares a given submitted function against a correctly implemented
    version of the same function over two sets of inputs. The first failure
    of a public input is reported if it occurs. Private input failures are
    only reported as having failed a private test but not the input the caused
    it to fail. Ive included name for now as an easy way to display the function
    being tested. Works on functions with multiple inputs passed as n-ary tuples
    in the input lists with each element having the same arity as the number of
    function arguments.
    '''
    try:
      hw_func = sanity.getfunction(self.hw_obj, name)
      ta_func = sanity.getfunction(self.ta_obj, name)
      pub_count = 0
      fail = False
      for i in pub_inputs:
        hw_func_result = hw_func(*i)
        if hw_func_result == ta_func(*i):
          pub_count += 1
          self.i_log("{!s} returned correct result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))
        else:
          self.x_log("{!s} returned incorrect result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))
          self.i_log("{!s} returned incorrect result of {!s} on input {!s}.".format(name, str(hw_func_result), str(i)))
          fail = True
          return False
          # break
      if pub_count == len(pub_inputs):
        self.x_log("All public tests for {!s} passed. So far so good.".format(name))
        self.i_log("All public tests for {!s} passed.".format(name))
        
      priv_count = 0
      if not fail:
        for i in priv_inputs:
          hw_func_result = hw_func(*i)
          if hw_func_result == ta_func(*i):
            priv_count += 1
            self.i_log("Correct result on input {!s}.".format(str(i)))
          else:
            self.x_log("Your code ran incorrectly on a private test. Please try again")
            self.i_log("Incorrect result on input {!s}.".format(str(i)))
            return False
            # break
        if priv_count == len(priv_inputs):
          self.x_log("All tests for {!s} passed. Good job!".format(name))
          self.i_log("All tests for {!s} passed.".format(name))
          return True
    except:
      self.x_log("Exception raised while running tests on {!s}. Try testing to see if you can recreate the exception and solve it.".format(name))
      self.i_log("Exception raised... hopefuly not our fault.")
      return False
  
  
  def _arg_compare(self, ta_obj, hw_obj):
    '''
    _arg_compare() takes two objec
    '''
    log = []
    ta_funcs = set(sanity.listfunction_names(ta_obj))
    hw_funcs = set(sanity.listfunction_names(hw_obj))
    ta_farg = {f:sanity.getfunction_argcount(ta_obj, f) for f in ta_funcs}
    hw_farg = {f:sanity.getfunction_argcount(hw_obj, f) for f in hw_funcs}
    args_there = True #innocent until proven guilty

    for func, arg_count in ta_farg.items():
      hw_arg_count = hw_farg[func]
      if arg_count == hw_arg_count:
        log.append("PASSED@{!s}: {!r} args defined in ta-{!s}. {!r} args in submitted-{!s}".format(func, arg_count, ta_obj.__name__ + "." + func, hw_arg_count, hw_obj.__name__ + "." + func))
      else: 
        log.append("ERROR@{!s}: {!r} args defined in ta-{!s}. {!r} args in submitted-{!s}".format(func, arg_count, ta_obj.__name__ + "." + func, hw_arg_count, hw_obj.__name__ + "." + func))
        self.x_log("You defined {!r} args in submitted-{!s}, there should be {!r} argument(s)".format(hw_arg_count, hw_obj.__name__ + "." + func, arg_count))
        args_there = False
    return args_there, log


  def compare(self):
    '''
     compare() does a basic comparison of two modules (or objects), checking to make sure that all functions and classes
     are defined with the appropriate number of arguments. returns true if so, false otherwise.
    ''' 

    all_there = True #innocent until proven guilty
    ta_module = self.ta_obj
    hw_module = self.hw_obj

    #scrape functions from top level:
    ta_top_lvl = set(sanity.listfunction_names(ta_module))
    hw_top_lvl = set(sanity.listfunction_names(hw_module))
    if ta_top_lvl <= hw_top_lvl:
      all_there, log = self._arg_compare(ta_module, hw_module)
      self._clog("top_lvl_funcs", log)
    else:
      #also log the missing ones
      missing = ta_top_lvl - hw_top_lvl
      missing_str = ", ".join(str(e) for e in missing)
      self._clog("top_lvl_funcs", "ERROR: some top level function(s) defined in ta-{!s} are missing in submitted-{!s}: {!s}".format(ta_module.__name__, hw_module.__name__, missing_str))
      self.x_log("You are missing some top level function(s) in {!s}: {!s}".format(hw_module.__name__, missing_str))
      all_there = False

    #scrape classes from TA_file, hw_file, and compare them
    hw_class_dict = sanity.getclass_dict(hw_module)
    ta_class_dict = sanity.getclass_dict(ta_module)
    ta_class_names = set(ta_class_dict.keys())
    hw_class_names = set(hw_class_dict.keys())
    common_class_names = ta_class_names & hw_class_names

    #high level check to make sure all the classes in TA_module are defined in hw_module (no check to see if there's extra stuff defined in hw_module)
    if ta_class_names <= hw_class_names:
      self._clog("classes", "PASSED: all the classes in ta-{!s} exist in {!s}".format(ta_module.__name__, hw_module.__name__))

    else:
      missing = ta_class_names - hw_class_names
      missing_str = ", ".join(str(e) for e in missing)
      self._clog("classes", "ERROR: some classes defined in ta-{!s} are missing from submitted-{!s}: {!s}".format(ta_module.__name__, hw_module.__name__, missing_str))
      self.x_log("You are missing some classes in {!s}: {!s}".format(hw_module.__name__, missing_str))
      all_there = False

    #scrape functions from the common classes:
    for cls_name in common_class_names:
      hw_cls = hw_class_dict[cls_name]
      ta_cls = ta_class_dict[cls_name]
      ta_cls_funcs = set(sanity.listfunction_names(ta_cls))
      hw_cls_funcs = set(sanity.listfunction_names(hw_cls))
      cls_func_compare = str(cls_name)+"_funcs"
      if ta_cls_funcs <= hw_cls_funcs:
        cls_args_there, log = self._arg_compare(ta_cls, hw_cls)
        self._clog(cls_func_compare, log)
        if all_there and not cls_args_there:
          all_there = False
      else:
        missing = ta_cls_funcs - hw_cls_funcs
        missing_str = ", ".join(str(e) for e in missing)
        self._clog(cls_func_compare, "ERROR: some functions defined in ta-{!s}'s class {!s} are missing from submitted-{!s}'s class {!s}: {!s}".format(ta_module.__name__, cls_name, hw_module.__name__, cls_name, missing_str))
        self.x_log("Your class {!s} is missing some functions: {!s}".format(hw_module.__name__ +"." + cls_name, missing_str))
        all_there = False

    return all_there



  def _load_data(self):
    '''.
    used internally: _load_data(): grabs the small json object passed in
    '''
    submission_data = self.DATA_DIR + self.DATA_FILE
    with open(submission_data) as data_file: 
      self.data = json.load(data_file)

  def get_attempts(self):
    '''
    get_attempts returns the number of attempts on this problem / problem set
    '''
    attempts = self.data['attempts']
    return attempts

  def get_timedelta(self):
    '''
    gettimedelta returns the 0(on time) or -1 (late) on this problem / problem set, just a placeholder for now
    '''
    timedelta = self.data['timedelta']
    return timedelta

  def get_prevscore(self):
    '''
    get_prevscore returns the previous score (if any, one this problem)
    '''
    prevscore = self.data['prevscore']
    return prevscore

  def _info(self, key, message):
    '''
    used internally: _info logs to the 'info' key of the session log, 
    contains data about the session object
    '''
    self.log["info"][key] = message

  def _clog(self, key, message):
    '''
    used internally: _clog logs to the 'sanity_compare' key of the session log
    can be accessed by the TA
    '''
    # if key not in self.log["sanity_compare"]:
    #   self.log["sanity_compare"][key] = []
    # self.log["sanity_compare"][key].append(message) 
    self.log["sanity_compare"][key] = message

  def i_log(self, message):
    '''
    for external use: logs to the internal portion of the session log, 
    anything logged here is saved to the database for the TA's reference
    '''
    self.log["internal_log"].append(message)

  def x_log(self, message):
    '''
    for external use: logs to the external portion of the session log, anything logged here
    is passed back to the student
    '''
    self.log["external_log"].append(message)

  def set_max_score(self, max_score):
    '''sets the max score for the problem'''
    self._maxscore = max_score

  def set_score(self, new_score):
    ''' sets the new score for the homework '''
    # self.log["score_sum"].append("score set: {!r}")
    self._score = new_score

  def get_score(self):
    '''returns the current score'''
    return self._score

  def update_score(self, score_mod):
    ''' changes the value of self._score by the (int) given '''
    self._score += score_mod

  def finalize(self):
    '''
    for external use: finalize computes the final score (using the values of the score key)
    and logs the start & end times of the session, along with some data about the problem set
    finally, it dumps the log into a json object
    '''
    self.log["score_sum"] = self._score
    self.log["max_score"] = self._maxscore
    self.end_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S%p")
    self._info("start_time", self.start_time)
    self._info("end_time", self.end_time)
    self._info("timedelta", self.get_timedelta())
    self._info("attempts", self.get_attempts())
    self._info("final score", self._score)
    self._info("max score", self._maxscore)

    print(json.dumps(self.log))
    return json.dumps(self.log)
     
  def tab_report(self):
    if sanity.find_tabs(self.hw_obj):
      self.x_log("It looks like you are using tabs in your source code. You should configure your editor so it changes tabs to spaces.")
