import urllib
import json
import webbrowser
from IPython.display import Image

url = 'https://api.nasa.gov/planetary/apod?api_key=FdSrIRAIChs4hnbySHRX3lhLTQrmpUxncapC9ulz&date=2017-07-08'

urlobj = urllib.urlopen(url)
apodread = urlobj.read()
data = json.loads(apodread.decode('utf-8'))


print(data["title"])

print(data["url"])

Image(data["url"])

from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return data["url"] + '  ' + data["title"]

if __name__ == "__main__":
    app.run()
