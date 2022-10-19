
import sys

print("In run_me.py")
sys.stdout.flush()

import debugpy

# print(dir(debugpy))
# print(debugpy.__version__)
# print(debugpy.__file__)
# print(debugpy.__path__)

# print("debugpy contents")
# import glob
# print(glob.glob(f"{debugpy.__path__[0]}/*"))
# import os
# os.system(f"ls {debugpy.__path__[0]}")
# print("find debugpy")
# os.system("find / -name \*debugpy\*")
# os.system(f"echo 'find debugpy.__path__' && find {debugpy.__path__[0]}")

# import debugpy._vendored.pydevd as pydevd
# import pydevd
# import debugpy
# pydevd = debugpy._vendored.import_module("pydevd")

# print("pydevd contents")
# print(dir(pydevd))
# print(help(pydevd))
# print(glob.glob(f"{pydevd.__path__}", recursive=True))
# # print(type(pydevd.pydevd))
# print("--")
# print(glob.glob("/usr/local/lib/python3.10/dist-packages/debugpy/_vendored/**"))

# pydevd.settrace(suspend=False, trace_only_current_thread=False)

# import pydevd
# # pydevd.settrace(host="", port=10001, suspend=False, trace_only_current_thread=False)
# pydevd.settrace(port=10001, suspend=True, trace_only_current_thread=False)


debugpy.listen(("", 10001))
debugpy.wait_for_client()
debugpy.breakpoint()

print("after breakpoint")
sys.stdout.flush()

print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")


# import debugpy
# debugpy.configure(subProcess=False)
# import pydevd
# pydevd.settrace(suspend=False, trace_only_current_thread=False)
# import debugpy
# debugpy.configure(subProcess=True)

# import debugpy._vendored.pydevd as pydevd
# import pydevd
# import debugpy
# pydevd = debugpy._vendored.import_module("pydevd")
# pydevd.settrace(suspend=False, trace_only_current_thread=False)

# import debugpy
# debugpy.debug_this_thread()


# import pydevd
# import debugpy
# pydevd = debugpy._vendored.import_module("pydevd")
# pydevd.settrace(suspend=False, trace_only_current_thread=False)


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
sys.stdout.flush()
