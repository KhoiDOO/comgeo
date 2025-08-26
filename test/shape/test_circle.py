import unittest
import math
from comgeo.core.shape.circle import Circle
from comgeo.core.vertex.vertex2d import Vertex2D

class TestCircle(unittest.TestCase):
	def setUp(self):
		self.center = Vertex2D(1.0, 2.0)
		self.radius = 5.0
		self.circle = Circle(self.center, self.radius)

	def test_center_property(self):
		self.assertEqual(self.circle.center, self.center)

	def test_radius_property(self):
		self.assertEqual(self.circle.radius, self.radius)

	def test_area(self):
		expected_area = math.pi * self.radius ** 2
		self.assertAlmostEqual(self.circle.area(), expected_area)

	def test_perimeter(self):
		expected_perimeter = 2 * math.pi * self.radius
		self.assertAlmostEqual(self.circle.perimeter(), expected_perimeter)

	def test_repr(self):
		rep = repr(self.circle)
		self.assertIn("Circle(center=", rep)
		self.assertIn(f"radius={self.radius}", rep)

	def test_contains_center(self):
		self.assertTrue(self.circle.contains(self.center))

	def test_contains_inside(self):
		point = Vertex2D(1.0, 6.0)  # distance = 4
		self.assertTrue(self.circle.contains(point))

	def test_contains_outside(self):
		point = Vertex2D(1.0, 8.0)  # distance = 6
		self.assertFalse(self.circle.contains(point))

	def test_contains_on_boundary(self):
		point = Vertex2D(1.0 + self.radius, 2.0)
		self.assertTrue(self.circle.contains(point))

if __name__ == "__main__":
	unittest.main()
