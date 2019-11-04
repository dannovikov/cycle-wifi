import subprocess
import time
import datetime

def cycleWifi():
    subprocess.call(['networksetup', '-setairportpower', 'en0', 'off'])
    subprocess.call(['networksetup', '-setairportpower', 'en0', 'on'])
    logData()


def testConnection():
    target = '8.8.8.8' 
    response = subprocess.call(['ping', '-c', '1', target])
    if response != 0:
        cycleWifi()


def logData():
    with open('log.txt', 'a') as f:
        f.write('Wi-fi has been cycled at {}\n'.format(datetime.datetime.now()))


while True:
    testConnection()
    time.sleep(5)
