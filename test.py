import unittest
from room_to_grow import Plant

class PlantTests(unittest.TestCase):
  def setUp(self):
    self.new_plant = Plant("tropical", "Planty", "Portland")
 
  def test_new_plant_is_equal_to_Plant(self):
    self.assertIsInstance(self.new_plant, Plant)

  def test_water(self):
    self.new_plant.water()
    self.assertEqual(self.new_plant.dryness_level, 0)

  def test_check_dryness(self):
    self.new_plant.check_dryness(3)
    self.assertEqual(self.new_plant.dryness_level, 43)

  def test_weather_effect(self):
    testDict = self.new_plant.weather_effect(97201)
    self.assertIsInstance(self.new_plant.weather_effect(97201), dict)
    self.assertIsNotNone(testDict["Temperature"])
    self.assertIsNotNone(testDict["Sky"])
    self.assertIsNotNone(testDict["Humidity"])

    
  # def test_when_to_water(self):

if __name__ == '__main__':
  unittest.main()