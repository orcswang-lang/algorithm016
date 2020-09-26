## 学习笔记

#### 时间复杂度
> 表示方式
* 大 O 表示法，程序运行之前是无法预估运行耗时的，但是通过相同代码被重复执行次数，可判定代码执行时间的好坏。
* 常见的时间复杂度

| 时间复杂度 | 描述 |
| :---- | :---- |
|常数阶O(1)|代码只被执行一次, 比如：变量、判断等|
|线性阶O(n)|相同代码被执行了n次， 比如：单层 for/while loop|
|平方阶O(n^2)|代码被执行指数此， 比如：多层 for 嵌套|
|対数阶O(logn)|代码被执行対数次，比如：二分查找|
|线性对数阶O(nlogn)|代码只被执行n*logn|

### 算法题最大误区：只做一遍！！！

### 五毒神掌
1. 5-10 分钟读题和思考，如果没有思路，看题解，默写代码
1. 马上自己写，提交LeetCode，多种解法，体会优化
1. 24 小时之后，再重复做题
1. 一周后重复做题
1. 面试前一周恢复性训练

### 切题四件套
1. 理清题意，确定题目的要求
2. 想尽可能多的解法，对比几种写法的时空复杂度，找到比较好的解法
3. 尽可能多地动手写
4. 测试用例

#### 一维数据结构
1. 数组 array，查询速度快，时间复杂度O(1)，删除、添加的速度慢，时间复杂度O(n)。
2. 链表 linked list，查询速度慢，时间复杂度O(n)；删除、添加的速度快，时间复杂度O(1)。
3. 栈 stack, 先进后出 FILO，查询速度为O(n)；删除、添加的速度快，时间复杂度O(1)。
4. 队列 queue，先进先出，FIFO，查询速度为O(n)；删除、添加的速度快，时间复杂度O(1)。
5. 双端队列 deque, queue 和 stack 的结合体，头和尾都可以进行元素的push和pop，查询速度为O(n)，删除、添加速度为O(1)。
6. 集合 set,
7. hash表 map,

#### 二维数据结构
1. 树 tree,
2. 图 graph,
3. 二叉搜索树 binary search tree,
4. 堆 heap,
5. 并查集 disjoint set,
6. 字典树

#### 特殊数据结构
1. 位运算 Bitwise,
2. 布隆过滤器 Bloom Fiilter,
3. LruChache

## 数组和链表时间复杂度
|  操作   |  数组 |  链表  |
|  ----  | ----  |  ---   |
| prepend| o(1)  |  o(1)  |
| append | o(1)  |  o(1)  |
| lookup | o(1)  |  o(n)  |
| insert | o(n)  |  o(1)  |
| delete | o(n)  |  o(1)  |

##### 1.1 数组
连续内存块，在插入，删除过程中需要移动对应位置的后面所有元素，具有o(n)复杂度。在对应位置查找中具有o(1)复杂度。

在高级语言中的数组，一般至少含有原始数组及size及cap三个成员变量，当size==cap后继续append，需要分配更大的连续内存存放数据
以及复制原有数据到新的内存空间中再继续后续的append操作，意味着数组初始化容量太小，会有多次扩容复制以及内存垃圾的产生，因此
尽量在使用的过程中确定数组的size范围来初始化数组

数组相较链表，内存位置连续，这样更有可能利用上cpu cache，例如同样从0->n的遍历，数组要比链表快

虽然数组具有高速访问数据的特性，但是删除上的性能过低，无法直接用于当做队列结构，可以封装成环来充当队列

#### 1.2 链表
链表的处理尽量加上哨兵来简化操作

#### 1.3 跳表
跳表主要麻烦在插入，删除节点的处理，处理不好会导致导致高层节点间的元素不均衡，会导致查询时间复杂度退化到o(n)

#### 1.4 队列
1. ### queue
    1. 特点:FIFO(first in first out),添加只能在队尾,删除只能删队头节点
    2. 主要方法:`offer()`：添加队尾节点;`poll()`：删除队头节点;`peek()`：获取队头节点
    3. 实现:很多实现类,常用实现LinkedList(链表,LinkedList实现Deuque,Deque实现Queue)
    4. 方法分析(以LinkedList为例):
        1. offer,最终调用的是`linkLast`,见注释
        ```
        void linkLast(E e) {
                //指向最后一个节点
                final Node<E> l = last;
                //创建一个prev节点为l,next节点为null的节点
                final Node<E> newNode = new Node<>(l, e, null);
                last = newNode;
                if (l == null)
                    //如何链表为空,first节点赋为newNode
                    first = newNode;
                else
                    //原有尾节点的next改为新增节点
                    l.next = newNode;
                size++;
                modCount++;
            }
        ```
        2.poll,最终调用的是`unlinkFirst`,见注释
        
        ```
           //f=first
         private E unlinkFirst(Node<E> f) {
            // assert f == first && f != null;
            final E element = f.item;
            final Node<E> next = f.next;
            f.item = null;
            f.next = null; // help GC
            //移除头结点
            first = next;
            if (next == null)
                last = null;
            else
                //清理头结点的prev节点
                next.prev = null;
            size--;
            modCount++;
            return element;
        }
        ```
        3.peek,比较简单,见注释
        
        ```
        public E peek() {
            //返回头节点,空链表返回空
            final Node<E> f = first;
            return (f == null) ? null : f.item;
        }
        ```
