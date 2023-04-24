from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""
    __page_dict = page_info.invest_dict

    def test_miracle_survey_level_one(self, miracle_page):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        logging.info("开始圣迹调查关卡1级")
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_one"], record_pos=(0.252, 0.071),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡1级
        self.__start_invest()
        logging.info("圣迹调查关卡1级调查完毕")

    def test_miracle_survey_level_two(self, miracle_page):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        logging.info("开始圣迹调查关卡2级")
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_two"], record_pos=(0.255, -0.043),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡2级
        self.__start_invest()
        logging.info("圣迹调查关卡2级调查完毕")

    def test_miracle_survey_level_three(self, miracle_page):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        logging.info("开始圣迹调查关卡3级")
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_three"], record_pos=(0.254, -0.159),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡3级
        self.__start_invest()
        logging.info("圣迹调查关卡3级调查完毕")

    def test_temple_survey_level_one(self, temple_page):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        logging.info("开始神殿调查关卡1级")
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_one"], record_pos=(0.26, -0.042),
                       resolution=(1280, 720), threshold=0.9))  # 神殿调查关卡1级
        self.__start_invest()
        logging.info("神殿调查关卡1级调查完毕")

    def test_temple_survey_level_two(self, temple_page):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        logging.info("开始神殿调查关卡2级")
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_two"], record_pos=(0.262, -0.156),
                       resolution=(1280, 720), threshold=0.9))  # 神殿调查关卡2级
        self.__start_invest()
        logging.info("神殿调查关卡2级调查完毕")

    @pytest.fixture
    def miracle_page(self):
        """圣迹调查页面"""
        logging.info("开始进入圣迹调查页面")
        # 首先检测是否在里面了
        is_in_page = True
        try:
            wait(Template(self.shot_path + self.__page_dict["piece_of_heart"], record_pos=(0.075, -0.13), resolution=(1280, 720), threshold=0.9), timeout=2) # 心碎图片
            logging.info("检测到已经在圣迹调查页面，无需进入")
        except:
            is_in_page = False
        # 不在那就直接进去
        if not is_in_page:
            # 做一个稳定性检测，在调查页面里面就直接进去
            try:
                wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 神殿调查
                wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 圣迹调查
            except:
                logging.info("检测到不在调查页面，开始进入调查页面")
                Page.invest_page()  # 否则进入调查页面，再进去
                logging.info("进入调查页面完毕")
            touch(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065),
                           resolution=(1280, 720), threshold=0.9))  # 圣迹调查
            logging.info("进入圣迹调查页面完毕")

    @pytest.fixture
    def temple_page(self):
        """神殿调查页面"""
        logging.info("开始进入神殿调查页面")
        # 首先检测是否在里面了
        is_in_page = True
        try:
            wait(Template(self.shot_path + self.__page_dict["cup_of_stars"], record_pos=(0.08, -0.127), resolution=(1280, 720), threshold=0.9), timeout=2) # 星球杯图片
            logging.info("检测到已经在神殿调查页面，无需进入")
        except:
            is_in_page = False
        # 不在那就直接进去
        if not is_in_page:
            # 做一个稳定性检测，在调查页面里面就直接进去
            try:
                wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065), resolution=(1280, 720), threshold=0.9), timeout=2)  # 圣迹调查
                wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064), resolution=(1280, 720), threshold=0.9), timeout=2)  # 神殿调查
            except:
                logging.info("检测到不在调查页面，开始进入调查页面")
                Page.invest_page()  # 否则进入调查页面，再进去
                logging.info("进入调查页面完毕")
            touch(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064),
                           resolution=(1280, 720), threshold=0.9))  # 神殿调查
            logging.info("进入神殿调查页面完毕")

    def __start_invest(self):
        """使用扫荡券扫荡"""
        logging.info("使用扫荡券扫荡")
        for i in range(4):
            touch(Template(self.shot_path + self.__page_dict["plus"], record_pos=(0.415, 0.062),
                           resolution=(1280, 720)))  # +号
            sleep(1)
        touch(Template(self.shot_path + self.__page_dict["use_five_tickets"], record_pos=(0.285, 0.062),
                       resolution=(1280, 720)))  # 使用5张
        sleep(1)
        # 检查是否剩余次数
        has_remain = True
        try:
            wait(Template(self.shot_path + self.__page_dict["remain_challenge_zero"], record_pos=(-0.004, -0.016),
                          resolution=(1280, 720)),timeout=2)  # 剩余挑战次数为0
            has_remain = False
        except:
            pass
        """
        有次数则正常扫荡
        """
        if has_remain:
            # 开始扫荡
            CommonButton.blue_comfirm()
            try:
                touch(Template(self.shot_path + self.__page_dict["skip_and_finish"], record_pos=(0.001, 0.216),
                               resolution=(1280, 720)))  # 跳过完毕
                logging.info("跳过完毕")
            except:
                pass
            # 正常扫荡
            CommonButton.white_comfirm()
            sleep(1)
            logging.info("检测是否有限定商城开启，若有则处理")
            Page.detect_limit_shop_open()
            logging.info("扫荡结束")
        else:
            """
            没有次数则跳过
            """
            logging.info("没有扫荡次数，取消")
            CommonButton.cancel()
            sleep(1)
        logging.info("取消当前页面")
        CommonButton.cancel()
        sleep(1)
