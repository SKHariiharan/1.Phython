class multipleFunctions():
    
    @staticmethod
    def oddEven():
        num = int(input("Enter any number: "))
        if num % 2 == 0:
            print("The number is even")
            return "Even Number"
        else:
            print("The number is odd")
            return "Odd Number"

    @staticmethod
    def Mrg_Eligibility():
        gender = input("Enter the Gender: ")
        age = int(input("Enter the Age: "))
        if gender == "Male":
            if age >= 21:
                print("You are eligible for Marriage")
                return "Eligible"
            else:
                print("You are not eligible for Marriage")
                return "Not Eligible"
        elif gender == "Female":
            if age >= 18:
                print("You are eligible for Marriage")
                return "Eligible"
            else:
                print("You are not eligible for Marriage")
                return "Not Eligible"
        else:
            print("Invalid Gender")
            return "Invalid Input"

    @staticmethod
    def calAverage():
        print("Enter your Marks: ")
        Subject1 = int(input("Tamil: "))
        Subject2 = int(input("English: "))
        Subject3 = int(input("Maths: "))
        Subject4 = int(input("Science: "))
        Subject5 = int(input("Social: "))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Avg = Total / 5
        print("Total =", Total)
        print("Average =", Avg)
        return Avg

    @staticmethod
    def area():
        Height = int(input("Enter the Height: "))
        Breadth = int(input("Enter the Breadth: "))
        Area = (Height * Breadth) / 2
        print("Formula for the Area = (Height × Breadth) / 2")
        return Area

    @staticmethod
    def Perimeter():
        Height1 = int(input("Enter the Height1: "))
        Height2 = int(input("Enter the Height2: "))
        Breadth = int(input("Enter the Breadth: "))
        Perimeter = Height1 + Height2 + Breadth
        print("Formula for the Perimeter = (Height1 + Height2 + Breadth)")
        return Perimeter
