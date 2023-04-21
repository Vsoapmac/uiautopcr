from Common.ClientBasic import *


class TestShop(ClientBasic):
    """商店"""
    __page_dict = page_info.shop_dict

    def test_buy_shop_potion(self, shop_page):
        """购买主商店的所有经验药水,开始:首页,结束:首页"""
        # 首先选择全部增加容错
        touch(Template(self.shot_path + self.__page_dict["select_all_goods"], record_pos=(0.221, -0.149), resolution=(1280, 720))) # 全部
        sleep(1)
        touch(Template(self.shot_path + self.__page_dict["experience_potion_shop"], record_pos=(-0.148, -0.151), resolution=(1280, 720), threshold=0.9)) # 药剂
        sleep(1)
        touch(Template(self.shot_path + self.__page_dict["chose_all_goods"], record_pos=(0.395, -0.152), resolution=(1280, 720))) # 全选
        sleep(1)
        self.__buy_batch_goods()

    def test_buy_shop_upgrate(self, shop_page):
        """购买主商店的所有精炼石,开始:首页,结束:首页"""
        # 首先选择全部增加容错
        touch(Template(self.shot_path + self.__page_dict["select_all_goods"], record_pos=(0.221, -0.149), resolution=(1280, 720)))  # 全部
        sleep(1)
        touch(Template(self.shot_path + self.__page_dict["refine_stone_shop"], record_pos=(0.035, -0.151), resolution=(1280, 720), threshold=0.9)) # 精炼石
        sleep(1)
        touch(Template(self.shot_path + self.__page_dict["chose_all_goods"], record_pos=(0.395, -0.152), resolution=(1280, 720)))  # 全选
        sleep(1)
        self.__buy_batch_goods()

    def __buy_batch_goods(self):
        """批量购入"""
        try:
            wait(Template(self.shot_path + self.__page_dict["buy_batch_goods"], record_pos=(0.279, 0.174), resolution=(1280, 720)), timeout=2)  # 批量购入
            touch(Template(self.shot_path + self.__page_dict["buy_batch_goods"], record_pos=(0.279, 0.174), resolution=(1280, 720)))  # 批量购入
            sleep(1)
            CommonButton.blue_comfirm()
            CommonButton.blue_comfirm()
        except:
            pass

    @pytest.fixture
    def shop_page(self):
        """商店"""
        try:
            wait(Template(self.shot_path + self.__page_dict["select_all_goods"], record_pos=(0.221, -0.149), resolution=(1280, 720), threshold=0.9), timeout=2)  # 全部
            wait(Template(self.shot_path + self.__page_dict["chose_all_goods"], record_pos=(0.395, -0.152), resolution=(1280, 720), threshold=0.9), timeout=2)  # 全选
        except:
            Page.shop_page()