from Common.ClientBasic import *


class TestSearch(ClientBasic):
    """探索"""

    def test_experience_level_11(self):
        """经验值关卡11级,开始:冒险,结束:冒险"""
        touch([0.7*self.w, 0.287*self.h]) # 确保永远都是第一个

    def test_mana_level_11(self):
        """玛娜关卡11级,开始:冒险,结束:冒险"""
        touch([0.7*self.w, 0.287*self.h]) # 确保永远都是第一个
    
    def experience_page(self):
        touch(Template(r"tpl1681834402000.png", record_pos=(0.109, 0.065), resolution=(1280, 720))) # 经验值关卡
    
    def mana_page(self):
        touch(Template(r"tpl1681834418754.png", record_pos=(0.34, 0.064), resolution=(1280, 720))) # mana关卡
