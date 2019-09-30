import shutil
import os
import time

source = './testSrc/'
dest = './dest/'

if not os.path.exists(dest):
  os.mkdir(dest)

data = os.listdir(source)

initTime = time.perf_counter()

for x in data:
  shutil.copy(source + x, dest)

print(time.perf_counter() - initTime)