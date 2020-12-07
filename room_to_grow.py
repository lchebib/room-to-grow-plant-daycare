import requests

class Plant:

  def __init__(self, breed, name, location, dryness_level = 100):
    self.breed = breed
    self.name = name
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
    key = ""

    url = "http://api.weatherapi.com/v1/current.json"
    data = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"key": key,
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
  # input("Enter your Zip Code or the first 3 digits of your Postal Code: ")