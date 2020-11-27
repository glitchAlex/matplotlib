import numpy as np
from PIL import Image
import math

file_path = 'C:\DEV\lunar_images\lunar01_raw.jpg'
new_file_path = 'C:\DEV\lunar_images\lunar01_new.jpg'

# считаем картинку в numpy array
img = Image.open(file_path)
data = np.array(img)
min, max = data.min(), data.max()
sz = data.shape
print(min, max)
print(data.shape)

# ... логика обработки
updated_data = data
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        updated_data[i][j] = math.floor(((data[i][j]-min)/(max-min))*255)
        #updated_data = ((data[i][j]-min)/(max-min))*255

# запись картинки после обработки
res_img = Image.fromarray(updated_data)
res_img.save(new_file_path)