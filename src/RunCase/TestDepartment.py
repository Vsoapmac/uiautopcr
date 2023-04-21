from Common.ClientBasic import *


class TestDepartment(ClientBasic):
    """宿舍"""
    __page_dict = page_info.shop_dict

    def test_collect_deparment_strength(self):
        """收取工会之家的体力,开始:主页,结束:公会之家"""
        touch(Template(self.shot_path + self.__page_dict["collect_all_deparment_strength"], record_pos=(0.437, 0.162), resolution=(1280, 720))) # 全部收取
        touch(Template(self.shot_path + self.__page_dict["deparment_level_2"], record_pos=(-0.438, -0.141), resolution=(1280, 720))) # 2层
        touch(Template(self.shot_path + self.__page_dict["deparment_level_3"], record_pos=(-0.438, -0.191), resolution=(1280, 720))) # 3层

