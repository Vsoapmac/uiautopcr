from Common.ClientBasic import *


class TestMission(ClientBasic):
    """任务板块"""
    __page_dict = page_info.mission_dict

    def test_collect_mission(self, mission_page):
        """领取任务奖励,开始界面: 主页,结束界面: 主页"""
        touch(Template(self.shot_path + self.__page_dict["collect_all_mission_reward"], record_pos=(0.378, 0.175),
                       resolution=(1280, 720)))  # 全部收取
        # TODO:增加执行逻辑

    @pytest.fixture
    def mission_page(self):
        """任务"""
        try:
            wait(Template(self.shot_path + self.__page_dict["mission_tag"], record_pos=(-0.397, -0.248),
                           resolution=(1280, 720)),timeout=2)  # 任务标签
        except:
            Page.mission_page()
