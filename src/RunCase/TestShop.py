from Common.ClientBasic import *


class TestShop(ClientBasic):
    """商店"""

    def test_buy_shop_potion(self):
        """购买主商店的所有经验药水,开始:首页,结束:首页"""
        pass

    @pytest.skip(bool=True)
    def test_buy_shop_upgrate(self):
        """购买主商店的所有升级材料,开始:首页,结束:首页"""
        pass
