#!/bin/sh -e

sudo chmod +x /etc/init.d/celeryd
sudo /etc/init.d/celeryd start
sudo chmod +x /etc/init.d/celerybeat
sudo /etc/init.d/celerybeat start