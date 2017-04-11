def rvowels(s):

 
    if len(s) == 0:
       return 0
    elif s[0] in "aeiouAEIOU":
         return rvowels (s[1:])+1
    else:
         return rvowels (s[1:])+0 
     
i = input("plz enter sentence:  ")  
print(rvowels(i))

