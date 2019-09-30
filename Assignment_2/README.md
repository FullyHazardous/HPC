# HPC Homework 2
# to setup the program you need to create test files in the folder testSrc then run the .py files with python 3
dd if=/dev/zero of=filename.txt count=1024000 size=1024

cp filename.txt filename2.txt

cp filename.txt filename3.txt

cp filename.txt filename4.txt



# test results for four 1024MB fies:
copy.py - 8.287555631 seconds

thread.py - 5.627334852000001 seconds

processes.py - 4.254924563 seconds 

