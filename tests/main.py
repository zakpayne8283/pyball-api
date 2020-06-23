import unittest

from tests.connection_test import TestConnection


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestConnection())

    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
