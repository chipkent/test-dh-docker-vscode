
import sys

print("In run_me.py")
sys.stdout.flush()

import debugpy
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


# from deephaven_server import Server
# server = Server(port=10000, jvm_args=['-Xmx4g'])
# server.start()

# # UGP lock is automatically acquired for each query operation
# from deephaven import ugp
# ugp.auto_locking = True

# import threading
# print(f"CALLING: main thread={threading.get_ident()} thread={threading.current_thread()}")

# import mypkg

# t = mypkg.get_tt()
# print(t.to_string())

# e = mypkg.get_et()
# print(e.to_string())

# def exec_test():
#     print(f"CALLING: exec_test thread={threading.get_ident()} thread={threading.current_thread()}")
#     print("In Exec Test")

# exec("exec_test()")

# def update_func():
#     print(f"CALLING: update_func thread={threading.get_ident()} thread={threading.current_thread()}")
#     return 1

# t2 = t.update("Y=update_func()")

# while True:
#     input("Press enter to exit:\n")
#     break

print("DONE")
sys.stdout.flush()
