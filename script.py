import os
import sys
import bokeh

import requests

# print (sys.version)
# print (sys.executable)

r = requests.get("https://coreyms.com")
print(r.status_code)
