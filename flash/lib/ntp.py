import gc
import socket
import struct
import time
from machine import RTC
from machine import Timer

gc.enable()
rtc_synced = False

def rtc_init():
    global rtc_synced
    rtc = RTC()
    rtc.ntp_sync('pool.ntp.org', update_period=15)
    print('Waiting for RTC/NTP sync...')

    chrono = Timer.Chrono()
    chrono.start()

    while not rtc.synced():
        # wait for 30 seconds, then give up and try manual NTP sync
        if chrono.read() > 30:
            print('Sync timed out after %s seconds...' % chrono.read())
            rtc.ntp_sync(None)
            break

        time.sleep(1)

    if rtc.synced():
        print('RTC Set from NTP daemon to UTC:', rtc.now())
        rtc_synced = True

    else:
        print('Fetching time from NTP server manually...')
        try:
            NTP_QUERY = bytearray(48)
            NTP_QUERY[0] = 0x1b
            addr = socket.getaddrinfo('pool.ntp.org', 123)[0][-1]
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(3)
            s.sendto(NTP_QUERY, addr)
            msg = s.recv(48)
            s.close()

            # 70 years difference between NTP and Pycom epoch
            val = struct.unpack("!I", msg[40:44])[0] - 2208988800
            tm = time.localtime(val)
            rtc.init(tm)
            rtc_synced = True
            gc.collect()

        except socket.timeout:
            print('Timed out while fetching time from remote server.')

    if not rtc.synced() and rtc_synced:
        print('RTC Set from manual NTP call to UTC:', rtc.now())

    # adjust timezone
    if rtc_synced:
        # UTC-7/MST for testing
        time.timezone(-7*60*60)
        print('RTC adjusted from UTC to local timezone:', time.localtime())

    else:
        print('Unable to set RTC', rtc.now())
        print('Resetting NTP sync to 15 minutes')
        rtc.ntp_sync('pool.ntp.org', 60*15)
