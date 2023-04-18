from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""

    def test_miracle_survey_level_one(self,miracle_page):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡1级")

    def test_miracle_survey_level_two(self,miracle_page):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡2级")

    def test_miracle_survey_level_three(self,miracle_page):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡3级")

    def test_temple_survey_level_one(self):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        CustomAirtestPlugins.touchByText("神殿调查关卡1级")

    def test_temple_survey_level_two(self):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        CustomAirtestPlugins.touchByText("神殿调查关卡2级")

    @pytest.fixture
    def miracle_page(self):
        x, y = self.d.get_current_resolution()
        has_text = CustomAirtestPlugins.hasText(text="圣迹调查", device=self.d, x1=0, y1=0, x2=x, y2=y, type=1)
        if has_text:
            CustomAirtestPlugins.touchByText("圣迹调查")
        else:
            Page.invest_page()
            sleep(3)
            CustomAirtestPlugins.touchByText("圣迹调查")
