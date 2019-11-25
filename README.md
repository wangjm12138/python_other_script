# Python 模块

## 常规记录：

## 面向对象理解

<https://www.jianshu.com/p/2e2ee316cfd0>

 https://www.cnblogs.com/huchong/p/8244279.html 

### 1. \_\_new\_\_， \_\_init\_\_， \_\_call\_\_三个方法

 \_\_new\_\_，对象的创建，是一个静态方法，第一个参数是cls

 \_\_init\_\_，对象的初始化，是一个实例方法，第一个参数是self

 \_\_call\_\_，对象可call

1.\_\_new\_\_，和_\_init\_\_详解：new方法先被调用，返回一个实例对象，接着init被调用，从输出结果来看，new方法的返回值就是类的实例对象，这个实例对象会传递给init方法中定义的self参数，以便实例对象可以被正确地初始化。

2.如果new方法不返回值(或者说返回None)，那么ini将不会得到调用，这个也说的通，因为实例对象都还没创建起来，调用init也没什么用，此外，python还规定，init只能返回None值，否者会报错。__init__方法中除了self之外定义的参数，都将与__new__方法中除cls参数之外的参数是必须保持一致或者等效。因为Bar(x, y)传参的时候是先给到__new__(), 然后再传递给init。

3.new方法在类定义不是必须写的，如果没定义，默认会调用object. \_\_new\_\_去创建一个对象，如果定义了，就是override，可以custom创建对象行为。如果每次创建对象返回同一个就是单例模式了，下面会举个例子说明，并列举几种单例模式。

4.如果是采取自定义的new，是重载了父类的new，所以要自己显示调用父类的new，即object. \_\_new\_\_,或者用super()，所以自定义的new就需要用以下两种中其中一种：

- object. \_\_new\_\_(cls,*args,**kwargs)

- super(Bar.cls)._\_new\_\_(cls)

5.实例化后的对象，再当函数一样执行就会执行到这个 \_\_call\_\_函数

### 2.type和object的关系

<type 'type'>和<type 'object'>理解这两个类型有助于理解为什么要使用元类，理解单例模式等等，那么他们之间区别和联系是什么，下面来一一讲解。

平常定义一个类别时候如：

```
class A(object)：
	pass
a=A()
print(a.__class__)
<class '__main__.A'>
print(a.__bases__)
AttributeError: 'A' object has no attribute '__bases__'
print(A.__bases__)
(<class 'object'>,)
print(A.__class__)
<class 'type'>
print(object.__bases__)
()
print(object.__class__)
<class 'type'>
print(type.__bases__)
(<class 'object'>,)
print(type.__class__)
<class 'type'>
```

\_\_class\_\_属性表明是谁的实例，\_\_bases\_\_属性表明谁是父类。

这时候父类是object，其实object是所有类的超类，所有类都继承了object的，而type是object类型，或者说object是type的一个实例。**但是还有一句话，object又是type的超类**。这里会比较费解，由上面那几个print可以得出这个结论：

简单解释：

1.object比作是中国人，剩下所有类都是炎黄子孙，所以当你定义class A，class B，等等不管怎么样都是源头都是object，所以这条继承线是比较清晰的，object ---- class A / B /C ....等等，对应属性是\_\_bases\_\_

2.type比作是人,



由图形来详加解释：

## argparse模块

## logging模块

## 字符byte和字符串string类型

# Pypi包开发

# python包的开发和发布

---

## python各种类型包以及打包工具的梳理
python的打包工具是挺多的，主要有：  
1.distutils  
2.distutils2  
3.setuptools  
4.distribute 
然后python包的类型有,源码包，轮子包（我自己叫法），蟒蛇蛋：
1.\*.tar.gz，*zip，*.tar.bz2，*.tar等
2.\*.whl
3.\*.egg
最后还有包管理工具主要有pip和easy_install，常用来用安装。
打包工具是用来制作包的，制作成源码包，轮子包，蟒蛇蛋的，而pip和easy_install是用来安装包的，这点应该都知道。
打包工具中，distutils是亲儿子，是python标准库的一部分，在2000年发布，setup.py就是distutils的功能写成，可以随便找个网络上的例子来验证，这边随便截取网络一个例子：
hello.py文件：
def hello_fun():
&ensp; &ensp;print "i say hello to you"
setup.py文件：
from distutils.core import setup

