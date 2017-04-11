def vowels(s):
     
     count = 0
     for char in s:
         if(char=='a' or char=='i' or char=='o'or char== 'u' or char=='e'):
            count = count + 1

     return count

import time

beg = time.time()

for i in range(100):
    
    print(vowels("this is a test to see if my program can accurately count the vowels"))

end = time.time()

print("Elapsed time for non-recursive method: ", end-beg)
