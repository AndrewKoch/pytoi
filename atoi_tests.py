import argparse
import logging
import unittest

import pytoi


class PytoiTests(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()

    def base_cases(self):
        self.logger.info("Testing base cases")
        self.assertEquals(pytoi.s_to_i("5"), 5)
        self.assertEquals(pytoi.s_to_i("10"), 10)

        self.assertEquals(pytoi.s_to_i(5, 5))
        self.assertEquals(pytoi.s_to_i(10, 10))


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)
    logger = logging.getLogger()

    # Turns off logging
    if args.no_log:
        logger.disabled = True

    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(PytoiTests)
    runner.run(itersuite)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set logger level")
    parser.add_argument("--debug", action="store_true",
                        help="Sets logging to debug")
    parser.add_argument("--no_log", action="store_true",
                        help="Turns off all logging")

    args = parser.parse_args()

    main(args)
