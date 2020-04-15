### Page 222
## 11-1. City, Country
import unittest
from city_functions import city_functions

class NameTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_country(self):
        city_name = city_functions('santiago', 'chile')
        self.assertEquals(city_name, 'Santiago Chile')
    def test_city_country_population(self):
        city_name_population = city_functions('santiago', 'chile','500000')
        self.assertEquals(city_name_population, 'Santiago Chile 500000')
unittest.main()