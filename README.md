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

## 概率分布和概率密度

 https://www.jianshu.com/p/0cfc3204af77 

## BERT模型原理

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

## LDA主题发现：

## EM算法：

似然函数：

在数理统计学中，似然函数是一种关于统计模型中的参数的函数，表示模型参数中的似然性。

 给定输出x时，关于参数θ的似然函数L(θ|x)（在数值上）等于给定参数θ后变量X的概率： 
$$
L(\theta|x)=P(X=x|\theta)
$$
其中， 表示X取x时的概率。上式常常写为 或者 。需要注意的是，此处并非条件概率，因为θ不（总）是随机变量。

## 统计语言模型：

假定S表示某一个有意义的句子，由一连串特定顺序排列的词w1,w2,...wn组成，n为句子的长度。现在想知道S在文本中出现的可能性，即P(S)。此时需要有个模型来估算，不妨把P(S)展开表示为P(S)=P(w1,w2,...,wn)。利用条件概率的公式，S这个序列出现的概率等于每一个词出现的条件概率相乘，于是P(w1,w2,...,wn)可展开为：
 P(w1,w2,...wn)=P(w1)P(w2|w1)P(w3|w1,w2)...P(wn|w1,w2,...,wn-1) 

 其中P(w1)表示第一个词w1出现的概率；P(w2|w1)是在已知第一个词的前提下，第二个词出现的概率；以此类推 。 显然，当句子长度过长时，P(wn|w1,w2,...,wn-1)的可能性太多，无法估算，俄国数学家马尔可夫假设任意一个词wi出现的概率只同它前面的词wi-1有关，这种假设成为马尔可夫假设，S的概率变为 

 P(S)=P(w1)P(w2|w1)P(w3|w2)...P(wi|wi-1)...P(wn|wn-1) 

 其对应的统计语言模型就是二元模型。也可以假设一个词由前面N-1个词决定，即N元模型。当N=1时，每个词出现的概率与其他词无关，为一元模型，对应S的概率变为 

P(S)=P(w1)P(w2)P(w3)...P(wi)...P(wn)

当N=3时，每个词出现的概率与其前两个词相关，为三元模型，对应S的概率变为

P(S)=P(w1)P(w2|w1)P(w3|w1,w2)...P(wi|wi-2,wi-1)...P(wn|wn-2,wn-1)

维基百科是最常用且权威的开放网络数据集之一，作为极少数的人工编辑、内丰富、格式规范的文本语料，各类语言的维基百科在NLP等诸多领域应用广泛。下载地址为

https://dumps.wikimedia.org/zhwiki/20190301/zhwiki-20190301-pages-articles.xml.bz2。维基百科提供的语料是xml格式的，因此需要将其转换为txt格式。由于维基百科中有很多是繁体中文网页，故需要将这些繁体字转换为简体字，采用opencc第三方库进行繁简转换。本文的统计语言模型都是基于词的，所以需要对中文句子进行分词，采用Jieba中文分词工具对句子进行分词[5]。

由于一元模型不需要考虑上下文关系，所以其读取语料的方式与二元模型和三元模型不一样，直接采用Gensim的数据抽取类WikiCorpus对xml文件进行抽取，它能够去掉文本中的所有标点，留下中文字符和utf-8编码下字节数为1的标点符号，去掉这些符号后再进行繁简转换和分词，得到所需要的txt格式语料库。

二元模型和三元模型需要考虑上下文关系，不能直接去掉所有标点符号得到无分隔的语料。通过bz2file不解压读取语料，再利用Gensim的extract_pages类来提取每个页面[6]，此时得到的语料相比利用WikiCorpus得到的语料多了一些英文字符和中文标点符号，通过建立一个停用符号表和正则表达式两种方式清理语料，进行繁简转换和分词之后得到以一句一行的txt格式语料库。 

## 有限自动状态机(DFA，敏感词过滤)：

 https://blog.csdn.net/liangyihuai/article/details/82261978 

 https://blog.csdn.net/chenjiayi_yun/article/details/51699923 

 https://blog.csdn.net/tomato8524/article/details/7566275 

 https://www.cnblogs.com/twoheads/p/11349541.html 

