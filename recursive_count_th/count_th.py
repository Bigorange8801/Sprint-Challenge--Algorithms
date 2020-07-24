'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    count = 0

    def th_amount(word, i):
        if i > 0:
            to_match = word[i-2:i]
            print(to_match)
            if to_match == "th":
                nonlocal count
                count += 1
            th_amount(word, i-1)

    th_amount(word, len(word))
    return count