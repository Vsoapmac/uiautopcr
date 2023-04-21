from Common.ClientBasic import *


class TestShop(ClientBasic):
    """商店"""
    __page_dict = page_info.shop_dict

    def test_buy_shop_potion(self):
        """购买主商店的所有经验药水,开始:首页,结束:首页"""
        touch(Template(self.shot_path + self.__page_dict["experience_potion_shop"], record_pos=(-0.148, -0.151), resolution=(1280, 720))) # 药剂
        touch(Template(self.shot_path + self.__page_dict["select_all_goods"], record_pos=(0.221, -0.149), resolution=(1280, 720))) # 全部
        touch(Template(self.shot_path + self.__page_dict["chose_all_goods"], record_pos=(0.395, -0.152), resolution=(1280, 720))) # 全选
        touch(Template(self.shot_path + self.__page_dict["buy_batch_goods"], record_pos=(0.279, 0.174), resolution=(1280, 720))) # 批量购入

    @pytest.skip(bool=True)
    def test_buy_shop_upgrate(self):
        """购买主商店的所有升级材料,开始:首页,结束:首页"""
        touch(Template(self.shot_path + self.__page_dict["refine_stone_shop"], record_pos=(0.035, -0.151), resolution=(1280, 720))) # 精炼石

