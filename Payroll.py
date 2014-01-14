class Payroll:
    time_in = "00:00"
    time_out = "00:00"
    time_in_for_ot = "00:00"
    time_out_for_ot = "00:00"
    late_time = "00:00"
    under_time = "00:00"
    over_time = "00:00"
    salary = 0
    is_holiday = bool

    def isHoliday(self, boolean):
        self.is_holiday = boolean

    def setTimeIn(self):
        self.time_in = input("Time in: ")
        
    def setTimeOut(self):
        self.time_out = input("Time out: ")

    def setTimeInForOt(self):
        self.time_in_for_ot = input("Time in: ")

    def setTimeOutForOt(self):
        self.time_out_for_ot = input("Time out: ")

    def setLateTime(self):
        hour = 0
        for i in range(1, len(self.time_in)):
            if self.time_in[i] == ":":
                hour = int(self.time_in[:i])
                break
        minute = int(self.time_in[i+1:])
        if hour > 8 or hour == 8 and minute > 0:
            self.late_time = str(hour-8) + ":" + str(minute)
        else:
            self.late_time = str("00:00")

    def setUnderTime(self):
        hour = 0
        for i in range(1, len(self.time_out)):
            if self.time_out[i] == ":":
                hour = int(self.time_out[:i])
                break
        minute = int(self.time_out[i+1:])
        if hour < 17:
            self.under_time =  str(17 -(hour+1)) + ":" + str(60 - minute)
        else:
            self.under_time =  str("00:00")

    def setOverTime(self):
        hour_in = 0
        for i in range(1, len(self.time_in_for_ot)):
            if self.time_in_for_ot[i] == ":":
                hour_in = int(self.time_in_for_ot[:i])
                break
        minute_in = int(self.time_in_for_ot[i+1:])
        hour_out = 0
        for j in range(1, len(self.time_out_for_ot)):
            if self.time_out_for_ot[j] == ":":
                hour_out = int(self.time_out_for_ot[:j])
                break
        minute_out = int(self.time_out_for_ot[j+1:])
        if hour_out >= 0 and hour_out <= 8 or hour_out == 23:
            if hour_in > 18 or hour_in == 18 and minute_in > 0:
                self.over_time = str(23-(hour_in+1)) + ":" + str(60-minute_out)
            else:
                self.over_time =  str(5) + ":" + str(0)
            return True
        elif hour_out == 24:
            print("There is no 24. I told you the time format is military time, Thats why you must start again\n")
            return False
        elif hour_out < 23 and hour_in >= 18 and hour_in < hour_out:
            if hour_in > 18 or hour_in == 18 and minute_in > 0:
                self.over_time = str(hour_out - (hour_in+1)) + ":" + str((60 - minute_in) + minute_out)
            else:
                self.over_time = str(hour_out - (hour_in+1)) + ":" + str((60 - minute_in) + minute_out)
            return True
        else:
            print("You did not use properly the system.\n")
    
    def getTimeIn(self):
        return self.time_in

    def getTimeOut(self):
        return self.time_out

    def getTimeInForOt(self):
        return self.time_in_for_ot

    def getTimeOutForOt(self):
        return self.time_out_for_ot

    def getUnderTime(self):
        return self.under_time

    def getLateTime(self):
        return self.late_time

    def getOverTime(self):
        return self.over_time

    def getSalary(self):
        hour_for_late_time = 0
        for i in range(1, len(self.late_time)):
            if self.late_time[i] == ":":
                hour_for_late_time = int(self.late_time[:i])
                break
        minute_for_late_time = int(self.late_time[i+1:])
        
        hour_for_under_time = 0
        for i in range(1, len(self.under_time)):
            if self.under_time[i] == ":":
                hour_for_under_time = int(self.under_time[:i])
                break
        minute_for_under_time = int(self.under_time[i+1:])

        if self.over_time != "00:00":
            hour_for_over_time = 0
            for i in range(1, len(self.over_time)):
                if self.over_time[i] == ":":
                    hour_for_over_time = int(self.over_time[:i])
                    break
            minute_for_over_time = int(self.over_time[i+1:])
        else:
            hour_for_over_time = 0
            minute_for_over_time = 0

        if self.is_holiday:
            self.salary = 2 * (500 - (((hour_for_late_time + hour_for_under_time) * 62.5) + \
                     ((minute_for_late_time + minute_for_under_time) * 1.0416667)) + \
                     ((hour_for_over_time) * 62.5) + (minute_for_over_time * 1.0416667))
            return self.salary
        else:
            self.salary = (500 - (((hour_for_late_time + hour_for_under_time) * 62.5) + \
                     ((minute_for_late_time + minute_for_under_time) * 1.0416667)) + \
                     ((hour_for_over_time) * 62.5) + (minute_for_over_time * 1.0416667))
            return self.salary
