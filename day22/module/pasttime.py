import datetime
import calendar as cal


print(" ♣ 지금까지 몇 일? ♣")
day1 = datetime.date(2021,12,10)
print(day1)

today = datetime.date.today()

#지나온 날
passedtime = today - day1
print(passedtime)
print("{}일 지났습니다.". format(passedtime.days))

# 오늘 날짜
the_day = datetime.date(2022,1,1)
print(the_day)

cal.prcal(2021)
cal.prmonth(2022,2)