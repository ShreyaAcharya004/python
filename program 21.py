# Write python function to reverse a string if it's length is a multiple of 4
def rev_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string
original_string = "abcd1234"
result = rev_if_multiple_of_4(original_string)
print(result)