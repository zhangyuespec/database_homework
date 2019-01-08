# database_homework
## 1.运行环境
* 在ubuntu系统下,python3运行.需要安装PyMySQL模块
* pip3 install PyMySQL
* 如果出错,请卸载重装,并且按照出错提示百度一下解决办法,每个电脑运行环境不同

## 2.使用方法
* 2.1首先运行init.py文件,这个文件是初始化数据库中一些数据的.运行时需要输入本机的数据库密码 命令python init.py
* 2.2如果忘记本机数据库密码无法使用,则参考https://blog.csdn.net/qq_34788903/article/details/86062217
* 2.3运行完成init.py文件没有出错后,运行main.py文件 命令python main.py.
  同样需要输入本机数据库密码.
* 2.4运行程序之后,如果有账号则直接登录,如果没有账号则首先创建账号再登录,管理员账号是zhangyue,密码是123456
* 2.5管理员账号具有对航班,出租车,宾馆,用户账号信息的增删改查权限.普通用户账号只有查看和预定航班,出租车,宾馆的权限

## 3.测试用例
#### 3.1管理员

#### ##### 1.登录

#### ![1546912294765](/home/zhangyue/.config/Typora/typora-user-images/1546912294765.png)

##### ２．修改用户信息，输入１修改用户信息，目前只有管理员一个用户，管理员无权删除用户，只能帮助用户修改密码。

![1546912359163](/home/zhangyue/.config/Typora/typora-user-images/1546912359163.png)

##### ３．修改航班信息，首先会打印出所有的航班信息。

![1546912440343](/home/zhangyue/.config/Typora/typora-user-images/1546912440343.png)

![1546912472343](/home/zhangyue/.config/Typora/typora-user-images/1546912472343.png)

如果想增加航班就输入１，我们以增加航班为例。

![1546912609016](/home/zhangyue/.config/Typora/typora-user-images/1546912609016.png)

数据库增加信息在最后一行

![1546912630967](/home/zhangyue/.config/Typora/typora-user-images/1546912630967.png)

** 但是这里请注意：信息中间的逗号需要是英文的逗号，数字需要是英文状态下的数字，否则可能出错。

##### 4.修改宾馆信息

![1546912805271](/home/zhangyue/.config/Typora/typora-user-images/1546912805271.png)

选择相应的功能进行修改即可，进入功能之后提示都很完备。

##### 5.修改出租车信息

![1546912891798](/home/zhangyue/.config/Typora/typora-user-images/1546912891798.png)

增删改查操作按照提示即可完成

##### 6.修改用户预定信息

![1546912956262](/home/zhangyue/.config/Typora/typora-user-images/1546912956262.png)

因暂时没有普通用户登录所以没有信息

##### 7.退出系统

![1546913009860](/home/zhangyue/.config/Typora/typora-user-images/1546913009860.png)



### 普通用户登录

##### 1.注册

可以直接选择注册，或者当用户名不存在时直接跳转到注册功能。注册完成之后自动登录

![1546913149429](/home/zhangyue/.config/Typora/typora-user-images/1546913149429.png)

##### 2.查看航班

![1546913187054](/home/zhangyue/.config/Typora/typora-user-images/1546913187054.png)

##### 3.查看出租

![1546913223511](/home/zhangyue/.config/Typora/typora-user-images/1546913223511.png)



##### 4.查看宾馆

![1546913249078](/home/zhangyue/.config/Typora/typora-user-images/1546913249078.png)



##### 5.预定

预定可以选择预定航班，出租或者宾馆，这里我们以预定航班为例

![1546913342475](/home/zhangyue/.config/Typora/typora-user-images/1546913342475.png)

预定成功和失败都有提示，这时候我们可以查看航班信息会发现东航２５５的可用座位数量少了１０个

![1546913404532](/home/zhangyue/.config/Typora/typora-user-images/1546913404532.png)

##### 6.查看自己预定

![1546913443410](/home/zhangyue/.config/Typora/typora-user-images/1546913443410.png)

输入５即可查看自己的预定，我们可以看到预定了东航２５５，数量为１０．

###### 7.管理员查看用户预定

![1546913536645](/home/zhangyue/.config/Typora/typora-user-images/1546913536645.png)

可以看到用户名和预定信息，也可以看到用户账号信息

![1546913574744](/home/zhangyue/.config/Typora/typora-user-images/1546913574744.png)

现在系统内用户除了管理员还有一个叫做ｚｚ的用户。