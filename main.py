#Edge case of 12pm midnight when starting at 9pm
#Available time architecture needs rework ( track-real time. check every 60 seconds with time.sleep)
#Understanding how 2 GUI


print("This will always be ran")


def main():
    print("Second Version Main Method")
    AVAILABLE_TIME = 3
    trackDay()
    detectGame()
    #Write more of a main


def startTrackingTime() :
    startTime = time.localtime()


def endTrackingTime() :
    endTime = time.localtime()
    trackedTime = startTime - endTime
    AVAILABLE_TIME -= trackedTime
def detectGame() :
    if game is open :
        startTrackingTime()
    else if game is close :
        endTrackingTime()
def forceCloseGame() :
    if trackingTime(EndLimit) == True :
        sys.close game


def cantStart() :
    if trackingTime(HasReachedDailyLimit) == True :
        sys.cant open game()

def trackDay() :
    while gameIsOpen :
        trackRealTime


def updateAvailableTime() :






def checkAvailableTime():
    print("Checking")










    if __name__ == "__main__":
        main()

