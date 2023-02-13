import requests as req

city = 'Moscow,RU'
appid = '7f974c0ae95d64daf72fb23619d6e5ee'

res = req.get('http://api.openweathermap.org/data/2.5/weather',
              params = {'q': city, 'units':'metric','lang':'ru','APPID':appid})
data = res.json()

print('City',city)
print('Weather', data['weather'][0]['description'])
print('Temperature', data['main']['temp'])
print('Minimal temp', data['main']['temp_min'])
print('Maximum temp', data['main']['temp_max'])
print('Visibility', data['visibility'])
print('Wind Speed', data['wind']['speed'])
res = req.get('http://api.openweathermap.org/data/2.5/forecast',
              params = {'q': city, 'units':'metric','lang':'ru','APPID':appid})
data = res.json()
print('forecast')
for i in data['list']:
    print(f'''Date <{i['dt_txt']}> \r\nTemperature <{i['main']['temp']:3.0f}> \r\nWeather description <{i['weather'][0]['description']}> \r\nWind speed <{i['wind']['speed']}> \r\nVisibility {i['visibility']} ''')
    print('___________________________-')