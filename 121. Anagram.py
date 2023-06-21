def isAnagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    str1=sorted(str1)
    str2=sorted(str2)
    if(str1==str2):
        print("The string is anagram")
    else:
        print("The string is not anagram")

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

isAnagram(str1,str2)
