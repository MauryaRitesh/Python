import requests

print ('Starting to Download!')

url = 'http://deeplearning.net/tutorial/deeplearning.pdf'
r = requests.get(url)

filename = url.split('/')[-1]

with open(filename, 'wb') as out_file:
    out_file.write(r.content)

print("Download complete!")
