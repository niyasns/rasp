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
        print_time(self.name, self.counter, 2)
        threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def print_text():
    print("10 seconds : ping")
    threading.Timer(10, print_text).start()

threadLock = threading.Lock()
threads = []

threadRecord = raspThread(1, "Record", 10)

threadRecord.start()
print_text()

threads.append(threadRecord)

for t in threads:
    t.join()

print ("Exiting Main Thread")
