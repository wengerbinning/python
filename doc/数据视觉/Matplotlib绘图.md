# Matplotlib绘图
```
author: ClarkAaron
creationTime: 2020-01-22 18:05
```
* Matplotlib类似于Matlab的绘图库,绘图函数集合在pyplot模块中;
  
## 绘制散点图
---
* 绘制简单的散点图:
  ```
  from matplotlib import pyplot as plt
  import numpy as np
  x = np.random.randn(1000)
  y = np.random.randn(1000)
  plt.scatter(x,y)
  plt.title("Title")
  plt.show()
  ```
* 绘制复杂的散点图:
  ```
  plt.scatter(x,y,s=None,c=None,marker=None,alpha=None)
  ```
## 绘制折线图
---
* 使用plot绘制折线图

## 绘制柱状图
---
* 使用bar绘制柱状图;

## 绘制箱线图
---
* 使用boxplot绘制箱线图;