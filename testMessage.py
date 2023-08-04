#Jue Wu
#12/6/2022
#CS5001
#Final Project
#test message function

from message import removeSpace
from message import toBinary

def testRemoveSpace():
    if removeSpace("a b c") == "abc":
        print("removeSpace Function works with 'a b c'.")
    else:
        print("Problem with removeSpace function.")

def testToBinary():
    if toBinary("a") == '01100001':
        print("toBinary function work with 'a'.")
    else:
        print("Problem with toBinary function.")


testRemoveSpace()
testToBinary()