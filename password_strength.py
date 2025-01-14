password = "happycat"
special_characters = ["#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", "!"]

password_length = len(password)
upper_case = (password.isupper())

def has_special_char (str):
    for char in special_characters:
        if char in str:
            return True     # if you return. it stops the for loop
    return False

def has_upper_char(str):
    split_str = list(str)
    for char in split_str:
        if char.isupper():
            return True
    return False

def strength(pw):
    if password_length < 8:
        print("this password should be longer")
        return strength(input("Please input a longer password : "))
    elif has_upper_char(pw) == False:
        print("Please add at least 1 uppercase letter")
        return strength(input("Please add one upper Case letter : "))
    elif has_special_char(pw) == False:
        return strength(input(f"Must include one of the following: {','.join(special_characters)} : "))
    else:
        return True

print(strength("happycat!"))

