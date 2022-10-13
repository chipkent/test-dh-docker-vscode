
from deephaven_server import Server
server = Server(port=10000, jvm_args=['-Xmx4g'])
server.start()

# UGP lock is automatically acquired for each query operation
from deephaven import ugp
ugp.auto_locking = True

import mypkg

t = mypkg.get_tt()
print(t.to_string())

e = mypkg.get_et()
print(e.to_string())

def exec_test():
    print("In Exec Test")

exec("exec_test()")

while True:
    input("Press enter to exit:\n")
    break
