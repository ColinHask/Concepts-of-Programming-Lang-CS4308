while True:
    try:
        print("--- Trapezoid Area Calculator ---\n")
        b1 = int(input("Enter base 1 length: "))
        b2 = int(input("Enter base 2 length: "))
        h = int(input("Enter height: "))

        #area formula
        a = ((b1+b2)/2)*h
        print(f"Area: {a}")
    except:
        print(f"Invalid Input, please try again.")
