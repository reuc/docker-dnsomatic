import os, time, requests
from datetime import datetime as dt
from pytz import timezone as tz

# log message
def log(level, msg):
    now = dt.now(tz(os.getenv('TZ')))
    datetime = now.strftime('%Y/%m/%d %H:%M:%S.%f')[:-3] + now.strftime('%z')
    print(datetime + '|dnsomatic|' + level + '|' + msg)
    return

# get environment variables
username = os.getenv('DNSOMATIC_USERNAME')
password = os.getenv('DNSOMATIC_PASSWORD')
hostname = os.getenv('DNSOMATIC_HOSTNAME')
delay = int(os.getenv('DNSOMATIC_DELAY'))
interval = int(os.getenv('DNSOMATIC_INTERVAL'))
tries = int(os.getenv('DNSOMATIC_TRIES'))

# delay startup
if delay > 0:
    log('INFO', 'Started with a ' + str(delay) + '-second delay')
    time.sleep(delay)

currentIp = ''
tried = 0
while True:
    try:
        # get your IP address
        req = requests.get('http://myip.dnsomatic.com/')
        if req.status_code == 200:
            newIp = req.text
            if newIp != currentIp:
                if DNSOMATIC_HOSTNAME in os.environ:
                    
                    # update all in DNS-O-Matic account
                    req = requests.get('https://updates.dnsomatic.com/nic/update?hostname=' + hostname + 'myip=' + newIp, auth=(username, password))
                    if req.status_code != 200 or req.text.rsplit()[0] != 'good':
                        raise Exception(req.text)
    
                    log('INFO', ('Current IP ' if currentIp == '' else 'New IP ') + newIp)
                    currentIp = newIp
                else:
                    # update all in DNS-O-Matic account
                    req = requests.get('https://updates.dnsomatic.com/nic/update?myip=' + newIp, auth=(username, password))
                    if req.status_code != 200 or req.text.rsplit()[0] != 'good':
                        raise Exception(req.text)
    
                    log('INFO', ('Current IP ' if currentIp == '' else 'New IP ') + newIp)
                    currentIp = newIp
        else:
            raise Exception(req.text)
    except Exception as e:
        log('ERROR', str(e))

    # check max number of tries
    tried += 1
    if tries > 0 and tried >= tries:
        log('INFO', 'Reached number of ' + str(tries) + ' tries')
        break

    time.sleep(interval)
