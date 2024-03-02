#Write a python function to insert a string in the middle of a string
def insert_in_middle(basse_string, insert_string):
    middle_index = len(base_string) // 2
    return base_string[:middle_index] + insert_string + base_string[middle_index:]

# Example usage:
original_string = "shreya acharya"
inserted_string = "123"
result = insert_in_middle(original_string, inserted_string)
print(result)
