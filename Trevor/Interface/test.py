import os

os.chdir('..')
files = str(os.listdir())
# dirs = str(os.walk())


files = files.replace(' ', '\b')
files = files.replace('[', '\b')
files = files.replace(']', '\b')
files = files.replace('\'', '\b')

print(files)
input()

print(dirs)
a,b,c = files.split(',')
print(a)
print(b)
print(c)
print("Where to?")
print("A. Back")
print("B.", a)
print("C.", )
