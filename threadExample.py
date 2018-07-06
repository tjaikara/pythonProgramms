import threading
import time

exitFlag = 0

class myThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(" Staring "+ self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting "+ self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadOne = myThread(1, "Thread-1", 5)
threadTwo = myThread(2, "Thread-2", 10)

threadOne.start()
threadTwo.start()

print("Exiting Main Thread")