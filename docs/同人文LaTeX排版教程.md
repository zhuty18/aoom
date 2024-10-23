---
title: 同人文LaTeX排版教程
tags: FIN
layout: latex
no_nav: true
---

本文为懂得$\LaTeX$基础命令、语法，准备以此为排版工具，制作**中文同人文本**的玩家撰写。适用于**纯文本**或**图文本的纯文字部分**排版，考虑了中英文掺杂的情况。有少量场景与操作系统有关，本文暂只有windows的解决方案。

其中不包含$\LaTeX$安装、运行、命令解释、文档阅读等入门内容。这部分教程在网上已经很多，不需要我再抄一遍。

- [$\\LaTeX$的优点](#latex的优点)
  - [代码式编辑](#代码式编辑)
  - [默认细节极佳](#默认细节极佳)
  - [模板化](#模板化)
- [排版参数](#排版参数)
  - [小说](#小说)
  - [同人文学](#同人文学)
  - [进阶知识](#进阶知识)
- [字体设定](#字体设定)
  - [字体入门](#字体入门)
    - [字体类别](#字体类别)
    - [字体风格](#字体风格)
  - [`ctex`包介绍](#ctex包介绍)
  - [字体名称查询](#字体名称查询)
  - [外语字符字体配置](#外语字符字体配置)
    - [连字](#连字)
  - [中文字符字体配置](#中文字符字体配置)
  - [字体选用建议](#字体选用建议)
  - [外语字符配置中文字体](#外语字符配置中文字体)
  - [字体找不到怎么办？](#字体找不到怎么办)
- [建立文档](#建立文档)
  - [文档类型和字号](#文档类型和字号)
    - [字号使用](#字号使用)
  - [纸张布局](#纸张布局)
    - [出血](#出血)
  - [各级标题](#各级标题)
  - [标题格式](#标题格式)
  - [换页](#换页)
  - [自动空白页](#自动空白页)
- [页面排版](#页面排版)
  - [行高和段距](#行高和段距)
    - [行高](#行高)
    - [段距](#段距)
  - [缩进](#缩进)
- [注释](#注释)
  - [脚注](#脚注)
  - [尾注](#尾注)
- [目录](#目录)
  - [目录标题](#目录标题)
  - [目录配置](#目录配置)
  - [局部目录](#局部目录)
  - [文档内跳转](#文档内跳转)
  - [页码更改](#页码更改)
- [页眉页脚](#页眉页脚)
  - [页面风格定义](#页面风格定义)
  - [页面风格使用](#页面风格使用)
  - [问题处理](#问题处理)
- [杂七杂八](#杂七杂八)
  - [空白页](#空白页)
  - [空白段](#空白段)
  - [中文破折号](#中文破折号)
  - [特殊字符换字体](#特殊字符换字体)
  - [行溢出](#行溢出)
  - [纸面不充盈](#纸面不充盈)
  - [扉页](#扉页)
  - [子文件](#子文件)
  

# $\LaTeX$的优点

一般我们说到$\LaTeX$，总难免骂两句这东西繁磨磨唧唧的渲染、乱七八糟的命令和屎山一样的包。正因如此，无数人试图取代$\LaTeX$，但它目前依然是唯一可靠的学术类排版工具，也是世界上最流行的排版系统之一，这足以证明它的独特价值。

## 代码式编辑

最开始令我选择$\LaTeX$的就是这一点——它的工作文件是纯文本（相当于代码），用引擎编译出结果。

“所见即所得”的优势在于可以即时获得结果，相对的，编辑时也必须应对格式和内容的深度捆绑。在$\LaTeX$里，编辑和渲染天然分离，纯文本文件可以轻松实现文档内容与格式的解耦。从而使得“编辑”这一步的工作效率达到最理想的状态。

对于格式：可以直接使用测试性的样例代码，用最快的编译速度查看格式效果。

对于内容：任何非正文内容，无论是标题还是注释，用$\LaTeX$都是打开编辑器敲一个命令的事。可以快速进行大量编辑，而后统一渲染，实际上能够节约时间。

甚至于，$\LaTeX$还支持条件判定（if-else），可以轻松实现多种格式的共存与切换。纯文本的性质也适用于版本管理。

## 默认细节极佳

如果找一些专业的中文排版攻略读（[比如这个](https://www.thetype.com/2020/01/16565/)），那么就会意识到，文字排版这件事其实非常细碎繁杂，需要关注的细节极多。*InDesign*等面对专业**版式设计**人士制作的排版软件，支持对每一个细节进行调整，因此选项功能层层相套。对应的，其初始状态其实相当不堪，需要做大量调整才可入眼。

而$\LaTeX$则不然。由于开源的特性，$\LaTeX$内有着大量前人造好的轮子，可以覆盖排版时应当处理的普适性专业细节，极大地节约工作成本。用户只需要进行自己的个性化即可。对于中文，最显著的案例就是标点压缩和字距。

- 标点压缩

    在正式的排版原则中，独立标点应为1个字符宽；连续的两个标点（如`：“`）应该挤压为1.5个字符宽；段首的起始标点应为0.5个字符宽；当汉字与外语字符/阿拉伯数字相邻时，其间距应该有一个空格……

这些细碎的设定，在$\LaTeX$的`ctex`包中默认就会满足，不需要自己进行任何选择或调整。

- 字距

    字距指文字之间的水平间距。一份理想的中文文本应该满足以下条件：

1. 行宽可以规定
2. 文字每行左右均顶格，恰好占满设定的行宽
3. 在没有标点压缩干扰的情况下，文字竖对齐。主要是最后一行，字距应与前文相同，而非简单左靠

与标点压缩相同，`ctex`包默认就提供最美观的排版。而其他专业排版工具中，就需要自己设置对齐、字距每个细节，才能达到一样的效果。

$\LaTeX$还能够在换行时，视需要自动断开英文单词，使得画面进一步整齐。

## 模板化

我创立了一个模板并上传了Overleaf，此时尚还处于审核中。如果希望使用，可以联系我(3440950898@qq.com)，我会发送给你。

# 排版参数

## 小说

版式设计是为了优化信息的传达。对于小说，最重要的信息永远是故事本身，即文字内容。因此，没有必要太深入地研究版面设计。但完全不管也不行，“易读性”和“可读性”是必须要考虑的。

易读性即Legibility，对每个文本单元（中文的字、英文的单词）的识别程度，更多地指向字体。可读性即Readability，即阅读体验的舒适性。在排版中，可读性代表一段文本的阅读容易度，主要指向基础单元的排布方式，例如字距、行高。

这都是排印学里非常根本的课题。有太多的人已经研究过了，我们可以直接使用现成的结论：

行高：中文的行高一般至少是字高的1.5~1.8倍，受字体和字号的双重影响。如果行高不足，汉字等高的特性会使得行与行之间空隙不清晰，降低阅读流畅性。

行数：翻页的频次主要是行数决定的，这个数极大地影响阅读体验。对于A5大小的纸张，可以以25为参照，每页行数小于等于25时，阅读体验比较休闲，反之行数越多，越接近于专业性强的书籍，阅读体验越严肃。实际使用中，23-27行适用于小说类文章排版。

单行字数：A5这个纸张大小还没有充分利用人眼的视野空间，因此单行字数只受限于字体大小和文字区域的宽度，不需要考虑人眼阅读能力而额外分栏。通常的书籍是每行28~30个字，实际体验上，26~32都是可接受的。

## 同人文学

同人文学，相比于标准的小说，自然会有些不同。我相信，没人希望自己的本子印出来是一股人民文学出版社四大名著的气质。对参数做一些小调整，降低一页上的信息量（可以简单理解为字数），就可以在排版时使页面变得活泼起来。

1. 拉宽行距

    拉宽行距、降低每页行数，能有效降低每页信息量。

2. 缩小版心

    版心即纸张上印刷核心内容的区域。缩小版心，也能把每页的信息量降低。

但请注意，*排版越疏松，本子越厚*。***本子越厚，成本越高***。印厂算钱的时候只看页数，不看油墨密度，页数越多就越贵。并且，对于字数较多（20万以上）的本，不紧凑一点真的会印成砖头的。

一个更直观的算法：`每页行数*每行字数`得到`理论每页字数`，是一页纸理论上能印的字数，但实际上不可能印满（~~出版物上标注的字数是版面字数，约等于理论字数乘页数，所以给人的感觉很注水~~）。理论值乘上`0.6~0.65`才是实际上的`平均每页字数`。整个本的字数除以`平均每页字数`可以得到大约的正文页数（排版增加的留白已经考虑在内）。最通用的80g纸，厚度是0.11毫米。

所以用`总字数/每页行数/每行字数/11.364`就可以得到一个大约的厚度（单位为毫米）。

也就是说，如果我们用每行32个字，一页24行来印刷一个20万字的本，会有约22.9毫米厚。如果用一行28个字，一页20行来印刷，将飙增至31.4毫米厚，增加了接近40%的厚度。

## 进阶知识

在正式出版物中，还有其他~~强迫症发作的~~进阶规则。

1. 行宽是整数个字的宽

    即一排汉字能将一行恰好排满，提升每页纸上的网格感。

2. 标题所占高度是整数个行的高

    使得不同页面格式中，正文都能实现跨页行对齐。

这些规则本质上都是令阅读体验更接近于排字印刷时代，但是到了现代，出版社也不是一定遵守这些规矩，姑且看看，了解一下即可。除非有很强的强迫症，不然不需要应用。

------

了解了以上内容后，就让我们进入正题，开始使用$\LaTeX$进行排版。

# 字体设定

不同字体的细节不同（如思源宋体会在一行有三个孤立标点时进行压缩，多挤出一个字宽，而方正书宋则不会），会在本质上影响排版效果，所以**一定**要在开始仔细排版**之前**就选择字体并配置好。

## 字体入门

### 字体类别

字体可以简单分为有衬线（Serif）和无衬线（Sans Serif，或简称为Sans）两类。衬线指的是笔画边角处的装饰，例如宋体是典型的衬线字体，而黑体是典型的无衬线字体。

纸张上，有衬线的字体易读性更佳，一般用于正文中；无衬线字体更加醒目，可以用于标题。

等宽字体（mono）指所有字母和符号都占据同样宽度的字体。对于中文等符号文字没有意义，咱天然就是等宽字体。对字母文字而言，等宽的易读性并不太好，应用场景很有限。除了故意模仿打字机的文字质感外，只有编程为了竖对齐使用等宽字体。

### 字体风格

一个字体名是一个系列，其中往往有多个风格，最重要的是各种字重和斜体。

字重：描述一个笔画有多粗。

从轻到重（从细到粗）分别有：thin, extra light, light, regular (normal), medium, semi bold, bold, heavy (black)。一个字体必然有字重关键词，留空时会自动使用regular。原则上的加粗行为就是字重从regular变成bold。如果一个字体没有bold字重，word还会用算法生成一种伪粗体。

斜体：Italic，也叫意大利体。

斜体是字母排版时产生的一种文字标注方式，字体的斜体和字重平行。不是所有字体都有斜体，很多时候我们看到的也是算法计算的伪斜体。**中文其实没有斜体**，承担类似功能的是楷体或仿宋。

## `ctex`包介绍

$\LaTeX$需要`ctex`包来处理中文，需要`xelatex`或`lualatex`引擎才能编译。使用方法为

```  latex
% 方案一
% 在建立文档时指定使用ctex，Z代指文档类型
\documentclass{ctexZ}

% 方案二
% 建立文档后引入包
\usepackage{ctex}
```

方案一相当于建立中文文档，方案二相当于在英文文档里使用中文。方案一自动将所有预设词翻译为了中文，更加便捷；方案二在细节上更加通用。例如，按方案一生成的目录中，标题内“第x章”“第x部分”等字样需要用`\ctexset`命令来调整；而方案二可以用更加基础（i.e.与其他包兼容性更好）的方式对这些地方进行自定义。

`ctex`包默认根据**当前操作系统**选择字体配置，策略如下

![ctex预设包](data/ctex.png)

`ctex`包内有若干套预设好的字体配置，可在导入时使用`[fontset=X]`选择，`X`为包名，详见。对于装了全套方正字体的用户，可以一键`[fontset=founder]`使用全套方正字体配置。

|  包名（`X`）  |
| :--: |
| `adobe` |
| `fandol` |
| `founder` |
| `mac` |
| `macnew` |
| `macold` |
| `ubuntu` |
| `windows` |

但是`ctex`包的预设是以**免费使用**而非**免费商用**为标准的，出本时最好只使用**免费商用**的字体，这就需要自己进行配置。

## 字体名称查询

首先是寻找字体，代码寻找字体需要使用字体的系统名称，在Windows中，简单的查找系统字体方法是运行`fc-list`命令。注意$\LaTeX$只能找到$\LaTeX$内自带的字体和`C:\Windows\Fonts\`目录下的字体。因此安装字体时，需要选择**为所有用户安装**。

可以用系统命令`fc-list >> fonts.txt`生成一个字体表文件，包括系统上的可用字体。增加`:lang-zh`参数可以指定过滤筛选中文字体。注意一些字体虽然使用时是中文，但其字体文件会被识别为日文或韩文，不会出现在结果中。确定**英文系列名**时，可以用`fc-list | Select-String "系列名"`来筛选字体列表。中文名可能会是乱码，建议只用英文名进行此项操作。

得出的结果中包含字体名，这里使用开源字体*Vollkorn*系列举例，`fc-list | Select-String "Vollkorn"`得到的结果如下

```
C:/Windows/fonts/Vollkorn-Medium.otf: Vollkorn,Vollkorn Medium:style=Medium,Regular
C:/Windows/fonts/Vollkorn-Italic.otf: Vollkorn:style=Italic
C:/Windows/fonts/Vollkorn-Bold.otf: Vollkorn:style=Bold
C:/Windows/fonts/Vollkorn-MediumItalic.otf: Vollkorn,Vollkorn Medium:style=Medium Italic,Italic
C:/Windows/fonts/Vollkorn-BoldItalic.otf: Vollkorn:style=Bold Italic
C:/Windows/fonts/Vollkorn-Regular.otf: Vollkorn:style=Regular
C:/Windows/fonts/Vollkorn-SemiboldItalic.otf: Vollkorn,Vollkorn Semibold:style=Semibold Italic,Italic
C:/Windows/fonts/Vollkorn-Semibold.otf: Vollkorn,Vollkorn Semibold:style=Semibold,Regular
```

其中`*.otf:`和`:style`之间的即为字体在系统里的名称。对于字体的特殊风格，可以直接以`字体名 风格`作为字体名加载，如`Vollkorn Semibold Italic`。切记区分大小写，有的字体里会是`SemiBold`，有的是`Semibold`。

注：一些字体名中含有`-`，在打印时会增加转义符显示为`\-`，使用这些字体时输入`-`即可。

另外，也可以使用[FontDrop!](https://fontdrop.info)网站解析单个字体文件，获得字体名。解析样例字体*EBGaramondSC12-Regular.otf*时结果如下。

```
You see EB Garamond SC

Name: EB Garamond SmallCaps 12 Regular. Style name: 12 Regular. Version 0.016
© Created by Georg Duffner with FontForge 2.0 (http://fontforge.sf.net)

License: Copyright 2010-2013, Georg A. Duffner (<http://www.georgduffner.at/ebgaramond|g.duffner@gmail.com>), 2013 Siva Kalyan This Font Software 
```

其中`You see`后的是字体系列名，而`Name`与`. Style name`之间的即为字体本身在系统里的名称（对于风格字体，即为指定时使用的名称）。

## 外语字符字体配置

$\LaTeX$的字体配置默认是**只对部分字符生效**的，需要分别配置，混排时可以叠加指定。

我们先说外语字符。`ctex`包只对中日韩三语起效，其他语言的字符（不止为ASCII，还包括章节符$\S$和摄氏度℃等符号）是默认使用基础字体渲染的，只有`fontspec`包配置的字体才能起效。

```latex
% 引入包
\usepackage{fontspec}
% 设置主字体
\setmainfont{Vollkorn}
```

可以设置三种基础类别的字体：主字体`\setmainfont`用`\rmfamily`调用；无衬线字体`\setsansfont`用`\sffamily`调用；等宽字体`\setmonofont`用`\ttfamily`调用。一般设个主字体就够了，其他两种字体是默认格式中使用的，自定义格式时反正也要覆盖掉。

用`\newfontfamily`配置新的字体。

```latex
% 设置字体，并自定义字体名\medfont
\newfontfamily\medfont{Vollkorn Medium}
```

$\LaTeX$默认寻找同系列的字体作为其加粗和斜体，但可以自行进行指定。

```latex
% 设置字体，并自行配置加粗和斜体
\newfontfamily\medfont{Vollkorn Medium}[BoldFont=Vollkorn Semibold, ItalicFont=Vollkorn Semibold Italic]
```

使用非主字体时，只需要输入配置时设定的字体名即可。

```latex
\begin{document}
% ...
\medfont medium weight text
% ...
\end{document}
```

### 连字

英文衬线字体中存在连字（ligature），通过设计优化某些字符串的显示方式来提升易读性。最经典的三个案例如下图（字体为*Vollkorn*）。

![连字样例](data/fil.png)

$\LaTeX$默认载入一部分通用连字（OTF中tag为liga），能提升英文文本的易读性。而一些字体对连字的设计比较充分，还使用了其他的连字tag。通常类别有：clig指上下文连字（contextual），能使手写体中产生连笔；dlig指自由连字（discretionary），会使文字更花俏；hlig指历史连字（historical）能令文字看起来较为复古；rlig标记必需连字（Required），可以实现“将英语字母拼合得到其他字母”，例如ae拼合为æ。

![连字配置](data/ligatures.png)

配置时可以添加一个`[Ligatures=XXX]`参数，启用一些其他tag里的连字，见上图。其中Common是默认打开的。

可以用[FontDrop!](https://fontdrop.info)这个网站来查看字体内连字。有些字体虽然设计了连字，但并没有正确标注，导致这些连字虽然存在但却无法使用。面对这种情况，可以用[FontForge](https://fontforge.org/en-US/)软件进行[手动标注](https://fontforge.org/docs/tutorial/editexample4.html)。

## 中文字符字体配置

中文字符，如`你`，`我`，`；`（中文分号），`“”`（中文引号），均需要使用`ctex`包内的命令进行字体配置才能正常显示。首先是引入包时用`[fontset=none]`避免加载默认字体集，防止产生冲突。

```latex
\documentclass[fontset=none]{ctexZ}
% 或
\usepackage[fontset=none]{ctex}
```

字体配置的命令和`fontspec`包的差不多，加个`CJK`即可配置中文、日文、或韩文的字体，配置出的字体只会对这三种语言内的字符生效。

```latex
% 免费商用中文字体
\setCJKmainfont{Source Han Serif}[BoldFont=Source Han Serif SemiBold, ItalicFont=FZKai-Z03]

% 以下是六种免费商用的中文字体，字体名根据所下载到的文件，可能会多一些后缀，以fc-list中的结果为准
\newCJKfontfamily\songti{Source Han Serif} % 思源宋体
\newCJKfontfamily\sheiti{Source Han Sans} % 思源黑体

\newCJKfontfamily\shusong{FZShuSong-Z01}% 方正书宋
\newCJKfontfamily\fangsong{FZFangSong-Z02} % 方正仿宋
\newCJKfontfamily\heiti{FZHei-B01} % 方正黑体
\newCJKfontfamily\kaiti{FZKai-Z03} % 方正楷体
```

其中，方正系列四个字体都只有一个字重，而思源两个系列都具有extralight, light, regular, medium, semibold, bold, heavy七个字重，可以进行指定。所有字体中都不含斜体。

## 字体选用建议

- 中文

实际使用时，建议将方正书宋或思源宋体Regular作为主字体，这样易读性较好。两种字体的本质区别在于，书宋是完全针对书籍印刷设计的，印出来效果最好，正因如此，被大量出版社采用，看起来会很眼熟；思源宋体的设计在屏幕显示和印刷之间端了水，印出来的效果略逊于书宋，但是不会那么眼熟。字重上，书宋略重于思源宋体Light，略轻于思源宋体Regular。

使用上，思源宋体可以自行指定粗体的程度；方正书宋只有一个字重免费，固然技术上可以将较粗的思源宋体或方正黑体作为粗体使用，但因为细节差异众多，看起来会很古怪。

不管用什么主字体，都推荐指定方正楷体或仿宋作为斜体，以便于在正文中标注少量字符（如引用）。

装饰性文字（脚注、页眉等）建议使用方正仿宋或楷体。

各级标题字体建议自己判断决定，但思源黑体是无论如何都不推荐的，它的设计上比方正黑体差很多。我个人喜欢用不同字重的思源宋体来显示各级标题。

注：由于Windows系统的渲染机制问题，在Windows电脑上面的宋体就没有好看的，可将文档传到其他系统的设备上检阅效果。

- 外语

外语的免费字体很多（特别是仅支持ASCII字符的免费字体），在挑花眼的同时，最好也关注一下一些进阶选项，以提升混排效果。这里介绍一些实用的花招，更详细的推荐阅读`fontspec`包文档。

以下是一些样例，中文使用思源宋体Regular；英文字体均是从网站[1001 Fonts](https://www.1001fonts.com)下载的免费商用字体，全部使用Regular字重的默认配置。

![字体对比](data/fonts.png)

*Neuton*虽然设计好看，但字母显著偏小。配置时建议用`[Scale=比例]`参数放大。

*Libre Baskerville*和*Cormorant*的默认字重都与中文差异颇大。

*EB Garamond*的字母字重与中文相当契合，但其数字放在中文内会显得很弱。

*Vollkorn*的整体字重略高一些，英文显得略粗，数字在与中文混排时保持了恰当的视觉重量。但由于数字采用了与英文相同的三格设计（俗称OldStyle），在数字与汉字混排时看起来会很诡异。建议使用`[Numbers=Lining]`切换到等高数字，该功能与连字类似，不是所有字体都包含。

*Spectral*的字母设计更接近等宽字体，字距比起中文明显偏高。建议使用`[LetterSpace=改变值（如-3）]`来降低字母间距。

令，如果想要调整空格宽度，使用`[WordSpace=空格宽度]`参数即可。

不过本质上，**混排字体的选择取决于文本的字符频**。如果文中存在大量字母（例如ABO中，Alpha/Beta/Omega三个单词会反复出现），那么就应当主要关注字母能否融入正文。

## 外语字符配置中文字体

有的中文字体中也一并包含了同风格的外语字符设计。如果需要使用，将其用`fontspec`包内命令加载，然后叠加使用即可。

```latex
\newfontfamily\songtien{Source Han Serif}

\songti\songtien 中英文mixed文本
```

但是，不推荐大面积使用方正系列字体中的外语字符。

## 字体找不到怎么办？

第一步，确定字体确实安装在了`C:\Windows\Fonts`文件夹里。

第二步，检查代码中的拼写和`fc-list`命令获得的一样，特别是大小写。

第三步，在字体名称外面加个中括号。别问为什么，我也不知道，总而言之亲测有效。

```latex
% 修改前
\newCJKfontfamily\xbsong{Source Han Serif SemiBold}
% 修改后
\newCJKfontfamily\xbsong{[Source Han Serif SemiBold]}
```

第四步，直接配置字体文件名，支持绝对路径和`fc-list`中能找到的字体名。只要字体在你电脑上，用这个方法就可以百分百找到。该方案只支持XeTeX和LuaTeX两个引擎，巧了，就是支持中文的两个引擎。

```latex
\newfontfamily\vollkorn{Vollkorn-Regular.otf}
```

第五步，天涯何处无芳草，字体到处都是，换一个吧。

# 建立文档

相信在前文中，读者已经建立过一些测试文件来研究代码了，在这一节中，我们所讨论的是正经的印刷文档。

## 文档类型和字号

```latex
\documentclass[10pt]{book}
```

$\LaTeX$原生有着`article`、`book`、`report`三种文档类别，对应的`ctex`类分别为`ctexart`、`ctexbook`、`ctexrep`。三种类别的主要区别在默认层深和排版方式上，虽然排版之后肯定要自己改，但为了直观，本教程推荐使用`book`类。

`book`类默认支持三种字号10,11,12pt，pt即为磅数。三种字号可读性都属不错，不建议更大或者更小。具体选择时，可以用“磅数÷2.845=毫米数”来计算文字大小。也可参考word，word中的五号字是10.5磅，小四则是12磅。

`ctex`文档类别支持word款的两种字号，配置方法如下

```latex
% 正文五号字
\documentclass[zihao=5]{ctexbook}
% 正文小四号字
\documentclass[zihao=-4]{ctexbook}
```

### 字号使用

![字号](data/fontsize.png)

在不同的文档字号时，各个字号命令的对应的字号如上图。

## 纸张布局

一般来说，同人文本的尺寸是A5左右。标准A5是148*210mm，实际中印厂的尺寸不一定能到这里，但我个人还是建议按标准尺寸来做设计，边距留一些余量，印厂不能满足的话再压缩。

`geometry`是处理布局的包，参数极多，这里只介绍少量常用内容，有其他需求建议阅读文档。

![纸面布局](data/paper.png)

参数不需要全部设置，水平竖直方向各三个即可，最后一个会自动计算。注意水平方向`left, right`和`inner, outer`这两组是二选一的关系。双页印刷应当使用`inner, outer`这组参数，会根据页面单双自动调整文字区域位置。

``` latex
% 引入包
\usepackage{geometry}
\geometry{
% A5纸张标准宽高
paperwidth=148mm,
paperheight=210mm,
% 天头，文字区到纸张上沿的距离
top=17mm,
% 地脚，文字区到纸张下沿的距离
bottom=23mm,
% 切口，文字区到纸张被翻开一侧的距离
outer=13mm,
% 订口，文字区到纸张被装订一侧的距离
inner=21mm,
% 文字区和页眉下沿之间的空白
headsep=7mm,
% % 页眉的高度，一般不需要这行
% headheight=6mm,
% 文字区和页脚下沿之间的空白
footskip=12mm,
}
```

`\geometry`命令会决定纸张的大小，不可修改。边距等数值可以在文档内部用`\newgeometry`命令进行修改，如

```latex
\begin{document}
% ...
% 新的边距会从当前页起效
\newgeometry{left=30mm,right=30mm,top=20mm,bottom=20mm}
% ...
% 将边距重置为\geometry命令中设置的
\restoregeometry
% ...
\end{document}
```

### 出血

上述讲解的A5纸张所得到的是效果图，印刷时需要为印厂提供有`3mm`出血的版本。增加出血很简单，只需要将`paperwidth, paperheight`各增加`6mm`，**每一次**设置的`top, bottom, inner, outer, left, right`各增加`3mm`即可。`textwidth`和`textheight`两个参数不用改变。

**在正文排版没有bug的情况下**，这样的修改可以在效果图四周都增加`3mm`的白边，中心对齐检阅时，文字位置完全不变。如果修改后有页面发生了移动，那么请在该页的写法上寻找问题。

## 各级标题

`book`类可以使用所有种类的标题，直观地说，可以理解为一本长篇小说的级别。具体效果如下：

|       层深 | 标题 | 含义 | 效果 | 中短篇集用处 | 长篇用处 |
| :-:| :--: | :--: | :--- | :--- | ---- |
| -1 | \part | 部 | 标题新起一张纸，并独占 | 在文有明显分类，每类不止一篇时，用于分类 | 每部 |
| 0 | \chapter | 章 | 标题新起一张纸，标题下可以有内容 | 每篇文，标题下可以插入一些独立信息（如summary）占满一页，或直接接正文 | 每章 |
| 1 | \section | 节 | 标题与上文同页 | 篇内分章的话，作为一章的标题 | 每节 |
| 2 | \subsection | - | 标题与上文同页 | 看着用 | 看着用 |
| 3 | \subsubsection | - | 标题与上文同页 | 看着用 | 看着用 |

对于小说，不建议使用超过两级的标题。只选用`part+chapter`或`chapter+section`即可。

## 标题格式

对于文内标题，使用`titlesec`包内的命令来配置格式。

对于标题格式，用`\titleformat`命令来配置

```latex
% 参数
\titleformat{命令}[形式]{格式}{标题序号}{间距}{前命令}[后命令]
% 示例
\titleformat{\chapter}{\huge\chapterfont}{\thechapter}{1em}{\thispagestyle{empty}}
```

对于标题的间距，使用`\titlespacing`命令

```latex
% 参数
% 注：左间距的相对点是这一行文字的起始位置，即段首缩进后的
\titlespacing*{命令}{左间距}{上间距}{下间距}[右间距]
% 示例
```

标题上的编号默认为*1.1.1*类，即子级编号会带上上级，用以下命令来去除子级的上级编号

```latex
\counterwithout{字级别}{亲级别}
```

## 换页

`\clearpage`命令可以使后续内容从新的一页上开始，`\newpage`则可以新起一栏（单栏模式下即为新开一页）。有浮动要素（如图片、表格）时，二者的处理机制也不同，如需要这部分功能请自行深入研究。

## 自动空白页

`\chapter`及以上级别的标题会自动新起一张纸。`book`类文档中默认为双页模式，右页为新纸。当上文结束在奇数页时，会产生一页空白页。不想要的话，可以在定义`documentclass`的时候增加一个参数`openany`，允许在偶数页开启新内容。

```latex
\documentclass[...,openany]{...}
```

相对的，如果在使用了`openany`参数后，希望某页在右页上开始，则可以使用`\cleardoublepage`命令。该命令会自动插入空白页，使后续内容从下一个右页铺开。

若希望后文在左页上开始，可以使用以下写法：

```latex
% 新起一页
\clearpage
% 如果页码为奇数
\ifodd\thepage
    % 插入一个空白页，空白页函数见后文杂七杂八-空白页一节
    \blankpage
\fi
```

# 页面排版

## 行高和段距

首先来明确几个词的含义：

行高：上一行文字底边到这一行文字底边的距离。

行距：即行间距，上一行文字底边到这一行文字顶边的距离。

段距：换段时，在行距基础上额外增加的距离。

段距应为**行高的整数倍**，不然特别的丑。

### 行高

推荐使用`\setspace`包来调整行高。

```latex
% 定义好的命令
\singlespacing % 单倍行高
\onehalfspacing % 1.5倍行高
\doublespacing % 双倍行高

% 自定义行高
\setstretch{行高倍数} % 如1.618
```

其中，定义好的三个命令以文字高度（即字号）为基础值，即，单倍行高会使得行高等同于文字高度。

但自定义行高的机制则不然。`\setstrectch`的基础倍数为**字号的120%**。对于10pt的文档字号，`\setstrectch{1}`会使得行高为12pt，`\setstrectch{1.5}`会使得行高为18pt。

这些方式都会使`\baselineskip`（记录行高的变量）自动跟着变化，可以以此为参数设置缩进。

### 段距

改变`\parskip`即可，默认为0pt。

```latex
\setlength{\parskip}{段距}
```

使用时，最好不要只给一个数，容易导致每页出现大量`Overfull/Underfull \vbox`错误，解决方法有两种。

1. 设置段距时，给出弹性空间。不要让最短段距低于0，会使得段间空白小于行间。
2. 使用命令允许每页下缘不齐。**不推荐**，在页面布局做不到行对齐时，该命令会使得整体看起来像狗啃的一样。

```latex
% 设置弹性空间
\setlength{\parskip}{段距 plus 最多加大值 minus 最多减少值}
% 下缘不对齐
\raggedbottom
```

## 缩进

用`identfirst`包来放开首段的缩进。

```latex
\usepackage{indentfirst}
```

段首缩进的长度也可以调整，但不是很需要。中文文档用默认的`2em`是最合适的。

```latex
\setlength\parindent{长度}
```

# 注释

注释一般是用脚注和尾注两种，视情况自行选择即可。

## 脚注

页底脚注以`\footnote[编号]{内容}`命令来添加。

引入`footnpag`包可以在每页重置脚注编号。

```latex
\usepackage{footnpag}
```

脚注所使用的字体可以自行设定，方法如下

```latex
\usepackage{etoolbox}
\makeatletter
\patchcmd{\@footnotetext}{\footnotesize}{指定字体和字号}{}{}
\makeatother
```

## 尾注

建议使用`endnotes`包来管理尾注。

添加尾注使用`\endnote[编号]{内容}`，在文章任意地方使用`\theendnotes`命令输出尾注。第二次使用`\theendnotes`会输出第一次输出后新增的尾注。

尾注标题使用以下命令进行修改。

```latex
\renewcommand{\notesname}{尾注标题}
```

尾注标题默认影响`\leftmark`（该命令的用处见页眉页脚一节），可以用以下命令规避。

```latex
\renewcommand{\enoteheading}{\section*{\notesname}\mbox{}\par\vskip-\baselineskip}
```

尾注编号可以用如下代码重置：

```latex
\makeatletter
% 每章重置尾注编号，chapter可修改为其他标题级别
\@addtoreset{endnote}{chapter}
\makeatother
```

# 目录

建议在**决定了所有内容后**，再来设计目录的格式。

用`\tableofcontents`命令，在文档中插入目录。

## 目录标题

使用如下命令来调整目录页的标题内容，其格式默认与`\chapter`级标题相同。`ctex`文档类别中，目录页标题会翻译为“目录”，也可用如下命令来增加空白间隔。

```latex
\renewcommand{\contentsname}{目录标题}
```

## 目录配置

用如下命令设置目录层深，层深数值见前文。

```latex
\setcounter{tocdepth}{层深}
```

目录配置包并不唯一，我使用的是`titletoc`，配置格式的命令是`\titlecontents`。

```latex
% 代码
\titlecontents{标题名}[左距离]{上方代码}
{序号格式}{无序号的标题格式}
{页码格式}[下方代码]

% 样例
\titlecontents{chapter}
[0em]
{\vspace{1em}\Large\tocchapterfont}
{\makebox[10mm][l]{\S\hspace{0.1em}\large\uppercase\expandafter{\romannumeral\thecontentslabel}}}
{}
{\hspace{4mm}\tocpagefont\large\contentspage}
[\vspace{0.5em}]
```

其中，无序号标题默认不出现在目录里，想要的话需要手动添加。可使用以下命令。

```latex
\addcontentsline{toc}{级别}{标题名}
```

标题的名称默认会显示在序号区和页码区之间，内容默认与正文相同，但可以不同。如注只能放在正文中的标题里，而不能出现在目录里。

```latex
\chapter[目录中的名称]{正文中的名称}
```

`[目录中的名称]`留空可以使其在目录中以编号节存在，而不显示节名称。

当改变页码字体时，可能会出现`\hbox underfull`警告，可以用以下代码改变默认的页码宽度。

```latex
\makeatletter
\renewcommand{\contentspage}[1][\thecontentspage]{\hb@xt@\@pnumwidth{#1\hfil}}
\renewcommand{\@pnumwidth}{页码宽度}
\makeatother
```

## 局部目录

`titletoc`包支持局部目录，用法如下。

```latex
% 开始记录标题属于某个局部
\startcontents[局部名称] % 这是一个key，保持一直即可
% 结束记录某个局部的标题
\stopcontents[局部名称]

% 打印局部目录
\printcontents[局部名称]
{前缀} % 留空则使用主标题内的格式
{开始层级} % 局部目录的开始层级
[层深] % 局部目录的层深
{目录代码} % 该目录表头的代码，如\chapter*{\contentsname}可增加一个标题
```

## 文档内跳转

虽然是按印刷品的标准的制作，但是为了检阅方便，还是建议使用`hyperref`包来启用超链接跳转。这样可以从目录直达某个标题。

超链接会带来格式的变化，可以使用一条命令来避免。

```latex
% 启用超链接
\usepackage{hyperef}
% 超链接不影响格式
\hypersetup{hidelinks}
```

## 页码更改

在文档中，可以用`\setcounter`来修改页码，后续页的页码和目录中的页码都会跟着改变。该命令可以很简便地确定正文首页为第1页。

```latex
\setcounter{page}{本页的新页码}
```

如果某处存在若干页使用其他方式排版（如图文混排时的图片部分），需要将这部分页码空置预留出来，可以使用`\addcounter`增加页码。

```latex
\addcounter{page}{增加量}
```

# 页眉页脚

一般使用`fancyhdr`包来自定义页眉页脚。

## 页面风格定义

用`\fancypagestyle`命令设计新的页面风格。

```latex
% 页面风格名为mystyle
\fancypagestyle{mystyle}{
% 清空既有设置
\fancyhf{}
% 设置页眉页脚
\fancyhead[位置]{内容}
\fancyfoot[位置]{内容}
}
```

位置为`[L,C,R]`（左中右）和`[O,E]`（奇偶数）两个选项组成，如`LE`表示偶数页的左侧，`C`表示无论奇偶页都显示在中间。

对于`book`类而言，文档随着进行会自动更新两个标，以便于在页眉页脚中使用。其中`\leftmark`记录章标记，`\rightmark`记录节标记。如果想要获得部类别的标题和序号，需要自己手动记录。

`\Xmark`默认为`X 序号. 目录中的标题名称`，可以用重定义的方法来去除章标记中`X 序号.`的部分，节标记同理。

```latex
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\sectionmark}[1]{\markboth{\leftmark}{#1}}
```

## 页面风格使用

在文档中使用`\pagestyle{风格名}`命令设置这一页起的风格。

使用`\thispagestyle{风格名}`设置当前页的风格，下一页自动还原。

`fancyhdr`包提供`fancy`，`plain`，`empty`几种内置风格，`book`类会自动引用适配不同的页面，可以用上文的定义方法直接重定义。

`fancy`：页眉外侧角落偶数页为`\leftmark`，奇数页为`\rightmark`，页脚中央为`\pagenumber`。

`plain`：页脚中央为`\pagenumber`。

`empty`：什么都没有。

## 问题处理

对于由于标题位置而补充的空页，其页面风格默认与前文相同，可以使用引入`emptypage`包，使得空页面上不显示页眉页脚。

页眉下默认有一条横线，可以用以下命令来设置横线宽度，0为去除。

```latex
\renewcommand{\headrulewidth}{宽度}
```

如果希望页眉页脚溢出在文字区外，可以使用以下写法：

```latex
\fancyhfoffset[位置]{溢出值} % 用H/F这组位置标记来明确是页眉还是页脚
% 单独设置页眉或页脚的溢出
\fancyheadoffset[位置]{溢出值}
\fancyfootoffset[位置]{溢出值}
```

# 杂七杂八

## 空白页

空白页要包含若干要素，建议直接写成函数，方便使用。

```latex
\newcommand{\blankpage}{
% 新起一页
\newpage
% 页面要有内容，不然会被省掉，一个空box即可
\makebox{}
% 由于页面内有内容，需要手动去除页眉页脚
\thispagestyle{empty}
% 下一页，也可用\vfill或\clearpage实现
\newpage
}
```

## 空白段

有人（比如我）喜欢用空一段的方式分节。在$\LaTeX$中，文字后的空行，不管多少，都视为且只视为一个回车，空一段需要使用如下写法。

```latex
上一节最后一行

% 方案一，空白符
~\
% 方案二，空白盒
\mbox{}

下一节第一行
```

## 中文破折号

绝大多数中文标点都能在$\LaTeX$中按正常方式渲染，但是破折号并不会和标准使用方法一样，等同于两个字宽。这与字体无关，而是标点处理方案导致的。如果想要宽度正确的破折号，可以使用以下写法。

```latex
% rule命令画线，可以自行根据字体设计破折号的高度和粗细
\rule[0.35em]{2em}{0.03em}
% 宽度为0的线即为硬空白，可以在破折号左右固定留白
\rule{0em}{0.15em}{0em}\rule[0.35em]{1.7em}{0.03em}\rule{0em}{0.15em}{0em}
% 用\hspace命令生成左右空白，可以允许留白被挤压
\hspace{0.15em}\makebox[1.7em]{\rule[0.35em]{1.7em}{0.03em}}\hspace{0.15em}
% 直接把破折号用盒子框起来也是个办法，破折号默认在盒子里居中
\makebox[2em]{——}
```

使用中，可以将实现方式定义为一个命令，然后把正文中所有破折号替换为该命令，一键解决。

注：`\mycommand文字`会发生识别错误，应该使用`{\mycommand}文字`的写法。

## 特殊字符换字体

对于个别字符，你可能不满意它的默认字体，（例：在思源宋体中，间隔号·的宽度大约为一个空格的宽度，而非应有的一个字，但方正书宋中则不会出现这个问题，因此如果主字体选用思源，将间隔号专门设置为书宋会合适一些）。可以用如下写法进行修改。

给它起名`\mysymbol`，在全文中将中文字符替换成`{\mysymbol}`，大括号防止文字粘连。

设定函数，让`\mysymbol`用指定字体渲染。注意大括号需要有两层，限制字体应用范围。

```latex
\newcommand{\mysymbol}{{\symfont 符号}}
```

## 行溢出

行溢出，即`Overfull \hbox`警告。一行文字无法恰当地显示在规定的行宽里。

从本质上来说，*警告*并不是一定要消除，因为它不影响功能的实现。但是$\LaTeX$中的*警告*与*丑*基本可以画等号，所以排版过程中还是建议解决一下。

调整字号、行宽等基础布局数值，都可能在某些页面产生或消除该警告。

可以增加一个`sloppypar`域来一劳永逸，即

```latex
\begin{document}
\begin{sloppypar}
内容
\end{sloppypar}
\end{document}
```

但这样的解决方法会导致某一行字距过大，还是影响观感。最美观的解决方法其实是直接调整文本，在确定页面参数后，通过增减这一行的几个字或标点来解决问题。不过因为只能在给自己排版时进行改动，所以大部分时候就只能接受一点点的不美观了。

## 纸面不充盈

即`Underfull \vbox`警告。该警告出现是因为某页前一部分内容不足以填充页面，后一部分内容所需空间又过多，致使页面无法恰当地加载。

调整行宽、行高、段距等基础布局数值，都可能在某些页面产生或消除该警告。

解决方案为在合适的地方进行手动换页（`\clearpage`或`\newpage`）。但由于这样的手动解决方式不是很优雅，所以应当在排版过程的**最后**进行此调整。

## 扉页

虽然可以选择用`\maketitle`命令生成一页现成的扉页，但是真的很丑。中文出版物的扉页通常是封面的黑白朴素版，内外呼应，我个人推荐按此办理。根据封面的设计来手动布局，或直接导出一页适于黑白印刷的封面pdf文件（注意出血），插入正文开头作为扉页。

```latex
\usepackage[pdfpages]
\begin{document}
\includepdf[
    pages={文档页码，以英文逗号连接},
    angle=逆时针方向旋转角度
    ]{文件名}
\end{document}
```

## 子文件

善用子文件可以便于管理，实现格式与内容的分离，以及无关内容彼此分割。

最简单的方法是用`\input`命令，将另一个`.tex`文件引入当前文件，效果相当于用该文件的全部内容替换`\input`这一行。

```latex
% 子文件，head.tex
\documentclass[10pt]{book}
\usepackage{hyperref}
\hypersetup{hidelinks}

% 主文件，main.tex
\input{head}
```

对于较厚的本，可以使用`\subfiles`来分割出子文档，该包可以在不影响整体编译的情况下，独立编译子文档。由于换页的位置会直接影响效果，每个子文档的内容，在主文档中都应当开始于新的一页或新的一张纸。

```latex
% 以main.tex为主文档
% 在同层级的Chapter文件夹内，创建ch1.tex为子文档

% 子文档
\documentclass[../main]{subfiles}
\begin{document}
文档内容
\end{document}

% 主文件， main.tex
\usepackage{subfiles}
\begin{document}
\subfile{Chapter/ch1}
\end{document}
```

对于一些在文档内使用生效的命令，如`\pagestyle`，需要在子文件的文档内容里和主文件引入子文件前**都**使用，才能达到相同的渲染效果。

在子文档中，页码自动从1开始。可以手动设置，但不建议这样做，因为手动调整页码的命令在主文件内同样生效，容易产生页码不连续的问题。

`subfiles`包有时会出现一些bug，如果主文件和子文件渲染出来有页码之外的区别的话，大概就是原生bug造成的。如果调整不出来，可以釜底抽薪，删除开头结尾的`document`相关声明，改用`\input`引入。
