import queue as Queue, multiprocessing, os
import shutil
import time

fileQueue = Queue.Queue()
source = './testSrc/'
dest = './dest/'

class mPCopy:
  allFiles = 0
  copyCount = 0
  lock = multiprocessing.Lock()

  def __init__(self):
    fList = os.listdir(source)

    if not os.path.exists(dest):
      os.mkdir(dest)

    self.allFiles = len(fList)
    self.procCopy(fList)


  def ShutCopy(self, Name):
    shutil.copy(source + Name, dest)
    self.lock.acquire()
    self.copyCount += 1
    percent = (self.copyCount * 100) / self.allFiles
    self.lock.release()

  def procCopy(self, titleList):
    pool = multiprocessing.Pool(6)
    pool.map(self.ShutCopy, titleList)
    pool.close()
    pool.join()

initTime = time.perf_counter()
mPCopy()
print(time.perf_counter() - initTime)