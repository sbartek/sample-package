from unittest import TestCase
from samplePackage.normal_number_generator import NormalNumberGenerator


class TestNormalNumberGenerator(TestCase):

    def setUp(self):
        seed = 42
        self.normal_number_generator = NormalNumberGenerator(seed=seed)

    def test_generate(self):
        self.assertAlmostEqual(self.normal_number_generator.generate(), 0.4967, places=4)
