# python_CTP
使用Python封装了 上期技术开发的CTPApi，方便策略设计和实现者实现自己的想法

只需在 setup.py 中修改 CTP_Version="6.3.11" 成具体的版本就可以实现，其它几乎不要变化
在实现自己的策略时，只需继承 CPyMDAPI, CPyTraderAPI，然后实现这些接口就可了，内部封装了回调细节。

#编译
build.bat

#安装
install.bat

#sample
#!/usr/bin/env python3
# encoding:utf-8
