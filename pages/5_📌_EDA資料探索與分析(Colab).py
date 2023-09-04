import urllib.request
import webbrowser

url = 'https://colab.research.google.com/drive/1SpmNMA3Nc2WgK3FU_OZRSmeU3g66suiw'
response = urllib.request.urlopen(url)
webContent = response.read()

webbrowser.open_new(url)