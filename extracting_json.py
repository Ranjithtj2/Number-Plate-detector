import pandas as pd
import urllib.request
import random
data = pd.read_json('./indian_Number_plates.json', lines=True)
url = data['content']
print(url)
file_url = [i for i in url]
i=0
for url in file_url:
    i=i+1
    location='C:/Users/Owner\Desktop\Car-Number-Plate-Detection-OpenCV-Python-master\json_photos\Car_Image'+str(i)+'.jpeg'
    urllib.request.urlretrieve(url,location)