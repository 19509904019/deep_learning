"""
保存

torch.save(模型名称,'name.pth')


加载
先导入构建的网络

from xxx import *

t = torch.load('name.pth')

如果要在网络上添加层，则如下：
t.add_module('str',nn.Linear())
"""
