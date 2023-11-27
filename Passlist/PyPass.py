from itertools import product
import math
import string
import time
from termcolor import cprint

cprint("Hello welcome to my tool PyPass",'green')
All = string.ascii_lowercase + ' ' + string.ascii_uppercase + string.digits + string.punctuation
cprint("Enter the characters you want to use [Type 'All' for default]: ",'blue')
Characters = input(">>> ")
if Characters in ['all','All']:
    Characters = All
cprint("Enter a minimum length: ",'green')
minimum = input(">>> ")
cprint("Enter a maximum length: ",'green')
maximum = input(">>> ")
try:
    Minima = int(minimum)
    Maxima = int(maximum)
except:
    cprint(str(Exception),'red')
words_pl = []
for x in range(Minima , Maxima + 1):
    words_pl.append(math.pow(len(Characters),x))
Total_Pass = math.fsum(words_pl)
cprint("Enter file path [Use \\\\ to specify directory]: ",'cyan')
path = input(">>> ")
try:
    file = open(path,'w')
except:
    cprint("Failed to create file. Check your file path and try again.",'red')
cprint(f"Making wordlist with {int(Total_Pass)} words. Process starting withing 5 seconds.",'blue')
time.sleep(4)
start = time.time()
cprint("Processing...",'cyan')
for x in range(Minima, Maxima + 1):
    words = product(Characters,repeat = x)
    for i in words:
        word = "".join(i)
        file.write(word)
        file.write('\n')
file.close()
end = time.time()
TIME = end - start
cprint(f"Wordlist created successfully within {TIME} seconds.",'green')
cprint("Thanks for using PyPass.",'cyan')