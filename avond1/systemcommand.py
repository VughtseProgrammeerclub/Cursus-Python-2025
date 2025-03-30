import os

cmd = "dir"

returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)
