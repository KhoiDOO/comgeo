import unittest
import math
from comgeo.core.shape.ellipse import Ellipse
from comgeo.core.vertex.vertex2d import Vertex2D

class TestEllipse(unittest.TestCase):
	def setUp(self):
		self.center = Vertex2D(0.0, 0.0)
		self.rx = 3.0
		self.ry = 2.0
		self.ellipse = Ellipse(self.center, self.rx, self.ry)

	def test_center_property(self):
		self.assertEqual(self.ellipse.center, self.center)

	def test_rx_property(self):
		self.assertEqual(self.ellipse.rx, self.rx)

	def test_ry_property(self):
		self.assertEqual(self.ellipse.ry, self.ry)

	def test_area(self):
		expected_area = math.pi * self.rx * self.ry
		self.assertAlmostEqual(self.ellipse.area(), expected_area)

	def test_perimeter(self):
		expected_perimeter = 2 * math.pi * math.sqrt((self.rx**2 + self.ry**2) / 2)
		self.assertAlmostEqual(self.ellipse.perimeter(), expected_perimeter)

	def test_repr(self):
		rep = repr(self.ellipse)
		self.assertIn("Ellipse(center=", rep)
		self.assertIn(f"rx={self.rx}", rep)
		self.assertIn(f"ry={self.ry}", rep)

	def test_contains_center(self):
		self.assertTrue(self.ellipse.contains(self.center))

	def test_contains_inside(self):
		point = Vertex2D(1.0, 1.0)
		self.assertTrue(self.ellipse.contains(point))

	def test_contains_outside(self):
		point = Vertex2D(4.0, 0.0)
		self.assertFalse(self.ellipse.contains(point))

	def test_contains_on_boundary(self):
		point = Vertex2D(self.rx, 0.0)
		self.assertTrue(self.ellipse.contains(point))

if __name__ == "__main__":
	unittest.main()
