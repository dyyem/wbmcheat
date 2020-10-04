words_list = open("words.txt", "r+").read().split("\n")

def solve(prompt):
    for word in words_list:
        if prompt in word and prompt != word and prompt + "s" != word:
            return word
