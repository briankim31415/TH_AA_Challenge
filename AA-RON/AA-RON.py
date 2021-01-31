import datetime

class AARON:
    def intro(self):
        return ("Hello, my name is AA-RON and I will be your personal flight bot-tendant today. Feel free to ask me for anything you may need. For a detailed list of what I can help you with, send “Help” in chat. Thank you for choosing American Airlines.");

    def parse_input(self, user_in):
        user_in = user_in.lower()
        if 'help' in user_in:
            return 'help'
        if 'lavatory' in user_in or 'bathroom' in user_in or 'restroom' in user_in:
            return 'lavatory'
        if 'food' in user_in or 'drink' in user_in or 'beverage' in user_in or 'eat' in user_in or 'snack' in user_in:
            return 'food'
        if 'complaint' in user_in:
            return 'complaint'
        if 'attendant' in user_in:
            return 'attendant'
        if 'flight status' in user_in:
            return 'status'
        if 'about me' in user_in:
            return 'about'
        else:
            return "Sorry, didn't quite catch that."

    def help(self):
        return("Things I can help with:\n• Lavatory wait list\n• Food & beverage delivery\n• Complaints\n• Call human attendant\n• Flight stats")

    def lavatory(self):
        lavatory_waitlist = 0; # call to database
        if lavatory_waitlist == 0:
            return("Available ✓\nWould you like to be admitted?")
        elif lavatory_waitlist > 0:
            waitlist_res = lavatory_waitlist + " people waiting in line.\nWould you like to be added to the waiting list?"
            return waitlist_res

    def lavatory_empty_res(self, user_in):
        if user_in.lower() == 'yes':
            return("You may go now.")

    def lavatory_notempty_res(self, user_in):
        if user_in.lower() == 'yes':
            lavatory_waitlist += 1
            waitlist_add_res = "You are " + lavatory_waitlist + get_line_pos(lavatory_waitlist) + " person in line."
            return waitlist_add_res

    def get_line_pos(self, num):
        switcher = {
            1: st,
            2: nd,
            3: rd,
        }
        return switcher.get(num, "th")

    def food_bev(self):
        return("What would you like?")

    def food_bev_res(self):
        return("I will get it sent to you shortly.")

    def complaint(self):
        return("What complaints do you have?")

    def complaint_res(self, user_in):
        if user_in.lower() != 'no':
            return("A human attendant will be notified of your complaint")

    def human_attendant(self):
        return("A human attendant will be with you shortly.")

    def flight_status(self):
        deptime = "2021-01-31T01:00:00.000-06:00"
        arrtime = "2021-01-31T22:30:00.000-05:00"

        T_index = deptime.find('T')

        depyear = int(deptime[0:4])
        depmonth = int(deptime[5:7])
        depday = int(deptime[8:10])
        dephour = int(deptime[T_index+1:T_index+3])
        depmin = int(deptime[T_index+4:T_index+6])
        deptime = datetime.datetime(depyear, depmonth, depday, dephour, depmin)

        arryear = int(arrtime[0:4])
        arrmonth = int(arrtime[5:7])
        arrday = int(arrtime[8:10])
        arrhour = int(arrtime[T_index+1:T_index+3])
        arrmin = int(arrtime[T_index+4:T_index+6])
        arrtime = datetime.datetime(arryear, arrmonth, arrday, arrhour, arrmin)

        curtime = datetime.datetime.now()

        percent = round ((curtime-deptime).total_seconds() / (arrtime-deptime).total_seconds() * 100, 1)

        remtime = str(arrtime-curtime)
        remtime = remtime[0:remtime.find(":",4,6)]

        status_res = "You are " + str(percent) + "% of the way there. " + remtime + " left in the flight."
        return status_res

    def about_me(self):
        return("My name is AA-RON, short for American Airlines-Responsive Online Network. To learn more about my namesake, watch this video: https://www.youtube.com/watch/Dd7FixvoKBw")

    def finish(self):
        return False