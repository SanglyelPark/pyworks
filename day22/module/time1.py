import time

# time.sleep(초) - 대기시간
# time.time() 1970.1.1 자정이후 현재까지의 초로 변환한 시간
# 수행시간 측정하기 - 시작시간, 종료시간

start = time.time()

for i in range(1,11):
    print(i)
    time.sleep(1)

end = time.time()
# print("수행시간 : " + str(end - start) + "초")
print("수행시간 : %.2f초" %(end - start))


# print(time.time())
# print(time.ctime())
#
#
# year = round(time.time() / (365*24*60*60))
# day = round(time.time() / (24*60*60))
# print(year)
# print(day)