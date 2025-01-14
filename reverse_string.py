
def reverse_string(string):
    backward_string = ""
    for l in string:
        backward_string = l + backward_string
    return backward_string

reverse_string("hello")

