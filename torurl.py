import sys
import time
import requests
import cloudscraper
from halo import Halo

# set the proxies.
proxies = {'http': 'socks5://127.0.0.1:9050',
           'https': 'socks5://127.0.0.1:9050'}

# Start Scraper
scraper = cloudscraper.create_scraper()
# Proxy Connection
scraper.proxies = proxies
# Terminal Spinner
spinner = Halo(text='Fetching...', color='cyan')

try:
    LINK = input('Enter a URL: ')
    spinner.start()
    time.sleep(5)
    spinner.text = 'Reading the Given URL...'
    response = scraper.get(LINK)
    time.sleep(5)
    spinner.stop()
except requests.URLRequired as e:
    spinner.start()
    time.sleep(2)
    spinner.color = 'red'
    spinner.text = 'URL Error - Empty URL or Wrong URL'
    time.sleep(2)
    spinner.fail('URL Validation Error')
    spinner.stop()
    print("OOPS!! Connection Error - May be the URL is Not Valid or Can't Bypass them")
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
    if response.history:
        print("URL was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
        print("Final destination:")
        print(response.status_code, response.url)
        break
    else:
        print(response.status_code, response.url + " - Current Live and Active URL")
