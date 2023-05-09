from Common.ClientBasic import *


class TestReliability(ClientBasic):
    """信赖度章节"""
    __page_dict = page_info.plugins_dict

    def test_reliability_new_content(self):
        """信赖度"""
        self.logger.info("点击信赖度")
        try:
            wait(Template(self.shot_path + self.__page_dict["reliability_new_content"], resolution=(1280, 720)), timeout=2)  # 新内容
        except:
            self.logger.info("暂无新内容")
        else:
            touch(Template(self.shot_path + self.__page_dict["reliability_new_content"], resolution=(1280, 720)))  # 新内容
            sleep(1)
            self.logger.info("点击语音，并完成信赖度对话")
            touch(Template(self.shot_path + self.__page_dict["reliability_none_voice"], record_pos=(-0.001, 0.097), threshold=0.9,
                           resolution=(1280, 720)))  # 无语音
            sleep(5)
            for i in range(10):
                touch([0.501 * self.w, 0.417 * self.h])  # 中间
                sleep(2)
            self.logger.info("信赖度对话完毕")