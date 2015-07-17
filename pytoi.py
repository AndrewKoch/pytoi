import argparse
import logging


def s_to_i(n):
    logger = logging.getLogger()
    logger.info("Received %s is type %s", n, type(n))
    if isinstance(n, int):
        return n
    else:
        return int(n)


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
    parser.add_argument("--num")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)