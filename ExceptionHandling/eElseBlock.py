try:
    num= 10
    a= int(input("Enter Number: "))
    print(num/a)
    
except ValueError:
    print("invalid input")
    
except ZeroDivisionError:
    print(num, "can not divisible by Zero")
        
else:
    print(a, "is a valid input")
        