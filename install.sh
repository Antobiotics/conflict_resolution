#!/bin/bash

(crontab -l && echo "* * * * * python main.py --volume 5") | crontab -
