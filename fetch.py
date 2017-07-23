import requests
import sys

response = requests.get(sys.argv[1]) # punch in your commandline url here

with open("html_string.txt", 'w') as f: # write out to file
    f.write(response.text)
