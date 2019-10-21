# Python 模块

## 面向对象理解

<https://www.jianshu.com/p/2e2ee316cfd0>

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


## 马尔科夫模型和隐马尔科夫模型



马尔科夫链中，要求该过程具备"无记忆"的性质：下一个状态的概率分布只能有当前状态决定，在时间序列中它前面的时间均无关。在马尔可夫链的每一步，系统根据概率分布，可以从一个状态变到另一个状态，也可以保持当前状态。状态的改变叫做转移，与不同的状态改变相关的概率叫做转移概率。随机漫步就是马尔可夫链的例子。随机漫步中每一步的状态是在图形中的点，每一步可以移动到任何一个相邻的点，在这里移动到每一个点的概率都是相同的（无论之前漫步路径是如何的）。








# 深度学习

## 梯度下降

