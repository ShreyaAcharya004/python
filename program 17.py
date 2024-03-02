#write a python program to get a single string from two given strings, separated by a space and swap the first  two chacters of each string.
def swapcombinestring(str1,str2):
    swapstr1=str2[:2]+str1[2:]
    swapstr2=str1[:2]+str2[2:]
    combinedstring=swapstr1+' '+swapstr2
    return combinedstring

string1=input("first string:")
string2=input("secondstring:")
result=swapcombinestring(string1,string2)
print(result)