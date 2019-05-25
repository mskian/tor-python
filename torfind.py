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

try:
    ## User input
    LINK = input('Enter a URL: ')
    spinner.start()
    time.sleep(2)
    spinner.text = 'Reading the Output'
    r = s.get(LINK)
    spinner.succeed('Successfully Fetched the URL')
    spinner.stop()
except requests.ConnectionError as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error')
    spinner.stop()
    print("OOPS!! Connection Error - May be Tor is Not Enabled or Can't Bypass them")
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
    print("OOPS!! General Error (Enter a Valid URL) - Add HTTP/HTTPS infront of the URL")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("Ok ok, quitting")
    sys.exit(1)
else:
    print(r.url + " - is an Current Live and Active URL")
