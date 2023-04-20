from Common.ClientBasic import *


class TestGift(ClientBasic):
    """礼物"""

    def test_collect_gift(self):
        """收集礼物奖励,开始:主页,结束:主页"""
        touch(Template(r"tpl1681997289265.png", record_pos=(-0.124, 0.214), resolution=(1280, 720))) # 取消勾选
        touch(Template(r"tpl1681997314239.png", record_pos=(0.341, 0.215), resolution=(1280, 720))) # 全部收取


