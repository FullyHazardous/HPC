import queue as Queue, threading, os
import shutil
import time

fileQueue = Queue.Queue()
source = './testSrc/'
dest = './dest/'

class ThrCopy:
  allFiles = 0
  copyCount = 0
  lock = threading.Lock()

  def __init__(self):
    fList = os.listdir(source)

    if not os.path.exists(dest):
      os.mkdir(dest)

    self.allFiles = len(fList)
    self.thrCopy(fList)


  def ShutCopy(self):
    while True:
      fName = fileQueue.get()
      shutil.copy(Name, dest)
      fileQueue.task_done()
      with self.lock:
        self.copyCount += 1
        percent = (self.copyCount * 100) / self.allFiles

  def thrCopy(self, titleList):
    for i in range(6):
      t = threading.Thread(target=self.ShutCopy)
      t.daemon = True
      t.start()
    for fName in titleList:
      fileQueue.put(source + fName)
    fileQueue.join()

initTime = time.perf_counter()
ThrCopy()
print(time.perf_counter() - initTime)