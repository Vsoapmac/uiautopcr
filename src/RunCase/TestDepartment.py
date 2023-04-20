from Common.ClientBasic import *


class TestDepartment(ClientBasic):
    """宿舍"""

    def test_collect_deparment_strength(self):
        """收取工会之家的体力,开始:主页,结束:公会之家"""
        touch(Template(r"tpl1682005597629.png", record_pos=(0.437, 0.162), resolution=(1280, 720))) # 全部收取
        touch(Template(r"tpl1682005608816.png", record_pos=(-0.438, -0.141), resolution=(1280, 720))) # 2层
        touch(Template(r"tpl1682005620883.png", record_pos=(-0.438, -0.191), resolution=(1280, 720))) # 3层



