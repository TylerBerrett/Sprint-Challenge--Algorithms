"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""
# search two letters at a time the remove one the keep track of how many th I find when returning
# return if length of less then one
def count_th(word):
    if len(word) <= 1:
        return 0
    search = word[:2]
    new_word = word[1:]
    if search == 'th':
        return 1 + count_th(new_word)
    return count_th(new_word)
