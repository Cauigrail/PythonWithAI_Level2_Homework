import urllib.request
import webbrowser

url = 'https://drive.google.com/file/d/1Pf43IjEkj5KQ-tHOlMPM0u2kvWPb_XiY/view'
response = urllib.request.urlopen(url)
webContent = response.read()

webbrowser.open_new(url)