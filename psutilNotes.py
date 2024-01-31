import psutil
import os
import signal
import datetime
# -------------------------------- IDEA ---------------------------------------------
"""
What i'm thinking is an infinite while loop checking for 
if the process is open using this for proc in psutil.process_iter method

extracting the .exe name from the list made through the GUI file extractor
into an array/list, then checking for every item in that list
inside the for loop, and returning true if any are launched
"""


# ------------------- receiving Pid of targetApplication ----------------------------

# while True:
for proc in psutil.process_iter(['pid', 'name', 'username']):
    if proc.name() == 'steam.exe':
        print(proc.pid)
        #break
    #else:
         #continue
    #break

"""
Instead of using psutil.pids() we use psutil.process_iter when iterating 
through processes.

We can use psutil.pid_exists(pid) to check if the pid is still running (I think?)

"""

# ------------------------------ Kill process --------------------------------------
target_process = 'steam.exe'
for process in psutil.process_iter(['pid', 'name']):
    if process.name() == target_process:
        try:
            os.kill(process.pid, signal.SIGTERM)
            print('Termination signal sent')
        except OSError as e:
            print('Error')
"""
Here we check if the process.name() in the process iteration is the name of a 
target process, if it is we then try to send a Termination Signal (SIGTERM) to 
the processes pid. This should kill the process, we could also do
SIGKILL or SIGILL if SIGTERM doesn't work. 

SIGKILL is a kill signal and immediately terminate the process
SIGILL is a signal in Unix-like operating systems that stands for Illegal Instruction.
when a process receives a SIGILL signal the default behavior is to terminate
the process immediately """
# ------------------------ disableLaunch of Applications ---------------------------
"""
In order to make applications not be able to be launched again
we can use the kill for ... in loop as a function
and call the function every minute as long as its not a new day
( if the time limit has been reached. )
This makes it so you can launch the applications, but it'll constantly keep
shutting down until the new day.
"""

"""
Make it parental software like, someone else holds a key 
"""