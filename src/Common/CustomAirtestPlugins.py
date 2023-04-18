import os, cv2
from airtest.core.api import *
from airtest.aircv import *
from easyocr import Reader


class CustomAirtestPlugins:
    """自定义airtest插件"""

    @classmethod
    def scanImageText(cls, image_path, lang_list=['ch_sim', 'en'], gpu=True):
        """
        扫描图片的文本

        :param image_path: 图片路径
        :param lang_list: 识别什么文字，例如简体中文:'ch_sim'；英文:'en'。可以为列表，默认['ch_sim', 'en']
        :param gpu: 是否用gpu识别图像，默认True
        :return: 结果列表
        """
        image = cv2.imread(image_path)
        reader = Reader(lang_list=lang_list, gpu=gpu)
        result_list = reader.readtext(image)
        return result_list

    @classmethod
    def scanCoordsByText(cls, text: str, delete_cache_image=True, cache_image_path="./cache_image.png",
                         lang_list=['ch_sim', 'en'],
                         gpu=True):
        """
        通过airtest截图，然后根据文字扫描该文字在画面中的位置
        
        :param text: 目标文字
        :param delete_cache_image: 是否删除缓存图片，默认True
        :param cache_image_path: airtest截图的缓存文件路径，默认"./cache_image.png"
        :param lang_list: 识别什么文字，例如简体中文:'ch_sim'；英文:'en'。可以为列表，默认['ch_sim', 'en']
        :param gpu: 是否用gpu识别图像，默认True
        :return: 坐标列表，如果没有为None
        """
        # 使用Airtest的image方法获取文字图像
        snapshot(cache_image_path)
        result_list = cls.scanImageText(image_path=cache_image_path, lang_list=lang_list, gpu=gpu)
        # 获取匹配结果的坐标
        for result in result_list:
            if text in result[1]:
                coords = result[0]
        # 删除缓存图片
        if delete_cache_image:
            os.remove(cache_image_path)
        if coords != None:
            # 返回结果
            return coords
        elif coords == None:
            raise Exception("无法识别并点击文字元素")

    @classmethod
    def touchByText(cls, text: str, offset_x=10, offset_y=10, delete_cache_image=True,
                    lang_list=['ch_sim', 'en'],
                    gpu=True):
        """
        通过文字点击元素

        :param text: 目标文字
        :param offset_x: 偏移量坐标x
        :param offset_y: 偏移量坐标y
        :param delete_cache_image: 是否删除缓存图片，默认True
        :param cache_image_path: airtest截图的缓存文件路径，默认"./cache_image.png"
        :param lang_list: 识别什么文字，例如简体中文:'ch_sim'；英文:'en'。可以为列表，默认['ch_sim', 'en']
        :param gpu: 是否用gpu识别图像，默认True
        """
        coords = cls.scanCoordsByText(text=text, delete_cache_image=delete_cache_image, lang_list=lang_list, gpu=gpu)
        x, y = coords[0]
        touch((x + offset_x, y + offset_y))

    @classmethod
    def scanTextsByCoord(cls, device, x1, y1, x2, y2, type=0, delete_cache_image=True,
                         cache_image_path="./cache_image.png",
                         lang_list=['ch_sim', 'en'], gpu=True):
        """
        通过airtest截整个画面，然后根据坐标裁剪画面并分析画面中的文本

        :param device: airtest连接的device
        :param x1: 裁剪框左上角x坐标
        :param y1: 裁剪框左上角y坐标
        :param x2: 裁剪框右下角x坐标
        :param y2: 裁剪框右下角y坐标
        :param type: 坐标类型，0为相对坐标，例如:(0.5, 0.5)；1为绝对坐标，例如:(920, 1080)，默认0
        :param delete_cache_image: 是否删除缓存图片，默认True
        :param cache_image_path: airtest截图的缓存文件路径，默认"./cache_image.png"
        :param lang_list: 识别什么文字，例如简体中文:'ch_sim'；英文:'en'。可以为列表，默认['ch_sim', 'en']
        :param gpu: 是否用gpu识别图像，默认True
        :return: 分析后的文字列表
        """
        # 使用Airtest的image方法获取文字图像
        snapshot(cache_image_path)
        # 读取图片
        img = cv2.imread(cache_image_path)
        # 裁剪图片
        if type == 0:
            # 相对坐标
            w, h = device.get_current_resolution()
            cropped = img[int(y1 * h):int(y2 * h), int(x1 * w):int(x2 * w)]
        else:
            cropped = img[y1:y2, x1:x2]
        # 保存结果
        cv2.imwrite(cache_image_path, cropped)
        # 识别文字
        result_list = cls.scanImageText(image_path=cache_image_path, lang_list=lang_list, gpu=gpu)
        # 保存扫描结果
        text_list = []
        for result in result_list:
            text_list.append(result[1])
        # 删除缓存图片
        if delete_cache_image:
            os.remove(cache_image_path)
        return text_list

    @classmethod
    def hasText(cls, text, device, x1, y1, x2, y2, type=0):
        """
        在特定裁剪框的画面中是否有目标文字
        
        :param text: 目标文字
        :param device: airtest连接的device
        :param x1: 裁剪框左上角x坐标
        :param y1: 裁剪框左上角y坐标
        :param x2: 裁剪框右下角x坐标
        :param y2: 裁剪框右下角y坐标
        :param type: 坐标类型，0为相对坐标，例如:(0.5, 0.5)；1为绝对坐标，例如:(920, 1080)，默认0
        :return: 目标文字是否在特定裁剪框的画面中
        """
        scan_list = cls.scanTextsByCoord(device, x1, y1, x2, y2, type)
        if len(scan_list) == 0:
            return False
        for scan_text in scan_list:
            if text in scan_text:
                return True
        return False

    @classmethod
    def mathInImageLimit(cls, image_path, x1, y1, x2, y2):
        """
        局部匹配图片

        :param image_path: 目标匹配图片路径
        :param x1: 限定区域左上角x坐标
        :param y1: 限定区域左上角y坐标
        :param x2: 限定区域右下角x坐标
        :param y2: 限定区域右下角y坐标
        :return: 该图片在设备窗口的位置
        """
        screen = G.DEVICE.snapshot()
        # 局部截图
        local_screen = aircv.crop_image(screen, (x1, y1, x2, y2))

        # 将我们的目标截图设置为一个Template对象
        tempalte = Template(image_path)
        # 在局部截图里面查找指定的图片对象
        pos = tempalte.match_in(local_screen)
        return pos