from Common.ClientBasic import *


class TestPassMap(ClientBasic):
    """普通过图"""
    __page_dict = page_info.plugins_dict

    def test_pass_map(self):
        """普通过图"""
        self.logger.info("点击角色，进入地图")
        touch(Template(self.shot_path + self.__page_dict["map_character"], resolution=(1280, 720)))  # 人物角色图
        wait(Template(self.shot_path + self.__page_dict["challenge_map"], threshold=0.9, record_pos=(0.373, 0.19), resolution=(1280, 720)), timeout=10)  # 挑战
        touch(Template(self.shot_path + self.__page_dict["challenge_map"], threshold=0.9, record_pos=(0.373, 0.19), resolution=(1280, 720)))  # 挑战
        sleep(2)
        self.logger.info("开始战斗")
        CommonButton.start_battle() # 战斗开始
        sleep(2)
        self.logger.info("等待战斗完毕")
        wait(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)), timeout=200)  # 下一步
        self.logger.info("战斗完毕")
        touch(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)))  # 下一步
        sleep(2)
        self.logger.info("检测是否开启限定商店，若有则关闭")
        Page.detect_limit_shop_open() # 检测是否开启限定商店
        sleep(2)
        wait(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)), timeout=20)  # 下一步
        self.logger.info("返回上页")
        touch(Template(self.shot_path + self.__page_dict["next_step"], threshold=0.9, record_pos=(0.366, 0.231), resolution=(1280, 720)))  # 下一步
        sleep(5)
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720), threshold=0.9), timeout=5)  # 取消
            touch(Template(self.shot_path + page_info.common_button_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720), threshold=0.9))  # 取消
            self.logger.info("关闭信赖度章节")
            sleep(2)
        except:
            pass
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720)), timeout=5)  # 关闭
            touch(Template(self.shot_path + page_info.common_button_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720)))  # 关闭
            self.logger.info("关闭剧情提示")
        except:
            pass
        sleep(2)
        self.logger.info("地图通关，结束")
