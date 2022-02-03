# 오늘 날짜와 현재 시간

import datetime

now = datetime.datetime.today()
print(now)

# 날짜
print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))

# 시간
print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))


# 오늘 날짜
today = datetime.date.today()
print(today)


#특정한 날찌
the_day = datetime.date(2022,1,1)
print(the_day)
