"""Testing for random_password.py"""

import unittest

from backend.random_password import passwordFullyRandom

class PasswordTest(unittest.TestCase):
	"""Test paddwordFullyRandom method"""

	# pylint: disable=invalid-name
	def assertCharacterCounts(self, string, letters, digits, specials):
		"""Assert that the counts in a character are as expected"""
		counts = [letters, digits, specials]
		for char in string:
			index = 0 if char.isalpha() else 1 if char.isdigit() else 2
			counts[index] -= 1

		self.assertEqual(counts, [0, 0, 0], f'Invalid character counts returned: {letters - counts[0]}L {digits - counts[1]}D {specials - counts[2]}S != {letters}L {digits}D {specials}S')

	def test_character_counts(self):
		"""Desired count of each character is generated"""
		self.assertCharacterCounts(passwordFullyRandom(9, 3, 3), 3, 3, 3)
		self.assertCharacterCounts(passwordFullyRandom(10, 0, 0), 10, 0, 0)
		self.assertCharacterCounts(passwordFullyRandom(10, 5, 0), 5, 5, 0)
		self.assertCharacterCounts(passwordFullyRandom(10, 0, 5), 5, 0, 5)

	def test_base_length(self):
		"""Password is desired length"""
		self.assertEqual(len(passwordFullyRandom(10, 0, 0)), 10, 'base length invalid')
		self.assertEqual(len(passwordFullyRandom(0, 0, 0)), 0, 'adds characters when none requested')
		self.assertEqual(len(passwordFullyRandom(15, 5, 5)), 15, 'other characters are added instead of replacing')
		self.assertEqual(len(passwordFullyRandom(15, 10, 10)), 20, 'extra characters not added')

	def test_random_length(self):
		"""Random length is random"""
		# Run 100 tests and get average length
		passwords = [passwordFullyRandom('random', 0, 0) for _ in range(100)]
		average = sum(len(password) for password in passwords) / len(passwords)

		self.assertTrue(12 < average < 14, 'average is not within 12 and 14: ' + str(average))

if __name__ == '__main__':
	unittest.main()
