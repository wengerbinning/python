# Python流程结构

[//]: # (__author__ = "Clark Aaron")

流程结构可分为顺序结构、分支结构、循环结构,而顺序结构是由上至下、从左至右、依次执行，是程序执行的默认结构。在Python中由if执行分支结构，for、
while来执行循环结构。pass为跳过该程序段，break为跳出当前循环，continue为结束本次循环进入下次循环。

## 分支语句

### if

```python
# There can be zero or more elif parts, and the else part is optional.
if <condition>:
    <execute-the-code>
elif <condition_1>:
    <execute-the-code_1>
elif <condition-2>:
    <execute-the-code_2>
else:
    <execute-the-code_end>
```

## 循环语句

### for

### while

## 控制语句

### pass

### break

在循环中的作用: 退出循环体;

### continue

在循环中的作用: 终止本次循环,进入下次循环;

* else在for语句中迭代器迭代完成或while语句中条件为假时执行，被break终止时则不会执行。
* 循环的嵌套: 循环体可以嵌套,但在实际中由于程序的时间复杂度的限制,嵌套层数不能太多;
