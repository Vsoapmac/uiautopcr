from Common.ClientBasic import *


class TestPreArana(ClientBasic):
    """竞技场"""

    def test_arana(self):
        """竞技场,开始:冒险,结束:冒险"""
        touch(0.612*elf.w,0.302*self.h) # 点击第一个人
        touch(Template(r"tpl1681996844208.png", record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        touch(Template(r"tpl1681996858374.png", record_pos=(-0.384, 0.164), resolution=(1280, 720))) # 对战覆历
        touch(Template(r"tpl1681996885521.png", record_pos=(-0.231, 0.165), resolution=(1280, 720))) # 防守设定


    def princess_arana(self):
        """公主竞技场,开始:冒险,结束:冒险"""
        touch(0.612*elf.w,0.302*self.h) # 点击第一个人
        touch(Template(r"tpl1681996844208.png", record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        touch(Template(r"tpl1681996951013.png", record_pos=(-0.385, 0.175), resolution=(1280, 720))) # 对战覆历
        touch(Template(r"tpl1681996968893.png", record_pos=(-0.231, 0.175), resolution=(1280, 720))) # 防守设定
        touch(Template(r"tpl1681997031445.png", record_pos=(-0.398, -0.189), resolution=(1280, 720))) # 队伍1
        touch(Template(r"tpl1681996990222.png", record_pos=(-0.152, -0.19), resolution=(1280, 720))) # 队伍3
        touch(Template(r"tpl1681997006519.png", record_pos=(0.373, 0.191), resolution=(1280, 720))) # 战斗开始



