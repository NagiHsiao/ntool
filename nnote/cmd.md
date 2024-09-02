# 

[TOC]

# [Glob模式](https://www.cnblogs.com/savorboard/p/glob.html)

![image-20240902160216279](C:\Users\ZhuanZ\AppData\Roaming\Typora\typora-user-images\image-20240902160216279.png)

# [BNF](https://hackmd.io/@ShenTengTu/HJzCM3aDr)

![image-20240902151414027](C:\Users\ZhuanZ\AppData\Roaming\Typora\typora-user-images\image-20240902151414027.png)

# github

## [git](https://git-scm.com/book/zh/v2) status

```cpp
git [status | diff]

git add [{文件名}* | . | {目录名}] //到暂存区Staging Area

//remove    
git rm  [ {文件} //删除暂存
	    | --cached {文件} //仅删除暂存，保留在文件系统
        | {\*~}{log/\*.log}  //Glob模式 {~结尾文件}
         					 //{log/目录下扩展名.logs所有文件}
]
    
git log -p -2   //历史提交
git log --stats //简略

```

![image-20240902150712265](C:\Users\ZhuanZ\AppData\Roaming\Typora\typora-user-images\image-20240902150712265.png)

## [git clone配置代理](https://blog.xiaoqi.work/index.php/2024/01/31/hello-world/)

> Q1：挂梯子git clone依旧慢

```
//7890配置代理的端口
git config --global http.proxy "127.0.0.1:7890"  
git config --global https.proxy "127.0.0.1:7890"
```



# cmd相关

## start

```cpp
start {cmd.md}  //打开文件
git diff  //比较暂存staged和文件系统
```

## dir

```
{磁盘} //例如C:
dir //ls -a
cls //cleanscreen

//新建文件        all | wide | page
mrdir [{指定目录}] [/a | /w | /p]

```

## echo 

```cpp
echo [{txt}] > .gitignore  //新建
echo {txt} >> .gitignore //追加
type {markdown}
```

## cmd默认路径

> 算法

```cmd
//cmd默认路径
win+R : regedit
注册表编辑器 ：计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor
新建 ： 字符串值，命名为autorun
修改 ： cd /d {your_formal_path}
win+R ： 验收结果
    
EOF.
```

> [案例1](https://blog.csdn.net/m0_62975468/article/details/126287883)

```cmd
// cmd 注释
:: {commnet}
```



# pip相关

## pip install 换源

> Q1：换源

```cmd
// 临时换源
pip install markdown -i {src_url}

//永久换源
pip config set global.index-url {src_url}

//源
https://mirrors.aliyun.com/pypi/simple/ :: 阿里云
http://pypi.douban.com/simple/ :: 豆瓣
https://pypi.tuna.tsinghua.edu.cn/simple/ :: 清华大学
http://pypi.mirrors.ustc.edu.cn/simple/ :: 中国科学技术大学 
```



## pip install -r requirement.txt

> Q1: 安装失败

```cpp
// 安装失败时的策略
注释失败的part ： #requirement.txt
最后安装      

EOF.
```

> Q2:常用

```python
//freeze your rqt file
pip freeze > {requirement.txt}

//
```



## pip3 show numpy

> 查看版本

# mod相关

## py -m venv vr-1

> 创建虚拟环境vr-1

```cpp
//venv name and filename at same time
py -m venv {name_of_venv}
```

