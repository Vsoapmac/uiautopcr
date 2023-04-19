from Common.ClientBasic import *


class TestSearch(ClientBasic):
    """探索"""
    __page_dict = page_info.search_dict

    def test_experience_level_11(self, experience_page):
        """经验值关卡11级,开始:冒险,结束:冒险"""
        touch([0.7 * self.w, 0.287 * self.h])  # 确保永远都是第一个
        sleep(2)
        self.__start_search()

    def test_mana_level_11(self, mana_page):
        """玛娜关卡11级,开始:冒险,结束:冒险"""
        touch([0.7 * self.w, 0.287 * self.h])  # 确保永远都是第一个
        sleep(2)
        self.__start_search()

    @pytest.fixture
    def experience_page(self):
        """经验值关卡"""
        touch(Template(r"experience_potion.png", record_pos=(0.071, -0.13), resolution=(1280, 720))) # 经验值药水

        try:
            wait(Template(self.shot_path + self.__page_dict["experience"], record_pos=(0.109, 0.065),
                           resolution=(1280, 720)), timeout=2)
        except:
            Page.search_page()
        touch(Template(self.shot_path + self.__page_dict["experience"], record_pos=(0.109, 0.065),
                           resolution=(1280, 720)))  # 经验值关卡
        sleep(2)

    @pytest.fixture
    def mana_page(self):
        touch(Template(r"mana_potion.png", record_pos=(0.07, -0.127), resolution=(1280, 720))) # mana药水

        try:
            wait(Template(self.shot_path + self.__page_dict["mana"], record_pos=(0.34, 0.064),
                       resolution=(1280, 720)), timeout=2)
        except:
            Page.search_page()
        touch(Template(self.shot_path + self.__page_dict["mana"], record_pos=(0.34, 0.064),
                       resolution=(1280, 720)))  # mana关卡
        sleep(2)

    def __start_search(self):
        """使用扫荡券扫荡"""
        touch(Template(r"use_two_tickets.png", record_pos=(0.284, 0.065), resolution=(1280, 720))) # 使用2张
        sleep(2)