1. ### PriorityQueue
    1. 特点:优先队列,不同于FIFO,每次出队的节点为优先级最高的节点
    2. 本质:通过数组实现了一个平衡二叉树
        1. 头结点为优先级最高节点(自然排序的情况下)
        2. 左右,父节点有如下特点
            1. parentNode=(currentNode-1)/2
            2. leftNode=parentNode*2+1
            3. rightNode=parentNode*2+2
    3. 主要方法:`offer()`：添加节点;`remove()`：删除节点;
    4. 方法图例
        1.![avatar](https://img-blog.csdnimg.cn/20190417102145729.jpg)
       
    5. 方法分析(以LinkedList为例):
        1. `offer`:插入节点比较后可能上浮
        
        ```
        public boolean offer(E e) {
            if (e == null)
                throw new NullPointerException();
            modCount++;
            int i = size;
            if (i >= queue.length)
                grow(i + 1);//如需扩容,用copy方式扩容
            size = i + 1;
            if (i == 0)
                queue[0] = e;
            else
                siftUp(i, e);
            return true;
        }
        //自然顺序下siftUp调用的方法,比较上浮,rmove的上浮也是这个方法
        private void siftUpComparable(int k, E x) {
            Comparable<? super E> key = (Comparable<? super E>) x;
            while (k > 0) {
                int parent = (k - 1) >>> 1;
                Object e = queue[parent];
                if (key.compareTo((E) e) >= 0)
                    break;
                queue[k] = e;
                k = parent;
            }
            queue[k] = key;
        }
        ```
        2. `remove`:删除节点后,末尾节点可能上浮或下沉
        
        ```
        public boolean remove(Object o) {
            int i = indexOf(o);//查找到待删除节点
            if (i == -1)
                return false;
            else {
                removeAt(i);
                return true;
            }
        }
        private E removeAt(int i) {
            // assert i >= 0 && i < size;
            modCount++;
            int s = --size;
            if (s == i) // removed last element
                queue[i] = null;
            else {
                E moved = (E) queue[s];
                queue[s] = null;
                //下沉
                siftDown(i, moved);
                //如果没交换
                if (queue[i] == moved) {
                    //上浮
                    siftUp(i, moved);
                    if (queue[i] != moved)
                        return moved;
                }
            }
            return null;
        }
        ```

### 一些思想
+ 写代码要采用自顶向下的编程方式，即先写主干逻辑，再写具体实现；
+ 双指针的算法一般要先进行排序；
+ 一维数据要加速可以通过升维度，如 有序的链表升为跳表；


|#|标题|解决思路|
|---|---|------|
|1|[两数之和](https://leetcode-cn.com/problems/two-sum/) | 用字典存储值和索引位置的关系|
|11|[盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | 双指针（左右指针不断逼近）|
|15|[三数之和](https://leetcode-cn.com/problems/3sum)| 排序 + 双指针|
|21|[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | 递归（确定好终止条件和循环条件）|
|26|[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | [双指针](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11751/Simple-Python-solution-O(n)) 指针i指向开始位置，指针j不断后移去找和i位置不同的值|
|42|[接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | 栈|
|66|[加一](https://leetcode.com/problems/plus-one/) | 只有两种情况，除 9之外的数字加一；数字 9 加一得10进一位 个位数为 0 |
|70|[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | 递推，动态规划，每次只能爬 11 级或 22 级，所以 f(x)f(x) 只能从 f(x - 1)f(x−1) 和 f(x - 2)f(x−2) 转移过来|
|84|[柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | 栈|
|88|[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) |使用了三个指针 p1指向num1数组位置m-1，p2指向num2数组位置n-1，p指针指向nums1数组最后一个位置|
|155|[最小栈](https://leetcode-cn.com/problems/min-stack) | getMin()函数实现再增加一个栈存储每次插入时候的最小值|
|189|[旋转数组](https://leetcode-cn.com/problems/rotate-array) | 三次翻转k%n|
|206|[反转链表](https://leetcode-cn.com/problems/reverse-linked-list)|双指针|
|239|[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | 双端队列|
|283|[移动零](https://leetcode-cn.com/problems/move-zeroes)| 暴力：统计0的个数；用指针j存储非0元素的位置，遍历数组找不为0的值赋值给索引j对应的元素|
|641|[设计循环双端队列](https://leetcode.com/problems/design-circular-deque/)| 需要capacity,size,front,rear,data参数，插入判断满，删除判断空|

### 推荐github地址
https://github.com/labuladong/fucking-algorithm

## 转载：
https://github.com/wentianyang/algorithm016/blob/master/Week_01/README.md
https://github.com/RainAlways/algorithm016/tree/master/Week_01

![](https://raw.githubusercontent.com/haxianhe/pic/master/image/%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5.png)

![](https://raw.githubusercontent.com/haxianhe/pic/master/image/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95.png)