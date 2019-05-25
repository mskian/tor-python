import sys
import time
import requests
from halo import Halo

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

# Terminal Spinner
spinner = Halo(text='Loading', color='green', spinner='hamburger')

# Make a request through the Tor connection
try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Verifying the Connections'
    ## Proxy
    r = s.get('https://api.ipify.org/')
    ## Normal Request
    p = requests.get('https://api.ipify.org/')
    spinner.succeed('It works!')
    spinner.stop()
except requests.ConnectionError as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error')
    spinner.stop()
    print("OOPS!! Connection Error - May be Tor is Not Enabled")
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'Wrong URL or Empty Field'
    time.sleep(2)
    spinner.fail('Wrong URL or Empty Field')
    spinner.stop()
    print("OOPS!! General Error")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("Ok ok, quitting")
    sys.exit(1)
else:
    print('IP Given by TOR')
    print(r.text)
    print('Your Public IP')
    print(p.text)
