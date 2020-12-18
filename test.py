import unittest
from room_to_grow import Plant, User

class UserTests(unittest.TestCase):
  def setUp(self):
    self.new_user = User("philton", "Paris Hilton", "Los Angeles")
  
  def test_create_plant(self):
    self.new_user.create_plant("Mr. Plant", "tropical")
    self.assertIsInstance(self.new_user.Plants[0], Plant)
    self.assertTrue(self.new_user.Plants[0].name == "Mr. Plant")

  def test_weather_effect(self):
    testDict = self.new_user.weather_effect(97201)
    self.assertIsInstance(self.new_user.weather_effect(97201), dict)
    self.assertIsNotNone(testDict["Temperature"])
    self.assertIsNotNone(testDict["Sky"])
    self.assertIsNotNone(testDict["Humidity"])

class PlantTests(unittest.TestCase):
  def setUp(self):
    self.new_plant = Plant("Planty", "tropical", "philton")
 
  def test_new_plant_is_equal_to_Plant(self):
    self.assertIsInstance(self.new_plant, Plant)

  def test_water(self):
    self.new_plant.water()
    self.assertEqual(self.new_plant.dryness_level, 0)

  def test_check_dryness(self):
    self.new_plant.check_dryness(3)
    self.assertEqual(self.new_plant.dryness_level, 43)

if __name__ == '__main__':
  unittest.main()