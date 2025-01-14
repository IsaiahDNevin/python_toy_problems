

def palindrome(string):
    iterator = 0
    for char in string:   
        last_index = len(string) - iterator - 1
        l_char = string[last_index]
        iterator += 1
        if l_char != char:
            return False
    return True
        

palindrome("racecar")




def palindrome2(string):
    iterator = 0
    for char in string:
        last_index = len(string) - iterator - 1
        l_char = string[last_index]
        iterator += 1
        if l_char != char:
            return False
    return True

palindrome2("hello")
