import requests 
from API import APIkey

class User:
  Plants = []
  
  def __init__(self, username, name, location):
    self.username = username
    self.name = name
    self.location = location
  
  def __repr__(self):
    return f"Welcome, {self.name}. Here are your plants: {self.Plants}"

  def create_plant(self,plant_name,plant_breed):
    new_plant = Plant(plant_name, plant_breed, self.username)
    self.Plants.append(new_plant)

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

class Plant:
  
  def __init__(self, name, breed, owner, dryness_level = 100):
    self.name = name
    self.breed = breed
    self.owner = owner
    self.dryness_level = dryness_level
  
  def __repr__(self):
    return f"Name: {self.name}, Breed: {self.breed}, Owner: {self.owner}"    

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

  # def when_to_water(self):
  #   pass

  