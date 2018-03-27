import threading
import time

class raspThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Staring recording with thread name " + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 1)
        threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

threadRecord = raspThread(1, "Record", 5)

threadRecord.start()

threads.append(threadRecord)

for t in threads:
    t.join()

print ("Exiting Main Thread")
