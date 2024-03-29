# main.py
import utime
from machine import DEEPSLEEP_RESET, reset_cause

from include.secrets import _ssid, _pass
from lib.ota_updater import OTAUpdater
from lib.ntp import rtc_init
from lalita.garuda import Garuda


if machine.reset_cause() != machine.SOFT_RESET:
    rtc_init()
print("Current time", utime.localtime())

GITHUB_REPO = 'https://github.com/desmith/Jayananda_wipy'
ota = OTAUpdater(GITHUB_REPO)
VERSION = ota.get_version(directory='.', version_file_name='.version')

f = open('board.py')
BOARD = f.readline().rstrip('\n')
f.close()


def download_and_install_update_if_available():
    print('checking for updates...')
    ota.download_and_install_update_if_available(_ssid, _pass)


def start():
    print('Hare Krishna')

    carrier = Garuda(board=BOARD, version=VERSION)
    carrier.arise()

    print('going to sleep for a while (but not deep sleep)...')


def boot():
    # check if the device woke from a deep sleep
    # (A software reset does not change the reset cause)
    if reset_cause() == DEEPSLEEP_RESET:
        print('woke from a deep sleep')

    # download_and_install_update_if_available()

    while True:
        start()


boot()
