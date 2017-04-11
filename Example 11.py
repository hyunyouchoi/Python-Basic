def rvowels(s):
    if len(s) == 0:
       return 0
    elif s[0] in "aeiouAEIOU":
         return rvowels (s[1:])+1
    else:
         return rvowels (s[1:])+0 
     
import time

beg = time.time()

for i in range(100):

 print(rvowels("this is a test to see if my program can accurately count the vowels"))

end = time.time()

print("Elapsed time for recursive method: ", end-beg)
