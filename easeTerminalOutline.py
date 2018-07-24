import os


internet = ["internet", "web", "google", "browser"]

email = ["gmail", "email", "yahoomail", "outlook",
        "hotmail"]

word = ["word", "blank", "blank page", "microsoft word", "word processor"]

excel = ["spreadsheet", "excel", "microsoft excel"]

powerpoint = ["powerpoint", "slideshow", "slides", "presentaton"]

calculator = ["calculator", "calculate", "math", "mathematics"]

volume = ["volume", "sound", "loud", "loudness", "quiet", "quieter", "louder", "mute", "unmute", "soft", "softer"]

brightness = ["brightness", "brighten", "dim", "dimmer", "light", "lighten", "bright"]

printing = ["print", "printing"]

save = ["save", "saving", "keep", "download"]

flashdrive = ["flash drive", "flashdrive", "usb", "usb drive", "usbdrive", "thumbdrive", "usb stick", "thumbstick", "stick"]

logout = ["logout", "close", "end"] # will need a prompt for are you sure you want to close out of everything

def configure():

    # if the paths for these different things are the same on all windows/linux/macs, we could just have them select which one they want to use
    # and then have the correct path already written down based on their selection

    print("Enter all of the web browsers installed on your computer: (Google Chrome, Mozilla Firefox, Microsoft Edge, Internet Explorer, Opera, Safari, Other")
    # this will be "Select" in the GUI and they can pick them graphically
    print("If Other, enter the path for them ")

    print("Enter the path to your word processor (it could be Microsoft Word, pages, openoffice, or something else:") 
    forWord = input()
    forWord = lower(forword)

    print("Enter the path to your spreadsheet application (it could be Microsoft Excel, open office, or something else:")
    forExcel = input()
    forExcel = lower(forExcel)

    print("Enter the path to your slides application (it could be Microsoft powerpoint, open office, or something else:")
    forPowerpoint = input()
    forPowerpoint = lower(forPowerpoint)

    print("Enter the path to your calculator application:") # if this is in a standard location on the computers - wouldn't need to have them configure it
    forPowerpoint = input()
    forPowerpoint = lower(forPowerpoint)


# paths will be different for windows/linux/mac
# needs to be setup to go into the os and open the path

def runProgram():
    x = input()

    if x in internet:
        open forInternet # /path/to/browser

    elif x in email:
        open # https://linkToPageWithEmailLinks.com

    elif x in word:
        open forWord # /path/to/word
    
    elif x in excel:
        open forExcel # /path/to/excel
    
    elif x in powerpoint:
        open forPowerpointc # /path/to/powerpoint
    
    elif x in calculator:
        open forCalculator # /path/to/calculator
    
    elif x in volume:
        open the custom gui volume slider

    elif x in brightness:
        open the custom gui brightness slider
    
        



    

