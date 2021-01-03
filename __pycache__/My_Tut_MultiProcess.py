import time

def arument1(*args):
    return args
# start = time.asctime(time.localtime(time.time()))
start = time.time()
my_Language = ['java', 'java script', 'c++', 'c', 'c#', 'ruby', 'css' ]
arument1(my_Language.append('html'))
arument1(my_Language.insert(0, 'yaml'))
print(my_Language)
end = time.time()
ti = time.asctime(time.localtime(time.time()))
print(ti)    
print(start - end, 'seconds')