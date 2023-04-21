# 简介

公主连结的日常脚本，用于刷取公主连结游戏中的重复内容，并解放双手做其他事情

# 使用声明

该项目使用的技术是模拟人在手机、模拟器上的操作，**不会修改任何的游戏数据**，理论上不会造成任何封号等处罚。

如果使用该项目时封号等处罚，作者将**不承担任何风险和责任**。

# 支持模拟器

理论上支持所有模拟器，但夜神模拟器效果最好。

无论使用什么模拟器，都**需要将分辨率调到1280 * 720**，否则会出现识别错误等情况

也可以使用真机，但是不确定会有未知的bug

# 使用指南

## 部署与运行流程

### 不会python的用户

部署流程如下:

1. 下载项目，将项目命名为uiautopcr(**注意这很重要**)
2. 去python官网找到`python 3.9.x`或者`python 3.8.x`的版本，下载python windows installer，下载地址为: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
3. 安装python，注意如果有`bat`、`cmd`等字眼注意勾选，目的是将python添加到环境变量中，这样就可以在命令行里面运行python命令
4. 进入命令行，输入`python -V`检查是否安装成功，如果安装成功，命令行提示符会出现python当前的版本号
5. 运行`安装项目所需第三方库.bat`

部署完成后，运行流程如下:

1. 修改config目录下面对应的参数
2. 运行run.bat文件执行项目

### 会python的用户

优先推荐使用conda环境

部署流程如下:

1. 下载项目，将项目命名为uiautopcr(**注意这很重要**)，可以在Utils包中的
2. 安装anaconda3或miniconda(python环境也行)
3. 使用指令`conda create -n uiautopcr python==3.9.16`创建conda环境(若直接安装python的用户则直接忽略这一步)
4. 使用指令`conda activate uiautopcr`激活conda环境(若直接安装python的用户则直接忽略这一步)
5. cd 到当前目录，使用指令`pip install -r requirements.txt`

部署完成后，运行流程如下:

1. 修改config目录下面对应的参数
2. 运行`src`目录下面的`main.py`即可运行