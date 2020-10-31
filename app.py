import datetime
import requests
import bs4

현재 = str(datetime.datetime.now())
print(현재)
날 = str(현재[:4] + 현재[5:7] + 현재[8:10])

html = requests.get("http://school.cbe.go.kr/cjnamsan-e/M01030901/list?ymd=" + 날)



수프 = bs4.BeautifulSoup(html.text, "html.parser")


트롤 = 수프.find("a", href="/cjnamsan-e/M01030901/list?ymd=" + 날)
결과 = 트롤.find_all("li")
식단 = ""
for i in 결과:
    식단 = 식단 + i.text + "\n"

import telegram
토큰 = "1403160400:AAHHPIqGq71PJOoDWhxVHdp-4VUBi-tmRvA"
봇 = telegram.Bot(token = 토큰)

for i in 봇.getUpdates():
    print(i.message)

봇.sendMessage("1352604698", 식단)

