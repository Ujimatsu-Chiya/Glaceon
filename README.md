# Sylveon

一款关于XCPC(X Collegiate Programming Contest)，OI(Olympiad in Informatics) 的随机测试数据生成器。

Sylveon名字来源：宝可梦中，仙子伊布的英文名。

比起[CYaRon](https://github.com/luogu-dev/cyaron)，其优势在于：

1. 生成的图中，边权可以包含多个，并且包含了不同类型，如以下输入：

```
5 6
1 2 300 a
2 3 400 b
2 4 700 x
2 5 100 y
1 5 600 z
3 5 2 w
```

2. 通过一些选项，支持图的邻接矩阵输出。
3. 生成迷宫，用于BFS和DFS的一些题目。
4. 生成核心代码模式下所需要的代码。

有空再进行填充。
