"""
Napisz test do kodu zawartego w src/rna.py
"""

import unittest
from src.rna import transcribe_rna, validate_dna

class RnaTestCase(unittest.TestCase):
    def test_01_transcribe_rna(self):
        self.assertEqual(transcribe_rna('GCTA'), 'CGAU')
        self.assertEqual(transcribe_rna('G'), 'C')
        self.assertEqual(transcribe_rna('GCTAAAAT'), 'CGAUUUUA')
        with self.assertRaises(KeyError):
            transcribe_rna('x')

    def test_02_validate_dna(self):
        self.assertTrue(validate_dna('GCTA'))
        self.assertFalse(validate_dna('X'))