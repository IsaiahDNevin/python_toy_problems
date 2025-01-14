# Repol
user_input_height = int(input("input height: "))
user_input_char = input("input char: ")


def pyramid(height, char):
    row_num = 1
    while row_num <= height:     
        blanks = " " * (height - row_num)
        xtra_chars = char * (row_num - 1)     
        chars = xtra_chars + char + xtra_chars 
        row = blanks + chars        
        print(row_num, row)
        row_num += 1


pyramid(user_input_height, user_input_char)

    
    










