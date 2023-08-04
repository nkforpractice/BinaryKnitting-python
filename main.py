#Jue Wu
#12/6/2022
#CS5001
#Final Project
#Implementation of BianryKnitting Application

#import Application class
from ApplicationFrame import KnittingApplication


def main():
    #create a knitting application
    app = KnittingApplication()
    #name the title of the application
    app.master.title('BinaryKnitting')
    app.mainloop()



if __name__ == "__main__":
    main()