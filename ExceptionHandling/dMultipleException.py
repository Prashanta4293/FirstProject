try:
    a= int(input("Enter Number: "))
    print(10/a)
    
except ValueError:
        print("invalid Input")
        
except ZeroDivisionError:
        print("can not divide by Zero")
        
        