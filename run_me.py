

print("In run_me.py")

import debugpy

# import threading

# print(dir(threading._DummyThread))

# def new_dummy_thread(*args, **kwargs):
#     print(f"MONKEY PATCHING DUMMY THREAD: {args} {kwargs}")
#     v = threading._DummyThread.__init__(*args, **kwkwargs)
#     print(f"NEW DUMMY THREAD: {v}")
#     return v

# threading._DummyThread.__init__ = new_dummy_thread

# def decorated_thread(fn):
#   def new_func(*args, **kwargs):
#     print("Dummy start")
#     # print(f"override: parent_id={threading.get_ident()}")
#     # args[0].parent_id = threading.get_ident()
#     return fn(*args, **kwargs)
#   return new_func

# threading._DummyThread.__init__ = decorated_thread(threading._DummyThread.__init__)

# threading._DummyThreadOld = threading._DummyThread
# class MyDummyThread(threading._DummyThreadOld):
#     def __init__(self, *args, **kwargs):
#         print(f"Dummy constructor start: {args} {kwargs}")
#         threading._DummyThreadOld.__init__(self, *args, **kwargs)
#         # debugpy.debug_this_thread()
#         print("Dummy constructor end")

#     def start(self):
#         print("Starting thread")
#         threading._DummyThreadOld.start(self)
    

# threading._DummyThread = MyDummyThread



# def decorated_thread(fn):
#   def new_func(*args, **kwargs):
#     print("Dummy start")
#     # print(f"override: parent_id={threading.get_ident()}")
#     # args[0].parent_id = threading.get_ident()
#     fn(*args, **kwargs)
#   return new_func


# threading._DummyThread.start = decorated_thread(threading._DummyThread.start)


# import threading

# def decorated_thread(fn):
#   def new_func(*args, **kwargs):
#     print(f"override: parent_id={threading.get_ident()}")
#     args[0].parent_id = threading.get_ident()
#     fn(*args, **kwargs)
#   return new_func

# threading.Thread.start = decorated_thread(threading.Thread.start)


debug_port = 10001
print(f"Waiting on debugger: {debug_port}")
debugpy.listen(("", debug_port))
debugpy.wait_for_client()
debugpy.breakpoint()

import sys
print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")

from deephaven_server import Server
server = Server(port=10000, jvm_args=['-Xmx4g'])
server.start()

# UGP lock is automatically acquired for each query operation
from deephaven import ugp
ugp.auto_locking = True

import threading
print(f"CALLING: main thread={threading.get_ident()} thread={threading.current_thread()}")

import mypkg

t = mypkg.get_tt()
print(t.to_string())

e = mypkg.get_et()
print(e.to_string())

def exec_test():
    print(f"CALLING: exec_test thread={threading.get_ident()} thread={threading.current_thread()}")
    print("In Exec Test")

exec("exec_test()")

def update_func():
    print(f"CALLING: update_func thread={threading.get_ident()} thread={threading.current_thread()}")
    return 1

t2 = t.update("Y=update_func()")

while True:
    input("Press enter to exit:\n")
    break

print("DONE")
