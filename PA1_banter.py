#Client name: Dr. Amy Connolly
#Programmer name: Matthew Woodson
#PA Purpose: To take input from user and then have a small conversation
#My submission of this program indicates that I have neither recieved nor given substnatial
#or unauthoized assistance in writing this program
import time
name = input("\nWhat is your name?  ")
time.sleep(.5)

mood = input("\nHello {} how are you feeling today? ".format(name))
print("\nInteresting to hear you are", mood)
time.sleep(.75)
age = input("How old are you today, {}? ".format(name))
time.sleep(1)
print("\nYou,", name,"are",age,"years old today and feeling",mood,". Goodbye!")
