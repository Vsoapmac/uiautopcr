import cv2
from easyocr import Reader

image = cv2.imread("./cache_image.png")
reader = Reader(lang_list=["ch_sim","en"], gpu=True)
result_dict = reader.readtext(image)
print(result_dict)

