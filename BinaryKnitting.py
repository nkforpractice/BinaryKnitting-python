#Jue Wu
#12/6/2022
#CS5001
#Final Project
#BinaryKnitting Class

class BinaryKnitting:
    def __init__(self, text):
        '''Constructor'''
        self.message = text


    def knit(self):
        '''
        Using conditionals to convert the binary message into knitting stitches
        '''
        n = 1
        #create a list to contain the stitches return
        knitway = []
        #using for loop and conditional to calculate the successive same number in binary message
        for i in range(1,(len(self.message))):
            if self.message[i] == self.message[i - 1]:
                n += 1
                if i + 1  == len(self.message):
                    if self.message[i] == '1':
                        knitway.append("k"+str(n))
                    elif self.message[i] == '0':
                        knitway.append("p"+str(n))
            else:
                if self.message[i - 1] == '1':
                    knitway.append("k"+str(n))
                    n = 1
                    if i + 1  == len(self.message):
                        if self.message[i] == '1':
                            knitway.append("k"+str(n))
                        elif self.message[i] == '0':
                            knitway.append("p"+str(n))
                elif self.message[i - 1] == '0':
                    knitway.append("p"+str(n))
                    n = 1
                    if i + 1  == len(self.message):
                        if self.message[i] == '1':
                            knitway.append("k"+str(n))
                        elif self.message[i] == '0':
                            knitway.append("p"+str(n))
        return knitway

    def pattern(self, string01):
        #replace the binary message to pattern
        stringPattern = string01.replace("1", u"\u2573").replace("0",u"\u2551")
        return (stringPattern + "\n")*10

