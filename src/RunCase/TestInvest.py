from Common.CommonButton import CommonButton
from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""

    def test_miracle_survey_level_one(self):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡1级")

    def test_miracle_survey_level_two(self):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡2级")

    def test_miracle_survey_level_three(self):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        CustomAirtestPlugins.touchByText("圣迹调查关卡3级")

    def test_temple_survey_level_one(self):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        CustomAirtestPlugins.touchByText("神殿调查关卡1级")

    def test_temple_survey_level_two(self):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        CustomAirtestPlugins.touchByText("神殿调查关卡2级")
