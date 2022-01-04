
import datetime
nowdate = datetime.date.today()
deadline = input("When is your deadline? (mm/dd/yyyy) ")
deadline = datetime.datetime.strptime(deadline, "%m/%d/%Y").date()
diff = deadline - nowdate
weeks = diff.days / 7
weeks = "{0:.2f}" .format(weeks)
print("Number of days left is", diff)
print("The number of days left till deadline is", diff.days ,"days")
print("And the number of weeks left till deadline is", weeks ,"weeks")