setup(
&ensp; &ensp;name="hello_module",
&ensp; &ensp;version="1.0",
&ensp; &ensp;author="ljk",
&ensp; &ensp;author_email="wilber@sh.com",
&ensp; &ensp;py_modules=['hello'],
)
执行：python setup sdist
这时候可以看到目录结构有这几个，dist就是生成的源码包。
![](https://wiki.chinanetcenter.com/html/doc//20190930/1569830183991image.png)  
OK，言归正传，distutils是python亲儿子，distutils2就是二儿子，新诞生的，然后setuptools是增强distutils而产生的，是distutils的增强版，而这个打包工具是本次介绍的核心！！！，然后distribute是setuptools的一个分支版本，大体关系就是这样，现在一般都是用distutils和setuptools(后面distribute也合并到setuptools了)这两个。
再说说包的类型，蟒蛇单是早期用的，现在普遍是用whl或者源码包，蟒蛇蛋一般用easy_install来安装，当然用pip也可以，所以包的类型和包的管理工具可以认为：
egg和easy_install是旧式，而pip和whl是新式，whl出现是为了替代egg，可能是规范如何打包等等，具体不太懂，可以自行查询。

## 准备阶段
这个是setuptools的官网
https://setuptools.readthedocs.io/en/latest/setuptools.html
其实setuptools和上面的distutils是差不多的，毕竟是增强集合，所以setup.py写法差不多，可以看一个例子，setup.py文件：
\#coding:utf8
from setuptools import setup, find_packages

setup(
&ensp; &ensp; name='MyApp', # 应用名
&ensp; &ensp; version='1.0', # 版本号
&ensp; &ensp; packages=find_packages(), # 包括在安装包内的Python包
&ensp; &ensp; include_package_data=True, # 启用清单文件MANIFEST.in
&ensp; &ensp; exclude_package_date={'':['.gitignore']},
&ensp; &ensp; install_requires=[ # 依赖列表
&ensp; &ensp; 'Flask>=0.10',
&ensp; &ensp; 'Flask-SQLAlchemy>=1.5,<=2.1'
&ensp; &ensp; ]
)
无非就是import部分改为setuptools，当然setuptools最为增强集合，有很多特性，这里不详加赘述，也没完全了解，只是简单使用，具体可以看官网。

这里从一个标准式的python包来探讨开发一个标准python包里面应该包含哪些东西。
aws的boto3的python包的github
https://github.com/boto/boto3

准备开发一个标准python包，应该包含以下几部分，当然可增可少，但是大体是这样：
1.boto3文件夹   (源码目录)
2.scripts文件夹 (命令行工具文件夹)
3.docs文件夹    (介绍文档)
4.teset文件夹   (测试用例)
5.setup.py      (打包源码)
6.setup.cfg     (配置setpu.py一些参数，可要可不要)
7.MANIFEST.in   (打包时想引入一些非python文件时候用的，可以看一下这个文件它写了什么)
8.tox.ini        (tox是virtualenv管理器和命令行测试工具，主要是检查不同环境下运行你的测试代码，可要可不要)
9.一些txt文件    (包括LICENSE,requirements.txt等等说明文件)

以上就是要开发时候需要准备的东西，当然开发后，生成相应源码包也好或者轮子包给用户使用，就不需要像上面那么多，一切都是通过setup.py来描述最终源码包和轮子包具体包含哪些东西。
把上面clone下来：
生成源码包：
1.git clone https://github.com/boto/boto3
2.进入目录python setup.py sdist bdist_wheel
3.在dist目录下找到\*.tar.gz文件和\*.whl的包。
OK，当产生完这两个包，最终只需要上传到pypi上就可以了，用户即可通过pip install <packagename>使用你的包，至于如何上传，下一节会讲到。
附：python setup.py 有多个参数，
python setup.py sdist是产生源码包，可以添加--formats参数，默认--formats=gztar参数就是tar.gz的格式，
python setup.py bdist_wheel是产生whl包，也有一些参数，比如--universal就是表示纯python代码，支持python2和3，还有--platform表示非纯python代码，等等，具体可以看命令帮助或者官网。
python setup.py bdist_egg就是产生蟒蛇包了，当然一般也不用这个，现在都是前两个。
如果心有疑虑，想一探究竟这源码包和轮子包有什么不同，可以解压：
解压源码包，tar -xzf \*.tar.gz
![](https://wiki.chinanetcenter.com/html/doc//20190930/1569833662423image.png)
可以看到，这里所有的文件要嘛被描述在MANIFEST.in，要嘛被描述在setup.py中。
解压whl包，znzip \*.whl
![](https://wiki.chinanetcenter.com/html/doc//20190930/1569835067840image.png) 可以看到这边whl就比较少，因为whl偏向于只包含源码，最贴近环境，是为了安装而生的，pip install皆可，而源码包使用用户则需要先解压后再python setup.py install

 ## 开发阶段
 举个简单例子，这个例子是pypi上的
 https://packaging.python.org/tutorials/packaging-projects/：
packaging_tutorial/
&ensp; example_pkg/
&ensp; \_\_init\_\_.py
&ensp; setup.py
&ensp; LICENSE
&ensp; README.md
一个最基本的setup.py文件如下：
\#coding:utf8
import setuptools

with open("README.md", "r") as fh:
&ensp; &ensp; long_description = fh.read()

setuptools.setup(
&ensp; &ensp; name="example-pkg-your-username",
&ensp; &ensp; version="0.0.1",
&ensp; &ensp; author="Example Author",
&ensp; &ensp; author_email="author@example.com",
&ensp; &ensp; description="A small example package",
&ensp; &ensp; long_description=long_description,
&ensp; &ensp; long_description_content_type="text/markdown",
&ensp; &ensp; url="https://github.com/pypa/sampleproject",
&ensp; &ensp; packages=setuptools.find_packages(),
&ensp; &ensp; classifiers=[
&ensp; &ensp; &ensp; &ensp; "Programming Language :: Python :: 3",
&ensp; &ensp; &ensp; &ensp; "License :: OSI Approved :: MIT License",
&ensp; &ensp; &ensp; &ensp; "Operating System :: OS Independent",
&ensp; &ensp; ],
&ensp; &ensp; python_requires='>=3.6',
)

python3 setup.py sdist bdist_wheel就可以产生源码包和whl包
官网小例子只介绍产生源码包和whl包以及上传到pypi上，没有涉及开发阶段，因为我们在本地开发时候，难免代码需要调试，而调试是需要包安装在本地的，模拟用户使用场景。
当需要模拟用户使用包时候一般是python setup.py install 我们的包，这时候包是安装在site-package的目录下，这时候测试代码发现包的代码有错误需要修改，一种是进入这个site-package目录下去直接修改包内容，这种肯定不行因为我们本地代码有git，安装到site-package是没有git大量反复修改会比较麻烦，第二种是测试出现错误先卸载包，然后修改我们代码，重新安装，这种操作过于繁琐。所以这时候需要用到setup.py的开发模式，命令为python setup.py develop，这时候只是将你的代码软连接到site-package，你的本地代码修改会同步到site-package中，测试和修改无缝衔接。当需要关闭开发模式时候，python setup.py develop -u皆可。

 ## 上传pypi阶段
 这一步较为简单
注册pypi登录官网注册即可。
pip install twine
twine register dist/mypkg.whl 完成注册
twine upload dist/*  上传源码包和whl包

这边给出我的pypirc的配置，配合twine使用保存在~/.pypirc中
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = **
password = **

# 算法部分

## 排列组合和分布

**伯努利分布：**

伯努利分布指的是对于随机变量X有, 参数为p(0<p<1)，如果它分别以概率p和1-p取1和0为值。EX= p,DX=p(1-p)。伯努利试验成功的次数服从伯努利分布,参数p是试验成功的概率。

伯努利分布式一次实验的结果，是二项分布的特殊情况。
$$
Pr(X=1)=p,Pr(X=0)=1-p,0<p<1.
$$
这边Pr(X=1)表示事件"X=1"的概率，跟二项分布不太一样，如下

**二项分布：**
$$
X \sim B(n,p) \\
P(K=k)=C_n^kp^k(1-p)^{n-k},k=0,1,2,...,n
$$
这里K表示重复了n次实验的概率。其中
$$
C_n^k=\frac {n!}{k!(n-k)!}
$$
(引出排列组合公式推导：

排列数公式：

从n个不同元素中取出m(m≤n)个元素的所有不同排列的个数，叫做从n个不同元素中取出m个元素的排列数。
$$
A_n^m=n(n-1)(n-2)...(n-m+1)
$$
表示，规定0！=1。

组合数公式：

从n个不同元素中取出m(m≤n)个元素的所有不同组合的个数，叫做从n个不同元素中取出m个元素的组合数。
$$
C_n^m=\frac {A_n^m}{A_m^m}=\frac {n(n-1)(n-2)...(n-m+1)}{m!}=\frac {n!}{m!(n-m)!} \\
C_n^0=C_n^n=1
$$
这里可以比如袋子有3个球，记录着1,2,3号，

那么取出2个球的排列数有多少，则就是A<sub>3</sub><sup>2</sup>=6

就是(1,2),(1,3),(2,3),(2,1),(3,1),(3,2)，=3*2，表示第一位数有三种选择，在第一位数选中情况下，第二位数有2选择。而可以看到，**排列数是和顺序有关，组合数是和顺序无关**，如(1,2)和(2,1)在组合数看来是一样的，或者说是固定顺序的，固定顺序怎么理解，打个比方，比如从小到大顺序，在排列数取出后，按从小到大顺序取，则只有3种，(1,2),(1,3),(2,3)，当然固定顺序不一定是从小到大，比如从大到小，等等，

**其第一种理解为**：

1.把从n个不同元素中取出m个元素的排列数先找出来

2.由于每种排列数共有A<sub>m</sub><sup>m</sup>种排序方式，拿出固定的一种排序方式，即要除以A<sub>m</sub><sup>m</sup>，即得到这种排序的数目。
$$
C_3^2=\frac {A_3^2}{A_2^2}=\frac {3!}{k!(n-k)!}
$$
也是组合数问题。

**而下面的的多项分布的公式可以用第二种理解来解释**，二项分布只不过是多项分布一个例子：

还是以三颗球取两颗球组合数作为例子，原本三颗球编号为：[1,2,3]

1.三颗球排列方式有3！=6种排列方式，为(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)

2.这时候排列方式是以每个球是不同编码为基础的，即每颗球是标着1号，2号，3号，如果这时候是三颗球是两个1号，一个2号，即编号为:[1,2,1]，这时候排列方式是3种，为(1,2,1),(1,1,2),(2,1,1)。这时候把1看成正面，2看成负面，不就跟我们上面做了三次实验，两次为向上的次数一致情况了吗。

**即三颗球取两个球的组合数=三颗不同取值球排序/（有着两种取值(0,1)，并且取值为1个数为2)，是等价的**

这个思想在于，对于A<sub>n</sub><sup>n</sup>，它就表示有着球有n种取值方式的排列组合，但是如果实际球取值只有两种0和1,并且1重复次数为m，0重复次数就为n-m，那么：
$$
\frac {A_n^n=n!}{m!(n-m)!}
$$
解释为上面原本三种取值，取值不重复情况下，有(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)种

而当前取值有重复，1和3实际重复了，2保持不变，那么针对原本每一种可能即(1,2,3),（1,3,2）等，将三和1调换位置也是一样的结果，即实际(1,2,3)和(3,2,1)是重复，每一种都有2次重复，所以分母除以2！由来：
$$
\frac {3!}{2!(3-2)!}
$$
)

而二项分布为什么是组合数问题，举个例子，把上面的球换作做了三次实验，编号为1,2,3,实验结果为正概率为p，为负概率为1-p，即3次伯努利实验，这时候，实验的顺序是1,2,3，按照上面的解释，即从3种实验为2种为正的排列数：
$$
A_3^2=6
$$
由于要按照1,2,3的从小到大顺序，再除以
$$
A_2^2=2
$$
所以成了组合数问题。
$$
C_3^2=\frac {A_3^2}{A_2^2}=\frac {3!}{k!(n-k)!}
$$
**多项分布：**

多项分布式二项分布的推广，是指单次试验中随机变量的取值不再是0/1的，而是有多种离散值可能(1,2,3,...,k)。比如掷骰子，有6个面，N次试验结果服从K=6的多项分布。
$$
p(x1=m1,x2=m2,...,xk=mk,n,p1,p2,...,pk)=\frac {n!}{m1!m2!...mk!}p1^{m1}p2^{m2}...,pk^{mk} \\
K个离散值得概率满足\sum_{i=1}^kpi=1 \\
所有随机变量取值可能发现次数总和n\sum_{i=1}^kmi=n \\
随机变量取值k个，X=(x1,x2,...,xk),x1=m1,表示随机变量取x1时发生的次数
$$
所以上面的二项分布其实可以写成这样：
$$
p(1=m1(正面向上次数),0=m2(负面向上次数))=\frac {n!}{m1!(m2)!}p1^{m1}(1-p)^{m2} \\
因为m1+m2=n，所以写成
p(1=m1,0=m2)=\frac {n!}{m1!(n-m1)!}p1^{m1}(1-p)^{n-m1}
$$
**Beta分布：**

## 聚类算法：

### Kmeans：

### DBSCAN：

## P问题，NP问题，NP完全问题

这里可以看百度百科，里面介绍的很清楚，解释P问题，NP问题，NP完全问题（NP-C），先要了解一些概念，

多项式，时间复杂度

P类问题：存在多项式时间算法的问题。(P：polynominal，多项式)。

为什么研究这个，因为时间复杂度为o(n^2)和o(e^n)的算法，所需的运行次数简直是天壤之别，o(e^n)指数级的可能运行好几天都没法完成任务，所以我们才要研究一个问题是否存在多项式时间算法。而我们也只在乎一个问题是否存在多项式算法，因为一个时间复杂度比多项式算法还要复杂的算法研究起来是没有任何实际意义的。

NP类问题：能在多项式时间内验证得出一个正确解的问题。(NP:Nondeterministic polynominal，非确定性多项式)

P类问题是NP问题的子集，因为存在多项式时间解法的问题，总能在多项式时间内验证他。

注意定义，这里是验证。NP类问题，我用个人的俗话理解就是，不知道这个问题是不是存在多项式时间内的算法，所以叫non-deterministic非确定性，但是我们可以在多项式时间内验证并得出这个问题的一个正确解。

比如，找大[质数](https://baike.baidu.com/item/质数)的问题。有没有一个公式能推出下一个[质数](https://baike.baidu.com/item/质数)是多少呢？这种问题的答案，是无法直接计算得到的，只能通过间接的“猜算”来得到结果。这也就是非确定性问题。

（3）NPC类问题（Nondeterminism Polynomial complete）：存在这样一个NP问题，所有的NP问题都可以约化成它。换句话说，只要解决了这个问题，那么所有的NP问题都解决了。

“问题A可约化为问题B”有一个重要的直观意义：B的时间复杂度高于或者等于A的时间复杂度。也就是说，问题A不比问题B难。这很容易理解。既然问题A能用问题B来解决，倘若B的时间复杂度比A的时间复杂度还低了，那A的算法就可以改进为B的算法，两者的时间复杂度还是相同。正如解一元二次方程比解一元一次方程难，因为解决前者的方法可以用来解决后者。

**约化具有传递性。**如果能找到这样一个变化法则，对任意一个程序A的输入，都能按这个法则变换成程序B的输入，使两程序的输出相同，那么我们说，问题A可约化为问题B。当然，我们所说的“可约化”是指的可“多项式地”约化(Polynomial-time Reducible)，即变换输入的方法是能在多项式的时间里完成的。约化的过程只有用多项式的时间完成才有意义。

如果不断地约化上去，不断找到能“通吃”若干小NP问题的一个稍复杂的大NP问题，那么最后是否有可能找到一个时间复杂度最高，并且能“通吃”所有的 NP问题的这样一个超级NP问题？答案居然是肯定的。也就是说，存在这样一个NP问题，所有的NP问题都可以约化成它。换句话说，只要解决了这个问题，那么所有的NP问题都解决了。这种问题的存在难以置信，并且更加不可思议的是，这种问题不只一个，它有很多个，它是一类问题。这一类问题就是传说中的**NPC 问题**，也就是NP-完全问题：首先，它得是一个NP问题；然后，所有的NP问题都可以约化到它。  既然所有的NP问题都能约化成NPC问题，那么只要任意一个NPC问题找到了一个多项式的算法，那么所有的NP问题都能用这个算法解决了，NP也就等于P 了。因此，给NPC找一个多项式算法太不可思议了。因此，前文才说，“正是NPC问题的存在，使人们相信P≠NP”。我们可以就此直观地理解，**NPC问题目前没有多项式的有效算法，只能用指数级甚至阶乘级复杂度的搜索。**

**NP-Hard问题**：它满足NPC问题定义的第二条但不一定要满足第一条（就是说，NP-Hard问题要比 NPC问题的范围广）。NP-Hard问题同样难以找到多项式的算法，但它不列入我们的研究范围，因为它不一定是NP问题。即使NPC问题发现了多项式级的算法，NP-Hard问题有可能仍然无法得到多项式级的算法。事实上，由于NP-Hard放宽了限定条件，它将有可能比所有的NPC问题的时间复杂度更高从而更难以解决。

有了第一个NPC问题后，一大堆NPC问题就出现了，因为再证明一个新的NPC问题只需要将一个已知的NPC问题约化到它就行了。后来，Hamilton 回路成了NPC问题，TSP问题也成了NPC问题。现在被证明是NPC问题的有很多，任何一个找到了多项式算法的话所有的NP问题都可以完美解决了。因此说，正是因为NPC问题的存在，P=NP变得难以置信。P=NP问题还有许多有趣的东西，有待大家自己进一步的挖掘。攀登这个信息学的巅峰是我们这一代的终极目标。现在我们需要做的，至少是不要把概念弄混淆了。



## 贪心算法，分治算法，动态规划

先看来贪心算法的例子：

假设有如下课程，希望尽可能多的将课程安排在一间教室里：

| 课程   | 开始时间  | 结束时间  |
| ------ | --------- | --------- |
| 语文   | 9：00 AM  | 10：00 AM |
| 英语   | 9：30 AM  | 10：30 AM |
| 数学   | 10：00 AM | 11：00 AM |
| 计算机 | 10：30 AM | 11：30 AM |
| 体育   | 11：00 AM | 12：00 AM |

在这里只需要选择结束最早且和上一节课不冲突的课进行排序，因为每次都选择结束最早的，所以留给后面的时间也就越多，自然就能排下越多的课了。

每一节课的选择都是策略内的局部最优解(留给后面的时间最多)，所以最终的结果也是近似最优解(这个案例上就是最优解)。

背包问题：有一个背包，容量为35磅 ， 现有如下物品

| 课程       | 重量 | 价格 |
| ---------- | ---- | ---- |
| 吉他       | 15   | 1500 |
| 音响       | 30   | 3000 |
| 笔记本电脑 | 20   | 2000 |
| 显示器     | 29   | 2999 |
| 笔         | 1    | 200  |

要求达到的目标为装入的背包的总价值最大，并且重量不超出。

方便计算所以只有3个物品，实际情况可能是成千上万。

同上使用贪婪算法，因为要总价值最大，所以每次每次都装入最贵的,然后在装入下一个最贵的，选择结果如下：

选择: 音响 + 笔，总价值 3000 + 200 = 3200

并不是最优解: 吉他 + 笔记本电脑, 总价值 1500 + 2000 = 3500

当然选择策略有时候并不是很固定，可能是如下：

(1)每次挑选价值最大的,并且最终重量不超出：

选择: 音响 + 笔，总价值 3000 + 200 = 3200

(2)每次挑选重量最大的,并且最终重量不超出(可能如果要求装入最大的重量才会优先考虑)：

选择: 音响 + 笔，总价值 3000 + 200 = 3200

(3)每次挑选单位价值最大的(价格/重量),并且最终重量不超出：

选择: 笔+ 显示器，总价值 200 + 2999 = 3199

如上最终的结果并不是最优解，在这个案例中贪婪算法并无法得出最优解，只能得到近似最优解,也算是该算法的局限性之一。该类问题中需要得到最优解的话可以采取动态规划算法(后续更新，也可以关注我的公众号第一时间获取更新信息)。

## 正则化（L1,L2范数）

 https://www.cnblogs.com/zf-blog/p/6522502.html 

模型训练过程中，不知道哪些特征会游泳，于是找到尽可能多的特征去拟合训练数据，但是往往的结果是，会用上了一些不重要的特征，尽管在训练中表现良好，但是在测试集上效果不佳。因为模型中使用的某些特征，本身就不具备普适性。但你通过训练集，还是学习到它了，因为你的模型，想法设法地拟合了所有的样本点，自然而然地就会出来很多特征参数，如下图，第三幅图的模型复杂程度远大于第一幅。

y = tanh(w1x1 + w2x2 + w3x3 + w4x4)

如果想变弱或消除特征x3, 其实很简单的。直接添加一项 -w3*常数就会达到效果，对吗？yeah, 这样不就变弱特征x3的作用了吗。

其实还是不难理解的。

**相比L2，L1正则更可能使模型变稀疏？**：

L1就是对模型中每个特征取绝对值，L2取平方。

**如果施加 L1**，则新的函数为：Loss()+C|w|，要想消除这个特征的作用，只需要令 w = 0，使它取得极小值即可。

且可以证明：添加L1正则后 ，只要满足：

**系数 C 大于原函数在 0 点处的导数的绝对值，**

w = 0 就会变成一个极小值点。

证明过程如下，如上图所示，要想在0点处取得极小值，根据高数基本知识：

1) w小于0时，d(Loss)/d(w) - C 小于0

2) 且，w大于0时，d(Loss)/d(w) + C 大于0

上面两个式子同时满足，可以简写为：| d(Loss)/d(w) | < C, 得证。


## 马尔科夫模型和隐马尔科夫模型



马尔科夫链中，要求该过程具备"无记忆"的性质：下一个状态的概率分布只能有当前状态决定，在时间序列中它前面的时间均无关。在马尔可夫链的每一步，系统根据概率分布，可以从一个状态变到另一个状态，也可以保持当前状态。状态的改变叫做转移，与不同的状态改变相关的概率叫做转移概率。随机漫步就是马尔可夫链的例子。随机漫步中每一步的状态是在图形中的点，每一步可以移动到任何一个相邻的点，在这里移动到每一个点的概率都是相同的（无论之前漫步路径是如何的）。



## NLP

### VSM

向量空间模型(Vector Space Model,VSM)也就是单词向量空间模型，区别于LSA,PLSA,LDA这些话题向量空间模型， 但是单词向量空间模型和话题向量空间模型都属于词袋模型，又和word2vec等文本分布式表示方法相区别 。

 向量空间模型的基本想法是：给定一个文本，用一个向量表示该文本的语义，向量的每一维对应一个单词，其数值是该单词在该文本中出现的频数或Tf-Idf。那么每个文本就是一个向量，特征数量为所有文本中的单词总数，通过计算向量之间的余弦相似度可以得到文本的相似度。 

 而文本集合中的所有文本的向量就会构成一个单词-文本矩阵，元素为单词的频数或Tf-Idf 

### Word2Vec

NLP（自然语言处理）里面，最细粒度的是 词语，词语组成句子，句子再组成段落、篇章、文档。所以处理 NLP 的问题，首先就要拿词语开刀。词语，是人类的抽象总结，是符号形式的（比如中文、英文、拉丁文等等），所以需要把他们转换成数值形式，或者说——嵌入到一个数学空间里，这种嵌入方式，就叫词嵌入（word embedding)，而 Word2vec，就是词嵌入（ word embedding) 的一种。简单点来说就是把一个词语转换成对应向量的表达形式，来让机器读取数据。



www.cnblogs.com/Luv-GEM/p/10888026.html 


# 深度学习

## 梯度下降

