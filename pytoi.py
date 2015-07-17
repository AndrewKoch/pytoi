import argparse
import logging
import sys


def s_to_i(x):
    logger = logging.getLogger()
    logger.info("Received %s, is type %s", x, type(x))

    try:
        if isinstance(x, int):
            return x
        else:
            split_num = []
            for l in x:
                split_num.append(ord(l) - 48)

            base = 1
            new_num = 0
            for i in xrange(len(split_num)):
                new_num += (split_num.pop() * base)
                base *= 10
            return new_num
    except TypeError:
        print "Could not convert data to an integer"
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def main(args):
    log_fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s"

    if args.debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format=log_fmt)

    s_to_i(args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("num")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
