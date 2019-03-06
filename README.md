一、python_CTP
(1)使用Python封装了上期技术开发的CTPApi
(2)默认连接SimNow的第一套环境，方便调试每个Api
(3)通过配置将自己的报单和成交信息记录到自己的数据库
(4)便于维护和管理自己的策略，并且可能实现策略验证 

二、发布新的CTP版本
只需在 setup.py 中修改 CTP_Version="6.3.11" 成具体的版本就可以实现，其它几乎不要变化
在实现自己的策略时，只需继承 CPyMDAPI, CPyTraderAPI，然后实现这些接口就可了，内部封装了回调细节。

三、编译
build.bat

四、安装
install.bat

五、简单案例
#!/usr/bin/env python3
# encoding:utf-8
