import time
import sys
import os
import re

f = open("Test.py","r")
filedata = f.read()
for m in re.finditer("print",filedata):
    