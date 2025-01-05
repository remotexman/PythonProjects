import os.path
import pprint
import requests
from PIL import Image
import pandas as pd
import numpy as np


#----------------------------requests---------------------------------------
ip = '5.5.5.5'
r = requests.get(f'http://ip-api.com/json/{ip}').json()
data = {
    'IP:': ip,
    'Country': r['country'],
    'City': r['city'],
    'Org': r['org']
}
pprint.pprint(data)
params = {'key': 'value'}
r_ = requests.post('https://httpbin.org/post', params=params)
r_json = r_.json()
print('POST_URL:' ,r_json['url'])

#-----------------------------PIL---------------------------------------------
img_url = 'https://cdn1.ozone.ru/s3/multimedia-2/6265594538.jpg'
with open('image.png', 'wb') as file:
    file.write(requests.get(img_url).content)
f, e = os.path.splitext('image.png')
output_file = f + '.jpg'
img = Image.open('image.png')
img.thumbnail((100, 150))
img.save('image_thumbnail.jpg')
img_ = Image.open('image.png')
img_ = img_.convert('L')
img_.save(output_file, 'JPEG')

#-------------------------pandas----------------------------------------------
dates = pd.date_range('20250101', periods=5)
df = pd.DataFrame(np.random.randn(5, 4), index= dates, columns=list('ABCD'))

print(df.sort_index(axis=1, ascending=True))
print(df[0:2])
print(df.at[dates[0], 'A'])
print(df.iloc[3:5, 0:2])
print(df.T)

