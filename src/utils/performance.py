import time 

global_start_time_scope = time.time()


def scope_time(get_time: bool):
  global global_start_time_scope
  if (get_time) :
    scope = time.time() - global_start_time_scope
    global_start_time_scope = time.time()
    return (scope)
  else :
    global_start_time_scope = time.time()