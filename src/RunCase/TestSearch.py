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
        is_in_page = True
        try:
            wait(Template(self.shot_path + self.__page_dict["experience_potion"], record_pos=(0.071, -0.13),
                          resolution=(1280, 720), threshold=0.9), timeout=2)  # 经验值药水
            is_in_page = False
        except:
            pass
        if is_in_page:
            try:
                wait(Template(self.shot_path + self.__page_dict["experience"], record_pos=(0.109, 0.065),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 经验值关卡
            except:
                Page.search_page()
            touch(Template(self.shot_path + self.__page_dict["experience"], record_pos=(0.109, 0.065),
                           resolution=(1280, 720)))  # 经验值关卡
            sleep(2)

    @pytest.fixture
    def mana_page(self):
        is_in_page = True
        try:
            wait(Template(self.shot_path + self.__page_dict["mana_potion"], record_pos=(0.07, -0.127),
                          resolution=(1280, 720), threshold=0.9), timeout=2)  # mana药水
            is_in_page = False
        except:
            pass
        if is_in_page:
            try:
                wait(Template(self.shot_path + self.__page_dict["mana"], record_pos=(0.34, 0.064),
                              resolution=(1280, 720), threshold=0.9), timeout=2)
            except:
                Page.search_page()
            touch(Template(self.shot_path + self.__page_dict["mana"], record_pos=(0.34, 0.064),
                           resolution=(1280, 720)))  # mana关卡
            sleep(2)

    def __start_search(self):
        """使用扫荡券扫荡"""
        touch(Template(self.shot_path + self.__page_dict["use_two_tickets"], record_pos=(0.284, 0.065),
                       resolution=(1280, 720)))  # 使用2张
        sleep(2)
        # 检查是否剩余次数
        has_remain = True
        try:
            CommonButton.blue_comfirm()
        except:
            has_remain = False
        """
        有次数则正常扫荡
        """
        if has_remain:
            # 开始扫荡
            try:
                touch(Template(self.shot_path + self.__page_dict["skip_and_finish"], record_pos=(0.001, 0.216),
                               resolution=(1280, 720)))  # 跳过完毕
            except:
                pass
            # 正常扫荡
            # TODO:增加三种情况，返回探索主页、进入经验值关卡、进入mana关卡
            sleep(1)
        else:
            """
            没有次数则跳过
            """
            CommonButton.cancel()
            sleep(1)
