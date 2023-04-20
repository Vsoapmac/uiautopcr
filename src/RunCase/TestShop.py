from Common.ClientBasic import *


class TestShop(ClientBasic):
    """商店"""

    def test_buy_shop_potion(self):
        """购买主商店的所有经验药水,开始:首页,结束:首页"""
        touch(Template(r"tpl1682005455115.png", record_pos=(-0.148, -0.151), resolution=(1280, 720))) # 药剂
        touch(Template(r"tpl1682005467781.png", record_pos=(0.221, -0.149), resolution=(1280, 720))) # 全部
        touch(Template(r"tpl1682005495636.png", record_pos=(0.395, -0.152), resolution=(1280, 720))) # 全选
        touch(Template(r"tpl1682005516815.png", record_pos=(0.279, 0.174), resolution=(1280, 720))) # 批量购入

    @pytest.skip(bool=True)
    def test_buy_shop_upgrate(self):
        """购买主商店的所有升级材料,开始:首页,结束:首页"""
        touch(Template(r"tpl1682005434629.png", record_pos=(0.035, -0.151), resolution=(1280, 720))) # 精炼石

