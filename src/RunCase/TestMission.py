from Common.ClientBasic import *


class TestMission(ClientBasic):
    """任务板块"""

    def test_collect_mission(self):
        """领取任务奖励,开始界面: 主页,结束界面: 主页"""
        touch(Template(r"tpl1681997205852.png", record_pos=(0.378, 0.175), resolution=(1280, 720))) # 全部收取
        touch(Template(r"tpl1681997235138.png", record_pos=(-0.397, -0.248), resolution=(1280, 720))) # 任务标签
