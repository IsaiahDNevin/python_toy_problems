import statistics

def avg_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum / len(lst)

user_input = input('please input numbers to get the average (eg, 1, 2, 2.5): ')

try:
    avg, lst = user_input.split(',') 
except ValueError:
    print("Invalid input. Please enter in the format '1, 2, 3, 4,'.")
else:
    # Call the function and print the result
    result = (avg_list)
    print(result)

lst = [1, 2, 3, 4, 5]
avg = avg_list(lst)

print(avg)






# 1. Split the sting into a list of numbers
# 2. Add all the numbers together whithout sum method
# 3. Calculate the average 
# 4. Print the average nice and pretty for daddy... dont sue me

