# Write a Python program to count occurrences of a substring in a string.
def counting(str,str2):
    count=str.lower().count(str2.lower())
    return count
    str="hello,how are you ,are u ok?"
    str2="whats up"
    occurrences= counting(str,str2)
    print("the str2'{str}occurs{str2}times in the string")
