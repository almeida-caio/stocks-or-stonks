import json
from PIL import Image
from PIL import PngImagePlugin

data = {}

for index in range(0, 1000):
	f = "1-" + str(index) + ".png"
	loaded_image = Image.open(f)
	data[f] = loaded_image.info
	
print(data)

with open('real_stock_metadata.json', 'w') as fp:
    json.dump(data, fp)