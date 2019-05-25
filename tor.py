import sys
import time
import requests
from bs4 import BeautifulSoup
from halo import Halo

# Create the session and set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

s = requests.Session()
s.proxies = proxies

# Terminal Spinner
spinner = Halo(text='Loading', color='green', spinner='hamburger')

try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Verifying the Connections'
    ## Proxy
    r = s.get('https://check.torproject.org/')
    spinner.succeed('It works!')
    spinner.stop()
except requests.ConnectionError as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error - May be Tor is Not Enabled')
    spinner.stop()
    print("OOPS!! Connection Error.")
    ## Normal Request
    p = requests.get('https://check.torproject.org/')
    BS = BeautifulSoup(p.text, "html.parser")
    METATAG = BS.select('h1.off')[0].text.strip()
    print(METATAG)
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
    print(r.url + " - Reading URL")
    BS = BeautifulSoup(r.text, "html.parser")
    METATAG = BS.select('h1.not')[0].text.strip()
    print(METATAG)
