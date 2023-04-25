from Common.ClientBasic import *


class TestDepartment(ClientBasic):
    """宿舍"""
    __page_dict = page_info.department_dict

    def test_collect_deparment_strength(self, department_page):
        """收取工会之家的体力,开始:主页,结束:公会之家"""
        self.logger.info("收取工会之家的全部体力和其他物品")
        touch(Template(self.shot_path + self.__page_dict["collect_all_deparment_strength"], record_pos=(0.437, 0.162), resolution=(1280, 720))) # 全部收取
        try:
            wait(Template(self.shot_path+page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720)),timeout=3) # 关闭
            touch(Template(self.shot_path+page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720))) # 关闭
            self.logger.info("收集完毕")
            sleep(1)
        except:
            self.logger.info("没有物品，无需收集")

    @pytest.fixture
    def department_page(self):
        """工会之家"""
        self.logger.info("开始进入工会之家页面")
        Page.department_page()
        self.logger.info("进入工会之家页面完毕")
