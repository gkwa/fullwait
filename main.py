import re

import bs4
import requests

url = "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html"
pat = re.compile(
    r"https://efa-installer.amazonaws.com/aws-efa-installer-(?P<version>[\.\d]+).tar.gz"
)

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

mo = pat.search(text)
version = None
if mo:
    version = mo.group("version")

print(version)
