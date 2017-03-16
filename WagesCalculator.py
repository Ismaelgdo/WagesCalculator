#IsmaelGarrido WagesCalculator.py
#This program computes the total salary of a employee for a week

def main():
    print("This program computes the total salary  wages for a certain week,")
    print("and calculates the total wage if an employee exceed 40 hours.")
    payroll = 0
    employee = 'y'
    

    while employee[0] == 'y' or 'n':
        Hours = eval(input("\nPlease enter the total number of hours worked: "))
        Rate = eval(input("Please enter the hourly rate: "))
        if Hours <= 40:
            Salary = Hours * Rate
        
        else:
            Salary = Rate * 40 + (Hours - 40) * 1.5 *(Rate)
            payroll = payroll + Salary
        print("The total net salary for this week is", Salary,"$")
        
        Employee = input ("\nDo you wish to compute the salary of more " 
                          "employees? Enter Y for yes and N for no: ")

        if employee == 'n' or 'N':
            print ("Thanks for using this program!")
            break
        else:
            continue
    
main()

"""
This program computes the total salary  wages for a certain week,
and calculates the total wage if an employee exceed 40 hours.

Please enter the total number of hours worked: 45
Please enter the hourly rate: 12.5
The total net salary for this week is 593.75 $

Do you wish to compute the salary of more employees? Enter Y for yes and N for no: n
Thanks for using this program!

"""
