#Typing Test

import time
from time import time

print "WELCOME TO TYPING TEST: \n"

a = "This is Tutorial to Typing test where you can estimate the time"
a1 = "taken by you in WPM. Typing Speed is essential for all computer engineers."
a2 = "I had used time module from Python to estimate your Typing Speed."
a3 = "So lets GET Started to this Amazing Fun of typing. Type the character"
a4 = "as shown exactly similar to written over here. At the end you are going"
a5 = "to get your Desired Results."

result = a+" "+a1+" "+a2+" "+a3+" "+a4+" "+a5

words = len(result.split(' '))

print a+"\n"+a1+"\n"+a2+"\n"+a3+"\n"+a4+"\n"+a5+"\n"

print "\nTYPE the same paragraph as shown"

try:
    raw_input("\nPRESS ENTER key to Continue: \n")

    print "\nYOUR time Starts"

    start = time()

    b = raw_input()
    c = raw_input()
    d = raw_input()
    e = raw_input()
    f = raw_input()
    g = raw_input()

    b = b +" " + c+" " + d+" " + e+" " + f+" " + g+" "

    end = time()

    if b == result:
        print "\nAhh! You typed correctly"

    else:
        print "\nRETRY! The test again to improve your Accuracy!"

    total = round(end - start, 2)

    print "\nYour Typing time is: ",total
    print "\nYour WPM Speed is ",words/total

except KeyboardInterrupt:
    exit(1)
