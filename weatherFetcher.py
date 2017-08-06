import BeautifulSoup
import requests
import re
import time

session = requests.session()

currentTime = time.strftime("%Y%m%d")
currentTime = currentTime[2:]

record = open('weatherinfo.txt','a')
req = session.get('http://weather.eos.ubc.ca/wxfcst/users/Guest/ubcrs_withicons/index.php?location=3510' + '&date=' + currentTime)

doc = BeautifulSoup.BeautifulSoup(req.content)

time = str(doc.findAll('span'))
temperature = str(doc.findAll('td', {"class" : "value t1" }))
windSpeed = str(doc.findAll('td', {"class" : "value t3" }))
sunRiseSetTime = str(doc.findAll('td', {"class" : "value t4" }))

tempTime = time.split('</span>', 1)
tempTime2 = tempTime[0]
tempTime3 = tempTime2.split('of ', 1)
finalTime = tempTime3[1]


tempTemperature = temperature.split('<td class="value t1">', 4)
tempTemperature2 = tempTemperature[1]
actualTemp = tempTemperature2.split('&#176;',1)[0]
actualTemp = re.sub(r'\s+', '', actualTemp)

tempTemperature3 = tempTemperature[2]
humidity = tempTemperature3.split('%</td>',1)[0]
humidity = re.sub(r'\s+', '', humidity)


tempTemperature4 = tempTemperature[3]
pressure = tempTemperature4.split('kPa',1)[0]
pressure = re.sub(r'\s+', '', pressure)
print(finalTime)
print('temperature: ' + actualTemp)
print('humidity: ' + humidity + '%')
print('pressure: ' + pressure + 'kPa')

record.write('record time: ' + finalTime + '\n')
record.write('temperature: ' + actualTemp + '\n')
record.write('humidity: ' + humidity + '%\n')
record.write('pressure: ' + pressure + 'kPa\n')
record.write('\n')

