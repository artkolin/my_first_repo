import unittest

from src.dna_check import (hamming_metric, dna_check_results, FIRST_MSG, SEC_MSG, ERROR_MSG)



class DnaTestCase(unittest.TestCase):
    def test_01_dna_check(self):
        self.assertEqual(hamming_metric('CGTA', 'CGTC'), 1)
        self.assertEqual(hamming_metric('G', 'C'), 1)
        self.assertEqual(hamming_metric('CGTA', 'CGTA'), 0)
        self.assertEqual(hamming_metric('GGAC', 'GGGG'), 2)

    def test_02_dna_check_result(self):
        self.assertEqual(dna_check_results('CGTA', 'GTTA', 'CCTA'), FIRST_MSG)
