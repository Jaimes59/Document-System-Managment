import unittest
from logic.classes.address import Address


class TestAddress(unittest.TestCase):
    address = Address(country='Colombia', department='Antioquia', city='Medellín', post_code='050021',
                      neighborhood='El Poblado', street='Carrera 43A', complement='Centro Comercial Santafé')

    def test_instance(self):
        self.assertIsInstance(self.address, Address, "It's an instance of the Address class!")

    def test_country(self):
        self.assertEqual(self.address.country, 'Colombia')

    def test_department(self):
        self.assertEqual(self.address.department, 'Antioquia')

    def test_city(self):
        self.assertEqual(self.address.city, 'Medellín')

    def test_post_code(self):
        self.assertEqual(self.address.post_code, '050021')

    def test_neighborhood(self):
        self.assertEqual(self.address.neighborhood, 'El Poblado')

    def test_street(self):
        self.assertEqual(self.address.street, 'Carrera 43A')

    def test_complement(self):
        self.assertEqual(self.address.complement, 'Centro Comercial Santafé')


if __name__ == '__main__':
    unittest.main()
