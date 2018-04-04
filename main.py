import sys
import argparse
import logging

import soco

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('conflict resolution')


DISCOVERED = soco.discover()


def set_volume(args):
    for zone in DISCOVERED:
        zone.volume = args.volume
        logger.info("%s's volume set to: %s" % (zone.player_name, args.volume))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--volume', default=5, help='sonos volume')
    args = parser.parse_args()
    logger.info("Yes, open offices sucks")
    set_volume(args)
