import unittest
from enviro_calculator.calculator import calculate_carbon_footprint

class TestCalculator(unittest.TestCase):
    def test_calculate_carbon_footprint(self):
        distance = 100  # km
        fuel_efficiency = 10  # km/l
        expected_carbon_footprint = 100 / 10 * 2.31  # 23.1 kg CO2
        result = calculate_carbon_footprint(distance, fuel_efficiency)
        self.assertEqual(result, expected_carbon_footprint)

if __name__ == '__main__':
    unittest.main()