## AC自动机算法(敏感词过滤，多模匹配)：

 https://github.com/eachain/aca 

 [https://ouuan.github.io/AC%E8%87%AA%E5%8A%A8%E6%9C%BA%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/](https://ouuan.github.io/AC自动机学习笔记/) 

 [http://xiaorui.cc/2014/09/21/python%e4%b8%8b%e7%9a%84ahocorasick%e5%ae%9e%e7%8e%b0%e5%bf%ab%e9%80%9f%e7%9a%84%e5%85%b3%e9%94%ae%e5%ad%97%e5%8c%b9%e9%85%8d/](http://xiaorui.cc/2014/09/21/python下的ahocorasick实现快速的关键字匹配/) 

## 关联规则算法(Apriori)：

 https://blog.csdn.net/qq_36523839/article/details/82191677 

## 关联规则算法(prefixspan)：

 https://github.com/chuanconggao/PrefixSpan-py 

 https://github.com/ICDI0906/PrefixSpan/blob/master/PrefixSpan.pdf 

## 字符串相似度：

 https://www.cnblogs.com/huilixieqi/p/6493089.html 

 https://www.cnblogs.com/lishanyang/p/6016737.html 

pip install python-Levenshtein

个人总结的 关于 Levenshtein 所有函数的用法 和 注释

apply_edit()  #根据第一个参数editops（）给出的操作权重，对第一个字符串基于第二个字符串进行相对于权重的操作

distance() #计算2个字符串之间需要操作的绝对距离

editops() #找到将一个字符串转换成另外一个字符串的所有编辑操作序列

hamming() #计算2个字符串不同字符的个数，这2个字符串长度必须相同

inverse() #用于反转所有的编辑操作序列

jaro() #计算2个字符串的相识度，这个给与相同的字符更高的权重指数

jaro_winkler() #计算2个字符串的相识度，相对于jaro 他给相识的字符串添加了更高的权重指数，所以得出的结果会相对jaro更大（%百分比比更大）

matching_blocks() #找到他们不同的块和相同的块，从第六个开始相同，那么返回截止5-5不相同的1，第8个后面也开始相同所以返回8-8-1，相同后面进行对比不同，最后2个对比相同返回0

median() #找到一个列表中所有字符串中相同的元素，并且将这些元素整合，找到最接近这些元素的值，可以不是字符串中的值。

median_improve() #通过扰动来改进近似的广义中值字符串。

opcodes() #给出所有第一个字符串转换成第二个字符串需要权重的操作和操作详情会给出一个列表，列表的值为元祖，每个元祖中有5个值
    #[('delete', 0, 1, 0, 0), ('equal', 1, 3, 0, 2), ('insert', 3, 3, 2, 3), ('replace', 3, 4, 3, 4)]
    #第一个值是需要修改的权重，例如第一个元祖是要删除的操作,2和3是第一个字符串需要改变的切片起始位和结束位，例如第一个元祖是删除第一字符串的0-1这个下标的元素
    #4和5是第二个字符串需要改变的切片起始位和结束位，例如第一个元祖是删除第一字符串的0-0这个下标的元素，所以第二个不需要删除

quickmedian() #最快的速度找到最相近元素出现最多从新匹配出的一个新的字符串

ratio() #计算2个字符串的相似度，它是基于最小编辑距离

seqratio() #计算两个字符串序列的相似率。

setmedian() #找到一个字符串集的中位数(作为序列传递)。 取最接近的一个字符串进行传递，这个字符串必须是最接近所有字符串，并且返回的字符串始终是序列中的字符串之一。

setratio() #计算两个字符串集的相似率(作为序列传递)。

subtract_edit() #从序列中减去一个编辑子序列。看例子这个比较主要的还是可以将第一个源字符串进行改变，并且是基于第二个字符串的改变，最终目的是改变成和第二个字符串更相似甚至一样
 https://www.jianshu.com/p/06370a33e1ee 

 https://blog.csdn.net/xiao1_1bing/article/details/86374341 

## 决策树：

 决策树是一种机器学习的方法。决策树的生成算法有ID3, C4.5和C5.0等 

 ID3：特征划分基于信息增益 

 C4.5：特征划分基于信息增益比 

 CART：特征划分基于基尼指数 







三种的不同之处：

 https://blog.csdn.net/songhao22/article/details/82727028 

### CART分类：

CART的生成算法：
输入：训练数据集D，停止计算条件

输出：CART决策树

根据训练数据集，从根节点开始，递归地对每个节点进行以下操作，构建二叉决策树：

（1）设结点的训练数据集为D，计算现有特征对该数据集的基尼指数。此时，对每一个特征A,对其可能取的每一个值a,根据样本点对A=a的测试为“是”或“否”将D分割为D1和D2两部分，利用式（5）计算A=a时的基尼指数。

（2）在所有可能的特征A以及它们可能的切分点a中，选择基尼指数最小的特征及其对应的切分点作为最优特征与最优切分点，依最优特征与最优切分点，从现结点生成两个子结点，将训练数据依特征分配到两个子节点中去。

（3）对两个子节点递归地调用（1）（2），直至满足停止条件。

（4）生成CART决策树。

### CART回归：

 决策树的生成就是递归地构建二叉决策树的过程，对回归树用平方误差最小化准则，对分类树用基尼指数最小化准则，进行特征选择，生成二叉树。 

1.选择最优切分变量j与切分点s，求解：
$$
\min\limits_{j,s}[\min\limits_{c1} \sum\limits_{x_i\in R_i(j,s)}(y_i-c_1)^2+\min\limits_{c2}\sum\limits_{x_i\in R_i(j,s)}(y_i-c_2)^2]
$$
 遍历变量j，对固定的切分变量j扫描切分点s，选择使上式取得最小值的对(j,s)。其中Rm是被划分的输入空间，Cm空间Rm对应的输出值。 

2.用选定的对(j,s)划分区域并决定相应的输出值：
$$
R_1(j.s)=\{x|x^(j)\leq s\},R_1(j.s)=\{x|x^(j)> s\}
$$

$$
\hat{c}=\frac {1}{N_m}\sum\limits_{x_i\in R_i(j,s)}y_i,x\in R_m,m=1,2
$$

3.继续对两个子区域调用步骤1，直至满足停止条件。

4.将输入控件划分为M个区域R1,R2....Rm生成决策树：
$$
f(x)=\sum\limits_{m=1}^{M}\hat{c}I(x \in R)
$$
例子1：

 训练数据见下表，x的取值范围为区间[0.5,10.5]，y的取值范围为区间[5.0,10.0]，学习这个回归问题的最小二叉回归树。 

| 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 5.56 | 5.70 | 5.91 | 6.40 | 6.80 | 7.05 | 8.90 | 8.70 | 9.00 | 9.05 |

 求解训练数据的切分点s: 
$$
R_1(j.s)=\{x|x^(j)\leq s\},R_1(j.s)=\{x|x^(j)> s\}
$$
 容易求得在R1、R2内部使得平方损失误差达到最小值的c1、c2为： 
$$
C_1=\frac {1}{N_1}\sum\limits_{x \in R_1}y_i,C_2=\frac {1}{N_2}\sum\limits_{x \in R_2}y_i
$$
**(这边的C1,C2其实就是就是回归预测时的值，自己认为)**

这里N1、N2是R1、R2的样本点数。

求训练数据的切分点，根据所给数据，考虑如下切分点：

1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5。

对各切分点，不难求出相应的R1、R2、c1、c2及
$$
m(s)=\min\limits_{j,s}[\min\limits_{c1} \sum\limits_{x_i\in R_i(j,s)}(y_i-c_1)^2+\min\limits_{c2}\sum\limits_{x_i\in R_i(j,s)}(y_i-c_2)^2]
$$
例如，当s=1.5时，R1={1}，R2={2,3,...,10}，c1=5.56，c2=7.50，则
$$
m(s)=\min\limits_{j,s}[\min\limits_{c1} \sum\limits_{x_i\in R_i(j,s)}(y_i-c_1)^2+\min\limits_{c2}\sum\limits_{x_i\in R_i(j,s)}(y_i-c_2)^2]=0+15.72=15.72
$$
 现将s及m(s)的计算结果列表如下： 

| s    | 1.5   | 2.5   | 3.5  | 4.5  | 5.5  | 6.5  | 7.5  | 8.5   | 9.5   |
| ---- | ----- | ----- | ---- | ---- | ---- | ---- | ---- | ----- | ----- |
| m(s) | 15.72 | 12.07 | 8.36 | 5.78 | 3.91 | 1.93 | 8.01 | 11.73 | 15.74 |

 由上表可知，当x=6.5的时候达到最小值，此时R1={1,2,...,6}，R2={7,8,9,10}，c1=6.24，c2=8.9，所以回归树T1(x)为： 
$$
T_1(x)=\begin{cases}
6.24& {x < 6.5}\\
8.91& {x \geq 6.5}
\end{cases}
$$

$$
f_1(x)=T_1(x)
$$

注意：以下原作者给出的例子中涉及到“残差”的部分，应当是GBDT求损失函数的一阶导函数得出的，非CART所用到的方法。

CART: 树的根节点分成2支后，再分别在这2支上做分支，以此递推，最终生成一颗完整的决策树；后续再剪枝等；

GBDT：获得一颗二叉树后，利用残差，再在完整的数据集上生成一颗二叉树，最终将多颗二叉树加权累加组成一个最终的函数。

故，本例实际上讲的是GBDT,请再参考：

 https://blog.csdn.net/openSUSE1995/article/details/77542330

  用f1(x)拟合训练数据的残差见下表，表中r2i=yi-f1(xi),i=1,2,...,10 

| 1     | 2     | 3     | 4    | 5    | 6    | 7     | 8     | 9    | 10   |
| ----- | ----- | ----- | ---- | ---- | ---- | ----- | ----- | ---- | ---- |
| -0.68 | -0.54 | -0.33 | 0.16 | 0.56 | 0.81 | -0.01 | -0.21 | 0.09 | 0.14 |

 第2步求T2(x)方法与求T1(x)一样，只是拟合的数据是上表的残差，可以得到： 
$$
T_2(x)=\begin{cases}
-0.52& {x < 3.5}\\
0.22& {x \geq 3.5}
\end{cases}
$$

$$
f_2(x)=f_1(x)+T_2(x)=\left\{
\begin{array}{rcl}
5.72       &      & {x      <      3.5}\\
6.46     &      & {3.5 \leq x < 6.5}\\
9.13     &      & {x \geq 6.5}\\
\end{array} \right.
$$

 继续求得 :
$$
T_3(x)=\begin{cases}
0.15& {x < 6.5}\\
-0.22& {x \geq 6.5}
\end{cases},L(y,f3(x))=0.47
$$

$$
T_4(x)=\begin{cases}
-0.16& {x < 4.5}\\
0.11& {x \geq 4.5}
\end{cases},L(y,f4(x))=0.30
$$

$$
T_5(x)=\begin{cases}
0.07& {x < 6.5}\\
-0.11& {x \geq 6.5}
\end{cases},L(y,f5(x))=0.23
$$

$$
T_6(x)=\begin{cases}
-0.15& {x < 2.5}\\
0.04& {x \geq 2.5}
\end{cases}
$$

$$
f_6(x)=f_5(x)+T_6(x)=T_1(x)+...+T_5(x)+T_6(x)=\left\{
\begin{array}{rcl}
5.63       &      & {x      <      2.5}\\
5.82     &      & {2.5 \leq x < 3.5}\\
6.56     &      & {3.5 \leq x < 4.5}\\
6.83     &      & {4.5 \leq x < 6.5}\\
8.95     &      & {x \geq 6.5}\\
\end{array} \right.
$$

可以用拟合训练数据的平方损失误差等来作为结束条件。此时 
$$
L(y,f_6(x))=\sum\limits_{i=1}^{10}(y_i-f_6(x_i))^2=0.71
$$
 假设此时已经满足误差要求，那么f(x)=f6(x)即为所求的回归树。 

参考链接：

 https://blog.csdn.net/aaa_aaa1sdf/article/details/81588382 

https://www.zhihu.com/question/51012842 

 https://blog.csdn.net/zhihua_oba/article/details/72230427 

 https://blog.csdn.net/haizhiguang/article/details/82587322 

 https://blog.csdn.net/gyq423/article/details/82147000 

 https://zhuanlan.zhihu.com/p/30059442 

## GBDT(GradientBoostingDecisionTree）：

GBDT (Gradient Boosting Decision Tree) 梯度提升迭代决策树。GBDT 也是 Boosting 算法的一种，但是和 AdaBoost 算法不同（AdaBoost 算法上一篇文章已经介绍）；区别如下：AdaBoost 算法是利用前一轮的弱学习器的误差来更新样本权重值，然后一轮一轮的迭代；GBDT 也是迭代，但是 GBDT 要求弱学习器必须是 CART 模型，而且 GBDT 在模型训练的时候，是要求模型预测的样本损失尽可能的小。 

 https://www.jianshu.com/p/405f233ed04b 

 https://zhuanlan.zhihu.com/p/30339807 

 https://www.jianshu.com/p/b90a9ce05b28 

## 随机森林(Random Forest，RF)



## 聚类算法：

### Kmeans：

```
from sklearn.cluster import KMeans
X = np.array([[1,1],[1,-1],[-1,1],[-1,-1],[1.41,0],[-1.41,0],[0,1.41],[0,-1.41],[2,2],[2,-2],[-2,2],[-2,-2],[2.82,0],[-2.82,0],[0,2.82],[0,-2.82]])
#plt.scatter(X[:, 0], X[:, 1], marker='o')
y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
```



### DBSCAN：

https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/

可视化的DBSCAN

基本概念：

 （1）Eps邻域：给定对象半径Eps内的邻域称为该对象的Eps邻域 

 （2）核心点（core point）：如果对象的Eps邻域至少包含最小数目MinPts的对象，则称该对象为核心对象; 

 （3）边界点（edge point）：边界点不是核心点，但落在某个核心点的邻域内; 

 （4）噪音点（outlier point）：既不是核心点，也不是边界点的任何点; 

 （5）直接密度可达(directly density-reachable)：给定一个对象集合D，如果p在q的Eps邻域内，而q是一个核心对象，则称对象p从对象q出发时是直接密度可达的; 

 （6）密度可达(density-reachable)：如果存在一个对象链 p1, …,pi,.., pn，满足p1 = p 和pn = q，pi是从pi+1关于Eps和MinPts直接密度可达的，则对象p是从对象q关于Eps和MinPts密度可达的; 

 （7）密度相连(density-connected)：如果存在对象O∈D，使对象p和q都是从O关于Eps和MinPts密度可达的，那么对象p到q是关于Eps和MinPts密度相连的。 

 （8）类（cluster）:设非空集合,若满足： 

图“直接密度可达”和“密度可达”概念示意描述。根据前文基本概念的描述知道：由于有标记的各点­M、P、O和R的Eps近邻均包含3个以上的点，因此它们都是核对象；M­是从P“直接密度可达”；而Q则是从­M“直接密度可达”；基于上述结果，Q是从P“密度可达”；但P从Q无法“密度可达”(非对称)。类似地，S和R从O是“密度可达”的；O、R和S均是“密度相连”（对称）的。

总结：半径越大，需要对应minpts也越多才行，极端情况就是，半径很大，minpts小，簇变成一个，所有点彼此都是密度直达点或者密度可达点。

半径描述的形成簇的多少，minpts描述的是簇内稠密的程度。

轮廓系数：
$$
C_3^2=\frac {A_3^2}{A_2^2}=\frac {3!}{k!(n-k)!}
$$


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


# 深度学习

## 梯度下降

## 卷积

我推荐用**复利**的例子来理解卷积可能更好理解一些：

小明存入100元钱，年利率是5%，按复利计算（即将每一年所获利息加入本金，以计算下一年的利息），那么在五年之后他能拿到的钱数是100(1+5%)^5，如下表所示：

| 本金 | 第一年         | 第二年         | 第三年         | 第四年         | 第五年         |
| ---- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 100  | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 | 100*（1.05）^4 | 100*（1.05）^5 |

   将这笔钱存入银行的一年之后，小明又往银行中存入了100元钱，年利率仍为5%，那么这笔钱按复利计算，到了第五年，将收回的钱数是100(1+5%)^5，我们将这一结果作为新的一行加入上面的表格中： 

| 本金 | 第一年         | 第二年         | 第三年         | 第四年         | 第五年         |
| ---- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 100  | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 | 100*（1.05）^4 | 100*（1.05）^5 |
|      | +100           | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 | 100*（1.05）^4 |

 以此类推，如果小明每年都往银行中存入新的100元钱，那么这个收益表格将是这样的： 

| 本金 | 第一年         | 第二年         | 第三年         | 第四年         | 第五年         |
| ---- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 100  | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 | 100*（1.05）^4 | 100*（1.05）^5 |
|      | +100           | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 | 100*（1.05）^4 |
|      |                | +100           | 100*（1.05）^1 | 100*（1.05）^2 | 100*（1.05）^3 |
|      |                |                | +100           | 100*（1.05）^1 | 100*（1.05）^2 |
|      |                |                |                | +100           | 100*（1.05）^1 |
|      |                |                |                |                | +100           |

 可见，最终小明拿到的钱将等于他各年存入的钱分别计算复利之后得到的钱数的总和，即： 

 用求和符号来简化这个公式，可以得到： 
$$
\sum\limits_{i=0}^{5}f(i)g(5-i)=where f(i)=100,g(5-i)=(1.05)^{5-i}
$$
在上式中，f(i)为小明的存钱函数，而g(i)为存入银行的每一笔钱的复利计算函数，在这里，小明最终得到的钱就是他的存钱函数和复利计算函数的卷积 为了更清晰地看到这一点，我们将这个公式推广到连续的情况，也就是说，小明在从 0到t的这一段时间内，每时每刻都都往银行存钱，他的存钱函数为：
$$
f(\tau)(0<=\tau<=t)
$$
而银行对他存入的每一笔钱都按复利计算公式收益：
$$
g(t-\tau)=(1+5\%)^{t-\tau}
$$
则小明到时间t将得到的总钱数为：
$$
\int_{-0}^{t} f(\tau)g(t-\tau)\, d\tau=\int_{-0}^{t} f(\tau)(1+5\%)^{t-\tau}\, d\tau
$$
 如果我们将小明的存款函数视为一个**信号发生（也就是激励）**的过程，而将复利函数  视为一个**系统对信号的响应函数（也就是响应）**，那么二者的卷积 就可以看做是在 t时刻 对系统进行观察，**得到的观察结果（也就是输出）**将是过去产生的所有信号经过系统的「处理／响应」后得到的结果的**叠加，**这也就是**卷积的物理意义**了 

## NLP

### VSM

向量空间模型(Vector Space Model,VSM)也就是单词向量空间模型，区别于LSA,PLSA,LDA这些话题向量空间模型， 但是单词向量空间模型和话题向量空间模型都属于词袋模型，又和word2vec等文本分布式表示方法相区别 。

 向量空间模型的基本想法是：给定一个文本，用一个向量表示该文本的语义，向量的每一维对应一个单词，其数值是该单词在该文本中出现的频数或Tf-Idf。那么每个文本就是一个向量，特征数量为所有文本中的单词总数，通过计算向量之间的余弦相似度可以得到文本的相似度。 

 而文本集合中的所有文本的向量就会构成一个单词-文本矩阵，元素为单词的频数或Tf-Idf 

### Word2Vec

NLP（自然语言处理）里面，最细粒度的是 词语，词语组成句子，句子再组成段落、篇章、文档。所以处理 NLP 的问题，首先就要拿词语开刀。词语，是人类的抽象总结，是符号形式的（比如中文、英文、拉丁文等等），所以需要把他们转换成数值形式，或者说——嵌入到一个数学空间里，这种嵌入方式，就叫词嵌入（word embedding)，而 Word2vec，就是词嵌入（ word embedding) 的一种。简单点来说就是把一个词语转换成对应向量的表达形式，来让机器读取数据。



www.cnblogs.com/Luv-GEM/p/10888026.html 

## 图像特征

### HOG特征，LBP特征，Haar特征

 http://shartoo.github.io/HOG-feature/ 

 https://zhuanlan.zhihu.com/p/94934407 

HOG特征即 Histogram of oriented gradients，源于2005年一篇[CVPR论文](https://hal.inria.fr/file/index/docid/548512/filename/hog_cvpr2005.pdf)，使用HOG+SVM做行人检测，由于效果良好而被广泛应用。大体效果如下，具体使用HOG+SVM做行人检测时再讨论详细代码。 

算法计算步骤概览

1.图像预处理。`伽马矫正`(减少光度影响)和`灰度化`(也可以在RGB图上做，只不过对三通道颜色值计算，取梯度值最大的)【可选步骤】

2.计算图像像素点梯度值，得到梯度图(尺寸和原图同等大小)

3.图像划分多个cell，统计cell内梯度直方向方图

4.将2×22×2个cell联合成一个block,对每个block做块内梯度归一

### 1 图像预处理

#### 1.1 gamma矫正和灰度化

**作用**：gamma矫正通常用于电视和监视器系统中重现摄像机拍摄的画面．在图像处理中也可用于调节图像的对比度，减少图像的光照不均和局部阴影． **原理**： 通过非线性变换，让图像从暴光强度的线性响应变得更接近人眼感受的响应，即将漂白（相机曝光）或过暗（曝光不足）的图片，进行矫正

gamma矫正公式：
$$
f(x)=x^\gamma
$$
即输出是输入的幂函数，指数为γ

```
import cv2
import numpy as np
img = cv2.imread('gamma0.jpg',0)
img1 = np.power(img/float(np.max(img)), 1/1.5)
img2 = np.power(img/float(np.max(img)), 1.5)
cv2.imshow('src',img)
cv2.imshow('gamma=1/1.5',img1)
cv2.imshow('gamma=1.5',img2)
cv2.waitKey(0)
```

 下图分别代表了处理之后的`原图`,`灰度图`，`gamma=1/1.5矫正`,`gamma=1.5矫正` 

![hog2](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_2.jpg?raw=true)

### 2 计算图像像素梯度图

 我们需要同时计算图像的`水平梯度图`和`垂直梯度图` 。如下图，假设我们要计算下图中像素点A的梯度值 

![hog3](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_3.jpg?raw=true)

 计算方法为 

 **梯度大小** 

 水平梯度： 
$$
g_x=\sqrt{(L(x-1,y)-L(x+1,y))^2}=\sqrt{(30-20)^2}=\sqrt{(10)^2}=10
$$
垂直梯度：
$$
g_y=\sqrt{(L(,y+1)-L(x,y-1))^2}=\sqrt{(32-64)^2}=\sqrt{(32)^2}=32
$$
梯度方向：
$$
\theta(x,y)=arctan[\frac {g_x} {g_y}]=arctan[\frac {10} {32}]
$$
梯度方向会取绝对值，因此得到的角度范围是 [0,180]

上面这些计算过程，在opencv中有对应的算子，称为Sobel算子，分别计算水平和垂直方向梯度的。

![hog4](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_4.jpg?raw=true)

```
im = cv2.imread('bolt.png')
im = np.float32(im) / 255.0
 
# 计算梯度
img = cv2.G
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
# 计算梯度幅度和方向
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
cv2.imshow("absolute x-gradient",gx)
cv2.imshow("absolute y-gradient",gy)
cv2.imshow("gradient magnitude",mag)
cv2.imshow("gradient direction",angle)
cv2.waitKey(0)
```

效果如下，分别为`原图`,`x方向梯度绝对值`,`y方向梯度绝对值图`,`梯度幅度图`,`梯度方向图` **下图是没有使用归一化效果**

![hog5](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_5.jpg?raw=true)

 **使用归一化之后的效果** 

![hog6](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_6.jpg?raw=true)

可以看到

1.x方向梯度图会强化垂直方向的特征，可以观察到左侧白色斜线更加明显，但是底部一些水平线没有了。

2.y方向梯度图会强化水平方向特征，底部水平线强化了，左侧垂直线不是那么明显了。

梯度图移除了大量非显著性特征，并加强了显著特征。三通道的彩色图中，每个像素的梯度幅度是三个通道中最大的那个，而梯度方向是梯度幅度最大的那个通道上的方向。 

### 3 计算梯度直方图

过上一步计算之后，每个像素点都会有两个值：**梯度方向和梯度幅度**。

但是，也看到了，梯度幅度和梯度方向图与原图等同大小，实际如果使用这些特征，会存在两个问题

- 计算量很大，基本就是原图
- 特征稀疏。图中其实只有少量稀疏的显著特征，大部分可能是0

以上是个人理解。

HOG特征在此步骤选择联合一个8×8的小格子内部一些像素，计算其梯度幅度和梯度方向的统计直方图，这样一来就可以以这个梯度直方图来代替原本庞大的矩阵。每个像素有一个梯度幅度和梯度方向两个取值，那么一个8×8的小格子一共有8×8×2=128个取值。

上面提到，梯度方向取值范围是[0,180]，以每20°为一个单元，所有的梯度方向可以划分为9组，这就是统计直方图的分组数目。如下图，我们选取划分格子之后的第二行第二列一个小单元，计算得到右边的梯度方向图和梯度幅度图，同时以以梯度方向为index，统计分组数量。

![hog7](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_7.jpg?raw=true)

 得到的统计频率直方图如下 :

![hog8](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_8.jpg?raw=true)

 从上图可以看到，更多的点的梯度方向是倾向于0度和160度，也就是说这些点的梯度方向是向上或者向下，表明图像这个位置存在比较明显的横向边缘。因此HOG是对边角敏感的，由于这样的统计方法，也是对部分像素值变化不敏感的，所以能够适应不同的环境。 

 至于为什么选取8×8为一个单元格，是因为HOG特征当初设计时是用来做行人检测的。在行人图片中8×8的矩阵被缩放成64×128的网格时，足以捕获一些特征，比如脸部或者头部特征等。 

### 4 block归一化

 目的：降低光照的影响 方法：向量的每一个值除以向量的模长 

 比如对于一个(128,64,32)的三维向量来说，模长是：
$$
\sqrt{(128)^2+(64)^2+(32)^2}=146.64
$$
 那么归一化后的向量变成 (0.87,0.43,0.22)

 HOG在选取8×8为一个单元格的基础之上，再以2×2个单元格为一组，称为block。作者提出要对block进行归一化，由于每个单元格cell有9个向量，2×2个单元格则有36个向量，需要对这36个向量进行归一化。下图演示了如何在图像中抽取block 

![hog9](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_9.jpg?raw=true)

### 5 HOG特征描述

每一个16×16大小的block将会得到36大小的vector。那么对于一个64×128大小的图像，按照上图的方式提取block，将会有7个水平位置和15个竖直位可以取得，所以一共有7×15=105个block，所以我们整合所有block的vector，形成一个大的一维vector的大小将会是36×105=3780。

### 6 参考代码

 计算图像HOG特征时，我们使用如下代码 

```
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
image = cv2.imread('C:/Users/dell/Desktop/123.png')
fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
plt.show()
```

 效果如下 ：

![hog10](https://github.com/wangjm12138/python_other_script/blob/master/picture/hog_feature_10.jpg?raw=true)

## 目标检测Yolov3：

## 目标跟踪的介绍

 https://blog.csdn.net/weixin_36836622/article/details/85644377 



## 目标跟踪KCF(判别式的跟踪)

 https://blog.csdn.net/crazyice521/article/details/53525366 

kernel correlaion filter核相关滤波算法。

主页 http://www.robots.ox.ac.uk/~joao/circulant/index.html 

