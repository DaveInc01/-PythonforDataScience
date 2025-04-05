import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(img: any, newWidth: int, newHeight:int) -> list:
   origWidth, orgiHeight = img.size
   startX = (origWidth - newWidth) / 2
   startY = (orgiHeight - newHeight) / 2
   area = ( startX, startY, startX + newWidth, startY + newHeight )
   # crop_image = img.crop(area)

   crop_image = img.crop(area).resize((400,  400)).convert("L")
   crop_image =  np.array(crop_image).reshape(400,400,1)
   print(f"New shape after slicing: {crop_image.shape} or ({crop_image.shape[0]}, {crop_image.shape[1]})")
   print(crop_image)
   plt.imshow(crop_image, cmap='gray')
   plt.show()
   return crop_image