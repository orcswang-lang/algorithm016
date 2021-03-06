学习笔记
### 动态规划

#### 思维要点

- 动态规划和递归、分治没有根本上的区别，关键看有无最优子结构
- 共性：找到重复子问题
- 差异性：最优子结构、中途可以淘汰次优解

#### 关键点
- 动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）
- 共性：找到重复子问题
- 差异性：最优子结构、中途可以淘汰次优解
- 最优子结构：opt[n] = best_of(opt[n-1], opt[n-2], ...)
- 储存中间状态：opt[i]
- 递推公式（美其名曰：状态转移方程或者DP方程）
      Fib: opt[n] = opt[n-1] + opt[n-2]
      二维路径: opt[i][j] = opt[i+1][j] + opt[i][j+1] (且判断a[i][j]是否为空地)

#### 解题步骤

- 化繁为简，分解成子问题
- 定义状态空间，储存中间状态（opt[i]）
- 动态规划方程

