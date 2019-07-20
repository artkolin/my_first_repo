import unittest
from parameterized import parameterized
from src.dna_check import (
   hamming_metric, dna_check_results, FIRST_MSG, SEC_MSG, ERROR_MSG, )


class DnaTestCase(unittest.TestCase):

   def test_01_hamming_metric(self):
       self.assertEqual(hamming_metric('CGTA', 'CGTC'), 1)
       self.assertEqual(hamming_metric('G', 'C' ), 1)
       self.assertEqual(hamming_metric('GCTA', 'GCTA' ), 0)
       self.assertEqual(hamming_metric('GGAC', 'GGGG' ), 2)


   def test_dna_check_results(self):
       #Test dna check results
       self.assertEqual(dna_check_results('CGTA', 'GTTA', 'CCTA'), FIRST_MSG)

   @parameterized.expand([
       ['foo', hamming_metric('CGTA', 'CGTC'), 1],
       ['bar', hamming_metric('G', 'C'), 1],
       ['fizz', dna_check_results('CGTA', 'GTTA', 'CCTA'), FIRST_MSG],
   ])
   def test_foo(self, name, a, b):
       self.assertEqual(a, b)