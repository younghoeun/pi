import psutil
import os

my_pid = os.getpid()

for proc in psutil.process_iter():
   try:
      processName = proc.name()
      processID = proc.pid

      if proc.pid == my_pid:
         print("I am not suicidal")
         continue

      if processName.startswith("python"):
         print(f"I will kill {processName}[{processID}] : {''.join(proc.cmdline())})")
         proc.kill()
   except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
      print(e)
