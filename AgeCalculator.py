# Age Calculator
from datetime import date

print("Hello Welcome to Age Calculator..! Please Enter your Birth Date")

go = "y"

def age():
    b_date = int(input("Birth Date: "))
    if( (1 > b_date) | (b_date> 31 )):
        print("Invalid Birth Date")
    else:
        b_month = int(input("Birth Month: "))
        if( (1 > b_month) | (b_month> 12 )):
            print("Invalid Birth month")
        else:
            b_year = int(input("Birth Year: "))
            if (b_year < 1940):
                print("Invalid  Birth year")
            else:
                print(f"Birth Date is : {b_date}-{b_month}-{b_year}")

                today = str(date.today())
                list_today = today.split("-")

                print(f"Todays date is: {list_today[2]}-{list_today[1]}-{list_today[0]} ")
                month = [31,28,31,30,31,30,31,31,30,31,30,31]

                c_date = int(list_today[2])
                c_month = int(list_today[1])
                c_year = int(list_today[0])

                if (b_date > c_date):
                    c_month = c_month -1
                    c_date = c_date + month[b_month - 1]
                if(b_month>c_month):
                    c_year = c_year -1
                    c_month = c_month + 12

                rt_date = str(c_date - b_date)
                rt_month = str(c_month - b_month)
                rt_year = str(c_year - b_year)

                print(f"Your current age is {rt_year} years, {rt_month} months and {rt_date} Days old")
                k = input("\n Do you wants to continue? Y / N ").lower()
                global go
                if (k == "n"):
                    go = k
                else:
                    print("Try again")


while(go is not "n"):
    # go = input("\n Do you wants to continue? Y / N").lower()
    if (go == "y"):
        age()
    elif(go == "n"):
        break
    else:
        print("Try again, invalid input")
