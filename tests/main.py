import unittest

from tests.connection_test import TestConnection


def create_suite():
    # Setup testing suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestConnection)

    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
