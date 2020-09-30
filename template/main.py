from time import time
import os

called_at = time()
print(f"i got called at: {called_at}")

with open("logs", 'a') as f:
    f.write(f"got called at:{called_at} with pid {os.getpid()} {os.linesep}")
