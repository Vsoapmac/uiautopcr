import logging, cv2
from airtest.core.api import *
from airtest.aircv import *
from easyocr import Reader

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

d = connect_device("Android:///127.0.0.1:62025")
cache_image_path = "./cache_image.png"
scan_text_type = ['ch_sim', 'en']
type = 0
x1 = 0.5
y1 = 0.5
x2 = 0.72
y2 = 0.95

# 使用Airtest的image方法获取文字图像
snapshot(cache_image_path)
# 读取图片
img = cv2.imread(cache_image_path)
# 裁剪图片
if type == 0:
    # 相对坐标
    w, h = d.get_current_resolution()
    cropped = img[int(y1*h):int(y2*h), int(x1*w):int(x2*w)]
else:
    cropped = img[y1:y2, x1:x2]
# 保存结果
cv2.imwrite(cache_image_path, cropped)
# 使用EasyOCR的Reader对象识别文字并返回结果
reader = Reader(scan_text_type, gpu=True)
result_list = reader.readtext(cache_image_path)
# 保存扫描结果
text_list = []
for result in result_list:
    text_list.append(result[1])
# 删除缓存图片
# os.remove(cache_image_path)
print(text_list)