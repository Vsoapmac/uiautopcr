from Common.ClientBasic import *


class TestGift(ClientBasic):
    """礼物"""
    __page_dict = page_info.gift_dict

    def test_collect_gift(self, gift_page):
        """收集礼物奖励,开始:主页,结束:主页"""
        try:
            wait(Template(self.shot_path + self.__page_dict["cancel_check_with_gift_energy"], record_pos=(-0.124, 0.214), resolution=(1280, 720)), timeout=2) # 取消勾选
            touch(Template(self.shot_path + self.__page_dict["cancel_check_with_gift_energy"], record_pos=(-0.124, 0.214), resolution=(1280, 720))) # 取消勾选
            sleep(1)
            logging.info("取消勾选")
        except:
            pass
        touch(Template(self.shot_path + self.__page_dict["collect_all_mission_reward"], record_pos=(0.341, 0.215), resolution=(1280, 720))) # 全部收取
        try:
            logging.info("全部收集礼物")
            wait(Template(self.shot_path + page_info.common_button_dict["blue_comfirm"], threshold=0.9, record_pos=(0.114, 0.103), resolution=(1280, 720)), timeout=2)  # 蓝色确认按钮
            touch(Template(self.shot_path + page_info.common_button_dict["blue_comfirm"], threshold=0.9, record_pos=(0.114, 0.103), resolution=(1280, 720)))  # 蓝色确认按钮
            CommonButton.white_comfirm()
            logging.info("全部收集礼物完毕")
        except:
            pass
        logging.info("取消页面")
        CommonButton.cancel()

    @pytest.fixture
    def gift_page(self):
        """礼物"""
        logging.info("开始进入礼物页面")
        try:
            wait(Template(self.shot_path + self.__page_dict["cancel_check_with_gift_energy"], record_pos=(-0.124, 0.214),resolution=(1280, 720)), timeout=2)  # 取消勾选
            logging.info("检测到已经在礼物页面，无需进入")
        except:
            Page.gift_page()
            logging.info("进入礼物页面完毕")