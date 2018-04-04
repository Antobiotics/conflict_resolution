import sys
import argparse
import logging

import soco

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger('conflict resolution')

NORAH_JONES = "https://open.spotify.com/track/6ybViy2qrO9sIi41EgRJgx?si=BOMAiqYwSUyKxN0WTbKP8g"

DISCOVERED = soco.discover()


def set_volume(args):
    for zone in DISCOVERED:
        zone.volume = args.volume
        logger.info("%s's volume set to: %s" % (zone.player_name, args.volume))

 def check_volume():
 	for zone in DISCOVERED:
 		if zone.volume > 50:
 			zone.play_uri(NORAH_JONES)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--volume', default=5, help='sonos volume')
    args = parser.parse_args()
    logger.info("Yes, open offices sucks")
    check_volume()
    set_volume(args)
