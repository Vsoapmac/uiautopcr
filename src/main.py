import pytest, time, subprocess
import ModelMapper as mapper
from Utils.PathUtils import PathUtils
from Utils.YamlUtils import YamlUtils
from datetime import datetime

# 加载配置文件
config_dict = YamlUtils.loadYamlFile(PathUtils.getConfigPath() + "config.yml")
shutdown_when_finish = config_dict["shutdown_when_finish"]
start_timer = config_dict["start_timer"]
rerun_if_fail = config_dict["rerun_if_fail"]
run_model_list = config_dict["run_model_list"]
run_plugins = config_dict["run_plugins"]
plugins_run_times = config_dict["plugins_run_times"]
plugins_model = config_dict["plugins_model"]

"""
装载pytest模块命令参数
"""
# 主参数
pytest_param_list = ["-s"]
# 副参数
if rerun_if_fail != 0:
    pytest_param_list.append("--reruns=" + rerun_if_fail)
# 判断是否开启插件运行
if not run_plugins:
    run_case_path = PathUtils.getRunCasePath()
    # pytest模块
    for model in run_model_list:
        pytest_param_list.append(run_case_path + mapper.main_model_dict[model])  # 进行模块映射并与地址一起存进list中
elif run_plugins:
    plugins_path = PathUtils.getPluginsPath()
    # 运行次数
    if plugins_run_times > 1:
        pytest_param_list.append("--count=" + plugins_run_times)
    # pytest模块
    pytest_param_list.append(plugins_path + mapper.plugins_model_dict[plugins_model])  # 进行模块映射并与地址一起存进list中
"""
运行
"""
# 定时条件
if start_timer != False:
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
