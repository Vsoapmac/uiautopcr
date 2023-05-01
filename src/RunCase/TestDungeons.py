from Common.ClientBasic import *


class TestDungeons(ClientBasic):
    """地下城"""
    __page_dict = page_info.dungeons_dict

    def test_dungeons(self, green_dragon_page):
        try:
            wait(Template(self.shot_path + self.__page_dict["skip_dungeons_battle"], threshold=0.9, record_pos=(0.001, 0.171), resolution=(1280, 720)), timeout=2)  # 跳过
        except:
            self.logger.info("无法扫荡地下城，可能为三种情况：1、没有次数，请等待次数冷却完毕；2、没有通关，无法进行跳过处理，请先通关地下城；3、程序出现错误，检查程序、模拟器(真机)网络等问题")
        else:
            touch(Template(self.shot_path+self.__page_dict["skip_dungeons_battle"], threshold=0.9, record_pos=(0.001, 0.171), resolution=(1280, 720)))  # 跳过
            try:
                touch(Template(self.shot_path + self.__page_dict["skip_and_finish"], record_pos=(0.001, 0.216),
                               resolution=(1280, 720)))  # 跳过完毕
                self.logger.info("跳过完毕")
            except:
                pass
            sleep(1)
            # 正常扫荡
            self.logger.info("结束扫荡")
            CommonButton.white_comfirm()
            sleep(2)

    @pytest.fixture
    def green_dragon_page(self):
        """绿龙的骇岭"""
        self.logger.info("打开绿龙的骇岭页面")
        try:
            wait(Template(self.shot_path+self.__page_dict["green_dragon_page"], threshold=0.9, record_pos=(0.132, 0.055), resolution=(1280, 720)), timeout=2)  # 绿龙的骸岭
        except:
            self.logger.info("检测到不在地下城页面，开始进入地下城页面")
            Page.dungeons_page()
            self.logger.info("进入地下城页面完毕")
        touch(Template(self.shot_path+self.__page_dict["green_dragon_page"], threshold=0.9, record_pos=(0.132, 0.055), resolution=(1280, 720)))  # 绿龙的骸岭
        self.logger.info("打开绿龙的骇岭页面完毕")

    @pytest.fixture
    def city_of_sky_page(self):
        """天上的浮城"""
        self.logger.info("打开天上的浮城页面")
        try:
            wait(Template(self.shot_path+self.__page_dict["city_of_sky_page"], threshold=0.9, record_pos=(0.374, 0.055), resolution=(1280, 720)), timeout=2)  # 天上的浮城
        except:
            self.logger.info("检测到不在地下城页面，开始进入地下城页面")
            Page.dungeons_page()
            self.logger.info("进入地下城页面完毕")
        touch(Template(self.shot_path+self.__page_dict["city_of_sky_page"], threshold=0.9, record_pos=(0.374, 0.055), resolution=(1280, 720)))  # 天上的浮城
        self.logger.info("打开天上的浮城页面完毕")
