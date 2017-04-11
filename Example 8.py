def vowels(s):
     
     count = 0
     for char in s:
         if(char=='a'or char=='e'or char=='i'or char=='u'or char=='o'):
            count = count + 1

     return count

i = input("plz enter sentence:  ")  
ans=vowels(i)
print(ans)


