import pytest, time, subprocess
from Utils.PathUtils import PathUtils
from Utils.YamlUtils import YamlUtils
from datetime import datetime


# 加载配置文件
config_dict = YamlUtils.loadYamlFile(PathUtils.getConfigPath() + "config.yml")
shutdown_when_finish = config_dict["shutdown_when_finish"]
start_timer = config_dict["start_timer"]
rerun_if_faile = config_dict["rerun_if_faile"]
run_model_list = config_dict["run_model_list"]

"""
装载pytest模块
"""
# TODO:增加plugins中的逻辑
run_case_path = PathUtils.getRunCasePath()
model_mapping = {
    # "登录": "TestLogin", # 运行逻辑复杂，暂时不搞
    "礼物": "TestGift.py",
    "任务": "TestMission.py",
    "工会之家": "TestDepartment.py",
    "商店": "TestShop.py",
    "探索": "TestSearch.py",
    "调查": "TestInvest.py",
    "竞技场": "TestArana.py",
    "地下城": "TestDungeons.py",
}
# 主参数
pytest_param_list = ["-s"]
# 副参数
if rerun_if_faile != 0:
    pytest_param_list.append("--reruns="+rerun_if_faile)
# pytest模块
for model in run_model_list:
    pytest_param_list.append(run_case_path+model_mapping[model]) # 进行模块映射并与地址一起存进list中
"""
运行
"""
# 定时条件
if start_timer!=False:
    now = datetime.now()
    year_month_day = now.strftime("%Y-%m-%d")
    end = datetime.strptime(year_month_day + " " + start_timer, "%Y-%m-%d %H:%M")
    d = end - now
    if d.days >= 0:
        time.sleep(d.seconds)
# 开始运行
pytest.main(pytest_param_list)
# 运行结束
# 关机
if shutdown_when_finish:
    time.sleep(1)
    subprocess.Popen("shutdown -p")