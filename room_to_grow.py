import requests 
from API import APIkey

class Plant:

  def __init__(self, name, breed, location, dryness_level = 100):
    self.name = name
    self.breed = breed
    self.location = location
    self.dryness_level = dryness_level
    
  def water(self):
    self.dryness_level = 0
    return self

  def check_dryness(self, last_watered):
  # maximum is the amount of days it takes for dryness level to return to 100
    if self.breed in ('tropical', 'bamboo'):
      maximum = 7
    elif self.breed == 'succulent':
      maximum = 14
    elif self.breed == 'ivy':
      maximum = 4
    self.dryness_level = round((last_watered / maximum) * 100)
    return self.dryness_level

  def weather_effect(self, zip):

    url = "http://api.weatherapi.com/v1/current.json"
    data = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"key": APIkey,
        "q": zip}
        ).json()
    results = data['current']
    temp = results['temp_c']
    sky = results["condition"]["text"]
    humidity = results["humidity"]
    weather = {"Temperature": temp, "Sky": sky, "Humidity": humidity}
    return weather


  # def when_to_water(self):
  #   pass

  # frontend to store zip = input("Enter your Zip Code or the first 3 digits of your Postal Code: ")

  