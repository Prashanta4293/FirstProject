try:
    num=10
    a= int(input("enter number: "))
    print(10/a)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Can't divisible by zero")
finally:
    print("No body can stop me.")
        