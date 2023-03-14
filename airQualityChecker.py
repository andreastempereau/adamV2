import requests
from bs4 import BeautifulSoup
import adamMethod as a
	
def getdata(url):
	r=requests.get(url)
	return r.text
def airQuality(a):
    htmldata = getdata("https://weather.com/forecast/air-quality/l/ddf3115ba49669e80b703bb1ac585fe1cb3a19a0dd433428c292f2eb932dc327")
    s = BeautifulSoup(htmldata, 'html.parser')
    data = s.find_all(class_="DonutChart--innerValue--2rO41 AirQuality--pollutantDialText--3Y7DJ")

    res_quality = s.find(class_="DonutChart--innerValue--2rO41 AirQuality--extendedDialText--2AsJa").text

    air_data = s.find_all(class_="DonutChart--innerValue--2rO41 AirQuality--pollutantDialText--3Y7DJ")
    air_data=[data.text for data in air_data]
    if a == 0:
        print("Air Quality :", res_quality)
        print("O3 level :", air_data[0])
        print("NO2 level :", air_data[1])
        print("SO2 level :", air_data[2])
        print("PM2.5 level :", air_data[3])
        print("PM10 level :", air_data[4])
        print("co level :", air_data[5])

    res = int(res_quality)

    if res <= 50:
        remark = "Good"
        impact = "Minimal impact"

    elif res <= 100 and res > 51:
        remark = "Satisfactory"
        impact = "Minor breathing discomfort to sensitive people"

    elif res <= 200 and res >= 101:
        remark = "Moderate"
        impact = "Breathing discomfort to the people with lungs, asthma and heart diseases"

    elif res <= 400 and res >= 201:
        remark = "Very Poor"
        impact = "Breathing discomfort to most people on prolonged exposure"

    elif res <= 500 and res >= 401:
        remark = "Severe"
        impact = "Affects healthy people and seriously impacts those with existing diseases"
    if a == 1:
        print(remark)
        print(impact)

def adamAirQuality(statement):
    if 'level' in statement or 'levels' in statement:
        a.speak(airQuality(0))
    else:
        a.speak(airQuality(1))