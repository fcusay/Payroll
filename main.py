from Payroll import *
from Employee import *

p = Payroll()
e = Employee()

def main():
    print("This Payroll System is need to login to check if you are employee")
    login()

def login():
    e.setUsername()
    e.setPassword()
    if e.isEmployee():
        print("Welcome, Today is", e.getDayOfWork())
        askEmployee()
    else:
        print("Sorry, your Username or Password cannot recognize\nPlease check and try again\n")
        login()

def askEmployee():
    try:
        print("Is holiday today? ")
        is_holiday = input("Yes[y]\t No[n]\n=> ")
        if is_holiday.lower() == 'y':
            print("Note: The time format is military time\nExample\nTime in: 8:00\nTime out: 17:00")
            p.isHoliday(True)
            p.setTimeIn()
            p.setLateTime()
            p.setTimeOut()
            p.setUnderTime()
            e.setSalary(p.getSalary())
            e.generateReport(p.getTimeIn(), p.getTimeOut(), p.getTimeInForOt(), p.getTimeOutForOt())
            e.generateSalary()
            print("You Successfully save your Daily Time Record. \"Please open the file " + "\'" + e.getUsername() + ".txt\'\"")
        elif is_holiday.lower() == 'n':
            print("Note: The time format is military time\nExample\nTime in: 8:00\nTime out: 17:00")
            p.isHoliday(False)
            p.setTimeIn()
            p.setLateTime()
            p.setTimeOut()
            p.setUnderTime()
            e.setSalary(p.getSalary())
            ot = input("Do you want to overtime? if yes press y, if not press any button\n=> ")
            if ot.lower() == 'y':
                print("\nThe time of overtime start in 18:00 to 23:00. Above is not count\n")
                p.setTimeInForOt()
                p.setLateTime()
                p.setTimeOutForOt()
                p.setUnderTime()
                if not p.setOverTime():
                    askEmployee()
            e.generateReport(p.getTimeIn(), p.getTimeOut(), p.getTimeInForOt(), p.getTimeOutForOt())
            e.generateSalary()
            print("You Successfully save your Daily Time Record. \"Please open the file " + "\'" + e.getUsername() + ".txt\'\"")
        else:
            print("\nJust answer Y or N.\n")
            askEmployee()
    except ValueError:
        print("You did not use the system properly, Bye")
    
if '__main__' == __name__:
     main()
