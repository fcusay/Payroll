class Employee():
    username = ""
    password = ""
    day_of_work = ""
    salary = 0

    def setUsername(self):
        self.username = input("Username: ")

    def setPassword(self):
        self.password = input("Password: ")

    def setSalary(self, salary):
        self.salary = salary

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getSalary(self):
        return self.salary

    def isEmployee(self):
        file = open("list_of_employee.txt", "r")
        user = file.readline().rstrip()
        is_employee = False
        while user != "":
            passw = file.readline().rstrip()
            salary = file.readline().rstrip()
            endline = file.readline().rstrip()
            if self.username == user and self.password == passw:
                is_employee = True
                break;
            user = file.readline().rstrip()
        file.close()
        if is_employee:
            return True
        return False

    def getDayOfWork(self):
        list_of_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        file = open("list_of_employee.txt", "r")
        user = file.readline().rstrip()
        while user != "":
            passw = file.readline().rstrip()
            salary = file.readline().rstrip()
            endline = file.readline().rstrip()
            if self.username == user and self.password == passw:
                if len(salary) != 0:
                    j = 0
                    for i in range(0, len(salary)):
                        if salary[i] == "/":
                            j = j + 1
                    self.day_of_work = list_of_day[j]
                    return list_of_day[j]
                else:
                    self.day_of_work = list_of_day[0]
                    return list_of_day[0]
            user = file.readline().rstrip()
        file.close()

    def generateReport(self, time_in, time_out, time_in_ot, time_out_ot):
        if self.day_of_work != "Friday":
            file = open(self.username+".txt", "a")
            file.write(self.day_of_work + "\n")
            file.write("\tTime in: " + time_in + "\n")
            file.write("\tTime out: " + time_out + "\n")
            file.write("\tTime in OT: " + time_in_ot + "\n")
            file.write("\tTime out OT: " + time_out_ot + "\n")
            file.write("\tSalary: " + "%1.2f"%self.salary + "\n")
            file.close()
        else:
            file = open(self.username+".txt", "a")
            file.write(self.day_of_work + "\n")
            file.write("\tTime in: " + time_in + "\n")
            file.write("\tTime out: " + time_out + "\n")
            file.write("\tTime in OT: " + time_in_ot + "\n")
            file.write("\tTime out OT: " + time_out_ot + "\n")
            file.write("\tSalary: " + "%1.2f"%self.salary + "\n")
            file.close()
            file = open(self.username+".txt", "r")
            total_salary = 0
            for i in range(1, 36):
                temp = file.readline().rstrip()
                if (i % 6) == 0:
                    total_salary = total_salary + float(temp[9:])
            file.close()
            file = open(self.username+".txt", "a")
            file.write("\nOther Expenses:\n")
            file.write("\tPhil Health less(1%): " + "%1.2f"%(total_salary * 0.01) + "\n")
            file.write("\tPagibig less(2.2%): " + "%1.2f"%(total_salary * 0.022) + "\n")
            file.write("\tTotal less: " + "%1.2f"%((total_salary * 0.01) + (total_salary * 0.022)) + "\n\n")
            file.write("Total Salary: " + "%1.2f"%(total_salary - ((total_salary * 0.01) + (total_salary * 0.022))))
            file.close()

    def generateSalary(self):
        file = open("list_of_employee.txt", "r")
        user = file.readline().rstrip()
        passw = file.readline().rstrip()
        recordUp = ""
        if user != self.username and passw != self.password:
            while user != self.username and passw != self.password:
                recordUp = recordUp + user + "\n"
                recordUp = recordUp + passw + "\n"
                recordUp = recordUp + file.readline()
                recordUp = recordUp + file.readline()
                user = file.readline().rstrip()
                passw = file.readline().rstrip()
            employee_record = ""
            employee_record = employee_record + user + "\n"
            employee_record = employee_record + passw + "\n"
            employee_record = employee_record + file.readline().rstrip() + "/" + str("%1.2f"%self.salary) + "\n"
            employee_record = employee_record + file.readline()
        else:
            employee_record = ""
            employee_record = employee_record + user + "\n"
            employee_record = employee_record + passw + "\n"
            employee_record = employee_record + file.readline().rstrip() + "/" + str("%1.2f"%self.salary) + "\n"  
            employee_record = employee_record + file.readline()
        user = file.readline().rstrip()
        recordDown = ""
        while user != "":
            recordDown = recordDown + user + "\n"
            recordDown = recordDown + file.readline()
            recordDown = recordDown + file.readline()
            recordDown = recordDown + file.readline()
            user = file.readline().rstrip() 
        file.close()
        file = open("list_of_employee.txt", "w")
        file.write(recordUp + employee_record + recordDown)
        file.close()
