from Common.ClientBasic import *


class TestLunaTower(ClientBasic):
    """露娜塔"""
    __page_dict = page_info.plugins_dict

    def test_luna_tower(self):
        """露娜塔通关"""
        wait(Template(self.shot_path + self.__page_dict["pass_level_team"], record_pos=(0.38, -0.175), resolution=(1280, 720), threshold=0.9), timeout=3) # 通关队伍
        touch(Template(self.shot_path + self.__page_dict["pass_level_team"], record_pos=(0.38, -0.175), resolution=(1280, 720), threshold=0.9)) # 通关队伍
        sleep(2)
        wait(Template(self.shot_path + self.__page_dict["use_luna_pass_team"], record_pos=(0.311, -0.138), resolution=(1280, 720)), timeout=3) # 使用（对坐标有严格要求）
        touch(Template(self.shot_path + self.__page_dict["use_luna_pass_team"], record_pos=(0.311, -0.138), resolution=(1280, 720))) # 使用（对坐标有严格要求）
        sleep(1)
        touch(Template(self.shot_path + self.__page_dict["use_luna_pass_team_to_fight"], record_pos=(0.152, 0.106), resolution=(1280, 720), threshold=0.9)) # 在实战中使用
        sleep(2)
        touch(Template(self.shot_path + page_info.common_button_dict["start_battle"], record_pos=(0.373, 0.191), resolution=(1280, 720)))  # 战斗开始
        touch(Template(self.shot_path + page_info.common_button_dict["start_battle"], record_pos=(0.373, 0.191), resolution=(1280, 720)))  # 战斗开始
        wait(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)), timeout=100)  # 下一步
        touch(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)))  # 下一步
