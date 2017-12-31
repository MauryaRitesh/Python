from tqdm import tqdm
import requests

chunk_size = 1024

url = 'http://deeplearning.net/tutorial/deeplearning.pdf'
r = requests.get(url, stream = True)

size = int(r.headers['content-length'])
filename = url.split('/')[-1]

with open(filename, 'wb') as f:
    for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),
                     total = size/chunk_size, unit = 'KB'):
        f.write(data)


print("Download complete!")
