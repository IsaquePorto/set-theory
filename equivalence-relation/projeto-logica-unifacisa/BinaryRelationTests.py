import unittest

from BinaryRelationUtils import BinaryRelationUtils
from SameFirstLetterBinaryRelation import SameFirstLetterBinaryRelation
from SameParityBinaryRelation import SameParityBinaryRelation
from GreaterThanBinaryRelation import GreaterThanBinaryRelation


class BinaryRelationTest(unittest.TestCase):

    def setUp(self):
        self.integers_set = set(range(100))
        self.names_set = {"Ananias", "Alice", "Allef", "Anderson", "Andre", "Barbara", "Bernardo", "Bob", "Bruno",
                          "Charles", "Carlos", "Camila", "Renata", "Rodolfo", "Zeus"}
        self.utils = BinaryRelationUtils()
        self.parity_relation = SameParityBinaryRelation()
        self.first_letter_relation = SameFirstLetterBinaryRelation()
        self.greater_than_relation = GreaterThanBinaryRelation()

    def testReflexivityVerification(self):
        self.assertTrue(self.utils.verify_reflexivity(
            self.parity_relation, self.integers_set))
        self.assertTrue(self.utils.verify_reflexivity(
            self.first_letter_relation, self.names_set))
        self.assertFalse(self.utils.verify_reflexivity(
            self.greater_than_relation, self.integers_set))

    def testSymmetryVerification(self):
        self.assertTrue(self.utils.verify_symmetry(
            self.parity_relation, self.integers_set))
        self.assertTrue(self.utils.verify_symmetry(
            self.first_letter_relation, self.names_set))
        self.assertFalse(self.utils.verify_symmetry(
            self.greater_than_relation, self.integers_set))

    def testTransitivityVerification(self):
        self.assertTrue(self.utils.verify_transitivity(
            self.parity_relation, self.integers_set))
        self.assertTrue(self.utils.verify_transitivity(
            self.first_letter_relation, self.names_set))
        self.assertTrue(self.utils.verify_transitivity(
            self.greater_than_relation, self.integers_set))

    def testAntiSymmetryVerification(self):
        self.assertFalse(self.utils.verify_antisymmetry(
            self.parity_relation, self.integers_set))
        self.assertFalse(self.utils.verify_antisymmetry(
            self.first_letter_relation, self.names_set))
        self.assertTrue(self.utils.verify_antisymmetry(
            self.greater_than_relation, self.integers_set))

    def testEquivalencyVerification(self):
        self.assertTrue(self.utils.verify_equivalency(
            self.parity_relation, self.integers_set))
        self.assertTrue(self.utils.verify_equivalency(
            self.first_letter_relation, self.names_set))
        self.assertFalse(self.utils.verify_equivalency(
            self.greater_than_relation, self.integers_set))

    def testSamples(self):
        self.assertTrue(self.parity_relation.contains_ordered_pair(100, 500))
        self.assertTrue(self.parity_relation.contains_ordered_pair(101, 501))
        self.assertFalse(self.parity_relation.contains_ordered_pair(100, 501))
        self.assertTrue(
            self.first_letter_relation.contains_ordered_pair("Alice", "Andre"))
        self.assertFalse(
             self.first_letter_relation.contains_ordered_pair("Alice", "Bruno"))
        self.assertTrue(
            self.greater_than_relation.contains_ordered_pair(500, 100))
        self.assertFalse(
            self.greater_than_relation.contains_ordered_pair(100, 500))

    def testPartitioning(self):
        self.assertEqual(len(self.utils.get_partitioning(
            self.parity_relation, self.integers_set)), 2)
        self.assertEqual(len(self.utils.get_partitioning(
            self.first_letter_relation, self.names_set)), 5)
        expected_names_partitioning = [{"Ananias", "Alice", "Allef", "Anderson", "Andre"}, {"Barbara", "Bernardo", "Bob", "Bruno"},
                                       {"Charles", "Carlos", "Camila"}, {"Renata", "Rodolfo"}, {"Zeus"}]
        actual_partitioning = self.utils.get_partitioning(
            self.first_letter_relation, self.names_set)
        for s1 in expected_names_partitioning:
            for s2 in actual_partitioning:
                if len(s1) == len(s2):
                    self.assertSetEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
