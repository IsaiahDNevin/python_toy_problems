def hello(fname, lname, datestring=""):
    msg = "hello " + fname + " " + lname
    if len(datestring) > 0:
        msg += " The date is " + datestring
    print(msg)

hello("isaiah", "nevin", "11/03/2024")

