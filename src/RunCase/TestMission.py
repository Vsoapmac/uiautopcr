from Common.ClientBasic import *


class TestMission(ClientBasic):
    """任务板块"""
    __page_dict = page_info.mission_dict

    def test_collect_mission(self, mission_page):
        """领取任务奖励,开始界面: 主页,结束界面: 主页"""
        touch(Template(self.shot_path + self.__page_dict["common_mission"], record_pos=(0.066, -0.255), resolution=(1280, 720))) # 普通
        self.__collect_mission_reward()
        touch(Template(self.shot_path + self.__page_dict["daily_mission"], record_pos=(-0.102, -0.256), resolution=(1280, 720))) # 每日
        self.__collect_mission_reward()
        touch(Template(self.shot_path + self.__page_dict["name_mission"], record_pos=(0.235, -0.256), resolution=(1280, 720))) # 称号
        self.__collect_mission_reward()

    @pytest.fixture
    def mission_page(self):
        """任务"""
        try:
            wait(Template(self.shot_path + self.__page_dict["mission_tag"], record_pos=(-0.397, -0.248), resolution=(1280, 720)),timeout=2)  # 任务标签
        except:
            Page.mission_page()

    def __collect_mission_reward(self):
        """全部收取任务奖励"""
        touch(Template(self.shot_path + self.__page_dict["collect_all_mission_reward"], record_pos=(0.378, 0.175),
                       resolution=(1280, 720)))  # 全部收取
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218),
                         resolution=(1280, 720)), timeout=3)  # 关闭
            touch(Template(self.shot_path + page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218),
                         resolution=(1280, 720)))  # 关闭
        except:
            pass
        sleep(2)