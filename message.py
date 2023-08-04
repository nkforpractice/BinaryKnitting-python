#Jue Wu
#12/6/2022
#CS5001
#Final Project
#Using replace() function to remove space of the message and using bin() function to convert the message into binary message


def removeSpace(message):
    '''Delete the space of the received message'''
    #using the replace() function to delete the space of the receive message
    noSpaceM = message.replace(" ","")
    return noSpaceM

def toBinary(noSpaceM):
    '''Change the message into binary'''
    byte_array = noSpaceM.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)
    no0bString = '0' + binary_string[2:]
    return no0bString