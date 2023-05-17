# 简介

公主连结的日常脚本，用于刷取公主连结游戏中的重复内容，并解放双手做其他事情

# 使用声明

该项目使用的技术是模拟人在手机、模拟器上的操作，**不会修改任何的游戏数据**，理论上不会造成任何封号等处罚。

如果使用该项目时封号等处罚，作者将**不承担任何风险和责任**。

# 部署与运行流程

所需软件/硬件：

- 安卓模拟器(夜神最优)或真机
- python
- Android SDK

Android SDK是电脑驱动安卓手机或模拟器的主要方式，其中最重要的是adb.exe，windows系统就靠它去驱动安卓手机的。如果需要查询手机的UUID(电脑识别模拟器/手机的唯一标识符)，则需要输入一些命令去查看这个标识符

关于如何配置Android SDK，如下：

1. 首先下载Android SDK: [Android SDK下载网址(AndroidDevTools)](https://www.androiddevtools.cn/)
2. 解压缩，记录好位置，比如说`D:\android-sdk-windows`
3. 双击打开Android SDK目录下的`SDK Manager.exe`，安装`Android 11`、`Android 10`、`Android 9`、`Android 7`、`Android 4`(最重要是9和7，因为大部分模拟器都是这个型号，其次是根据自己的真机的安卓版本对应安装)
4. 右键我的电脑（此电脑）—> 属性 —> 高级系统设置 —> 环境变量 —> 系统变量。找到path，并加上三个系统变量，分别是，其中`%ANDROID_HOME%`是第二步记录的位置：
   1. %ANDROID_HOME%\platforms，例如：`D:\android-sdk-windows\platforms`
   2. %ANDROID_HOME%\tools，例如：`D:\android-sdk-windows\tools`
5. 输入`adb devices`查看是否配置成功，否则重启电脑。

如果只用模拟器，似乎并不需要额外配置Android SDK，但是作者推荐去额外配置一个sdk，这样可以自己查询相应的UUID了，使用`adb devices`即可查看。如果需要迁移运行电脑，可以下载好的sdk压缩好然后在新电脑上解压并配置系统变量即可，麻烦一时，安心一世。

该项目理论上支持所有模拟器，但夜神模拟器效果最好。

无论使用什么模拟器，都需要

**将分辨率调到1280 * 720**

**将分辨率调到1280 * 720**

**将分辨率调到1280 * 720**

否则系统可能会出现识别不准确等情况

## 不会python的用户

部署流程如下:

1. 下载项目，将项目命名为uiautopcr(**注意这很重要**)
2. 去python官网找到`python 3.9.x`或者`python 3.8.x`的版本，下载python windows installer，下载地址为: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
3. 安装python，注意如果有`bat`、`cmd`等字眼注意勾选，目的是将python添加到环境变量中，这样就可以在命令行里面运行python命令
4. 进入命令行，输入`python -V`检查是否安装成功，如果安装成功，命令行提示符会出现python当前的版本号
5. 运行`安装项目所需第三方库.bat`

部署完成后，运行流程如下:

1. 修改config目录下面对应的参数
2. 运行run.bat文件执行项目

## 会python的用户

优先推荐使用conda环境

部署流程如下:

1. 下载项目，将项目命名为uiautopcr(**注意这很重要**)
2. 安装anaconda3或miniconda(python环境也行)
3. 使用指令`conda create -n uiautopcr python==3.9.16`创建conda环境(若直接安装python的用户则直接忽略这一步)
4. 使用指令`conda activate uiautopcr`激活conda环境(若直接安装python的用户则直接忽略这一步)
5. cd 到当前目录，使用指令`pip install -r requirements.txt`

部署完成后，运行流程如下:

1. 修改config目录下面对应的参数
2. 运行`src`目录下面的`main.py`即可运行

# 设置参考

这里放出默认设置:

```yaml
# 基础设置
# 真机: UUID。如: 10ACAU0MQX001UX (一般是5037端口，其他也行，能连上手机就行)
# 夜神模拟器: 127.0.0.1:62025
# mumu模拟器: 127.0.0.1:7555
client_url: 127.0.0.1:62025 # 设备连接UUID或url
log_output: false # 是否将日志写入文件

# 运行设置
shutdown_when_finish: false # 运行完毕后是否关机
# 定时运行，不定时则输入false，定时则输入时间，格式%H:%M(24小时)，如18:13，程序在这个时间后执行模块(需要加引号)，若设置的定时时间小于当前时间，则不定时直接开始
start_timer: false
rerun_if_fail: 0 # 运行失败后重新运行次数
run_model_list: # 运行的模块列表，注意先后顺序
    - 任务
    - 工会之家
    - 商店
    - 探索
    - 调查
    - 竞技场
    - 地下城
    - 任务
    - 礼物

# 插件模块设置
run_plugins: false # 运行其他插件模块(开启后，不会运行主要模块)
plugins_run_times: 10 # 插件模块运行次数
# 需要运行的插件模块，以下是可运行的插件
# 信赖度, 普通过图
plugins_model: 普通过图
```

# 开发者提示

如果需要增加额外的插件模块，在Plugins包中增加测试类后，在`ModelMapper.py`中增加`plugins_model_dict`中对应的映射，就可以在设置中配置自定义的模块了