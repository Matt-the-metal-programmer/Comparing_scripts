
import subprocess

stdout = subprocess.run(["python3","Test.py"],capture_output=True,text=True).stdout

print(stdout)