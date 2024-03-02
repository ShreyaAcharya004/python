#Write python function  that takes  a list of words  and returns  the length  of the longest one
def longest_word_len(word_list):
    if not word_list:
        return 0
    return max(len(word))for word in word_list)
word=["rose","lotus","chamomile","lavender"]
result=longest_word_len(word)
print(result)
            