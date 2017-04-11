def words(filename, str1):
    infile = open(filename)
    content = infile.read()
    infile.close()

    return content.count(str1)

print(words('C:\\frankenstein.txt','laboratory'))
print(words('C:\\frankenstein.txt','Frankenstein'))
print(words('C:\\frankenstein.txt','monster'))
