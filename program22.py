#Write a python program to get a string made of the first 2 and the last  2 chars from a given a string
def get_first_and_last_2_chars(input_string):
    if len(input_string) < 2:
        return ''  # Return an empty string if the length is less than 2
    else:
        return input_string[:2] + input_string[-2:]

givenstring = "abcdef"
result = get_first_and_last_2_chars(givenstring)
print(result)