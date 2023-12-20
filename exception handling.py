a = 5
b = 0


try:
    print("resource opened")
    print(a/b)
    k = int (input("enter a number"))
    print(k)

except ZeroDivisionError as f:
    print("Hey,you cannot divide a num by zero",f)
except ValueError as f:
    print("invalid input")
except Exception as f:
    print("something went wrong..!!")
finally:
    print("resource closed")
print("bye")