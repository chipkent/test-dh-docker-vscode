
import threading
from deephaven import time_table, empty_table
from deephaven.table import Table

# import debugpy

def get_tt() -> Table:
    # debugpy.debug_this_thread()
    print(f"CALLING: get_tt thread={threading.get_ident()} thread={threading.current_thread()}")
    return time_table("00:00:01").update("X = ii")

def get_et() -> Table:
    # debugpy.debug_this_thread()
    print(f"CALLING: get_et thread={threading.get_ident()} thread={threading.current_thread()}")
    return empty_table(100).update("X = ii")