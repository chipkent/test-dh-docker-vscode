

print("In run_me.py")

import debugpy
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

def threading_test():
    print(f"CALLING: threading_test thread={threading.get_ident()} thread={threading.current_thread()}")
    print("In Threading Test")

thread = threading.Thread(target = lambda: threading_test(), args=())
thread.start()
thread.join()

def update_func():
    print(f"CALLING: update_func thread={threading.get_ident()} thread={threading.current_thread()}")
    return 1

t2 = t.update("Y=update_func()")

while True:
    input("Press enter to exit:\n")
    break

print("DONE")
