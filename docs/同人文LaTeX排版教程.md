---
title: 同人文LaTeX排版教程
tags: FIN
---

本文为懂得$\LaTeX$基础命令、语法，准备以此为排版工具，制作**中文同人文本**的玩家撰写。适用于**纯文本**或**图文本的纯文字部分**排版，考虑了中英文掺杂的情况。有少量场景与操作系统有关，本文暂只有windows的解决方案。

本文不包含$\LaTeX$安装、运行、命令解释、文档阅读等入门内容。这部分教程在网上已经很多，不需要我再抄一遍。

- [$\\LaTeX$的优点](#latex的优点)
  - [代码式编辑](#代码式编辑)
  - [默认细节极佳](#默认细节极佳)
  - [模板化](#模板化)
- [排版参数](#排版参数)
  - [小说](#小说)
  - [同人文学](#同人文学)
  - [进阶知识](#进阶知识)
- [页面](#页面)
  - [纸张布局](#纸张布局)
  - [出血](#出血)
- [字体设定](#字体设定)
  - [`ctex`包介绍](#ctex包介绍)
  - [字体名称查询](#字体名称查询)
  - [基础字符字体配置](#基础字符字体配置)
  - [中文字符字体配置](#中文字符字体配置)
  - [英文字符配置中文字体](#英文字符配置中文字体)
  - [字体找不到的常见解决方案](#字体找不到的常见解决方案)
- [建立文档](#建立文档)
  - [文档类型和字号](#文档类型和字号)
  - [各级标题](#各级标题)
  - [标题格式](#标题格式)
  - [自动空白页](#自动空白页)
  - [行高和段距](#行高和段距)
    - [行高](#行高)
    - [段距](#段距)
  - [缩进](#缩进)
  - [文档内跳转](#文档内跳转)
- [注释](#注释)
  - [脚注](#脚注)
  - [尾注](#尾注)
- [目录](#目录)
  - [目录标题](#目录标题)
  - [目录配置](#目录配置)
  - [局部目录](#局部目录)
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

一般我们说到$\LaTeX$，总难免骂两句这东西异步的编译机制、乱七八糟的命令和屎山一样的包。正因如此，无数人试图取代$\LaTeX$，但它目前依然是唯一可靠的学术类排版工具，也是世界上最流行的排版系统之一，这足以证明它的独特的价值。

## 代码式编辑

最开始令我选择$\LaTeX$的就是这一点——它的工作文件是纯文本（相当于代码），用引擎编译出结果。

“所见即所得”的优势在于可以即时获得结果，相对的，编辑时也必须处理格式和内容的深度捆绑。在$\LaTeX$里，纯文本可以轻松实现编辑和渲染的分离、文档内容与格式的解耦。从而使得“编辑”这步工作的效率达到最理想的状态。

对于格式：可以直接使用测试性的样例代码，用最快的编译速度查看格式效果。

对于内容：任何非正文内容，无论是标题还是注释，用$\LaTeX$都是打开编辑器敲一个命令的事，但在所见即所得类排版器中，则必须要经历“打开软件”——“导入文档”——“选中非正文”——“增加格式”的流程。

甚至于，使用$\LaTeX$还有着注释、条件命令、版本管理等诸多代码式的优点，可以轻松实现多种格式的共存与切换。

## 默认细节极佳

如果找一些专业的中文排版攻略读（[比如这个](https://www.thetype.com/2020/01/16565/)），那么就会意识到，文字排版这件事其实非常细碎繁杂，需要关注的细节极多。*InDesign*等面对专业**版式设计**人士制作的排版软件，支持对每一个细节进行调整，因此选项功能层层相套。对应的，其初始状态其实相当不堪，需要做大量调整才可入眼。

而$\LaTeX$则不然。由于开源的特性，$\LaTeX$内有着大量前人造好的轮子，可以基本覆盖排版时应当处理的普适性专业细节，极大地节约工作成本。用户只需要进行自己的个性化即可。对于中文，最显著的案例就是标点压缩和字距。

- 标点压缩

在正式的排版原则中，独立标点应为1个字符宽；连续的两个标点（如`：“`）应该挤压为1.5个字符宽；段首的起始标点应为0.5个字符宽；当汉字与外语字符/阿拉伯数字相邻时，其间距应该有一个空格……

这些细碎的设定，在$\LaTeX$的`ctex`包中默认就会满足，不需要自己进行任何选择或调整。

- 字距

字距指文字之间的水平间距。一份理想的中文文本应该满足以下条件：

1. 行宽可以规定
2. 文字每行左右均顶格，恰好占满设定的行宽
3. 在没有标点压缩干扰的情况下，文字竖对齐。主要是最后一行，字距应与前文相同，而非简单左靠

与标点压缩相同，`ctex`包默认就是这样的。而其他专业排版工具中，就需要自己设置对齐、字距每个细节，才能达到一样的效果。

$\LaTeX$还能够在换行时，视需要自动断开英文单词，使得画面进一步整齐。

## 模板化

我创立了一个模板并上传了Overleaf，此时尚还处于审核中。如果希望使用，可以联系我(3440950898@qq.com)，我会发送给你。

# 排版参数

## 小说

对于小说，版面上最重要的永远是故事本身，即文字内容。因此，太研究版面设计是没有必要的。

但完全不管也是不行的，文字的“易读性”（Legibility，对每个文字的识别程度）和“可读性”（Readability，对成段信息的理解程度）会极大地影响阅读体验。

好在有太多的人已经研究过了，所以我们可以直接使用现成的结论：

A5书籍，每行28~32个字为宜。这个纸张大小还没有充分利用人眼的视野空间，制约一行字数的就是字体大小和文字区域的宽度。因此不用太考虑每行过长或过短。

行高至少是字高的1.5~1.8倍，最小值的波动来自于字体差异，行高过低，汉字等高的特性会使得阅读流畅性降低。

至于一页多少行，可用的范围很大，主要取决于目标是营造什么样的阅读体验。对于同人本使用的A5大小的纸张，每页行数小于等于25时，阅读体验比较休闲。行数越多，单页信息量越大，越接近于专业性强的书籍，阅读体验越严肃。

## 同人文学

相比于标准的小说，同人文学的印刷自然会有些不同。我相信，没人希望自己的本子印出来是一股人民文学出版社四大名著的气质。对参数做一些小调整，就可以在排版时简单地使同人本变得活泼起来。

1. 拉宽行距

  行距拉上来一些，阅读体验会更更轻快。

1. 缩小版心

  版心，即纸张上印刷核心内容的区域。版心越小，一页能承载的信息量越小，阅读时翻页越快，体验越轻巧。

但请注意，*排版越疏松，本子越厚*。***本子越厚，成本越高***。印厂算钱的时候只看页数，不看油墨密度，页数越多就越贵。并且，对于字数较多（20万以上）的本，不紧凑一点真的会印成砖头的。

一个更直观的算法：`每页行数*每行字数`得到`理论每页字数`，是一页纸理论上能印的字数，但实际上不可能印满（~~出版物上标注的字数是版面字数，约等于理论字数乘页数，所以给人的感觉很注水~~）。理想值乘上`0.6~0.65`才是实际上的`平均每页字数`。整个本的字数除以`平均每页字数`可以得到大约的正文页数（排版增加的留白已经考虑在内）。最通用的80g纸，厚度是0.11毫米。

所以用`总字数/每页行数/每行字数/11.364`就可以得到一个大约的厚度（单位为毫米）

也就是说，如果我们用每行32个字，一页24行来印刷一个20万字的本，会有约22.9毫米厚。如果用一行28个字，一页20行来印刷，将飙增至31.4毫米厚，增加了接近40%的厚度。

## 进阶知识

在正式出版物中，还有其他~~强迫症发作的~~进阶规则。但是这些规则出版社也不是一定遵守，所以姑且看看，了解一下即可。

1. 行宽是整数个字的宽

    即一排汉字能将一行恰好排满，提升每页纸上的网格感。

2. 标题高度是整数个行的高

    使得不同页面格式中的正文，都能行与行对齐。

------

了解了以上内容后，就让我们进入正题，开始使用$\LaTeX$进行排版。

# 页面

一般来说，同人文本的尺寸是A5左右。标准A5是148*210mm，实际中印厂的尺寸不一定能到这里，但我个人还是建议按标准尺寸来做设计，边距留一些余量，印厂不能满足的话再压缩。

## 纸张布局

`geometry`是处理布局的包，这里只放少量常用内容，有其他需求建议阅读文档。

![image-20240904214715287](https://raw.githubusercontent.com/zhuty18/pic_src/main/202409042147364.png)

水平竖直方向各有四个参数，设置三个即可，最后一个会自动计算。

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

在左右边距上，双页印刷应当使用`inner, outer`这组参数，会根据页面单双自动调整文字区域位置。

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

## 出血

上述讲解了如何设置A5大小的页面布局，但A5是效果图。印刷时需要为印厂提供有`3mm`出血的版本，增加出血很简单，只需要将`paperwidth, paperheight`各增加`6mm`，**每一次**设置的`top, bottom, inner, outer, left, right`各增加`3mm`即可。

**在正文排版没有bug的情况下**，这样的修改足以在中心对齐时保证文字位置完全不变。如果修改后有页面发生了移动，那么请在该页的写法上寻找问题。

# 字体设定

不同字体的细节不同（如思源宋体会在一行有三个孤立标点时，把它们压缩出一个字宽，而方正书宋则不会），会影响排版效果，所以**一定**要在开始仔细排版**之前**就选择字体并配置好！

## `ctex`包介绍

$\LaTeX$基本使用`ctex`包来处理中文，需要`xelatex`或`lualatex`引擎才能编译。使用方法为

```  latex
% 方案一
% 在建立文档时指定使用ctex，Z代指文档类型
\documentclass{ctexZ}

% 方案二
% 建立文档后引入包
\usepackage{ctex}
```

方案一相当于建立中文文档，方案二相当于在英文文档里使用中文。方案一更加便捷；方案二在细节上更加通用。例如，按方案一生成的目录中，标题内会自动加入“第x章”“第x部分”等字样，需要用`ctex`的命令来调整；使用方案二可以用更加正统的方式对这些地方进行自定义；但如果希望在标题中使用中文序号，方案二需要用`\zhnumber`命令进行转换，方案一则不需要。

`ctex`包默认根据**当前操作系统**选择字体配置，策略如下

![ctex预设包](https://raw.githubusercontent.com/zhuty18/pic_src/main/202409042105996.webp)

`ctex`包内还若干套预设好的字体配置，可在导入时使用`[fontset=X]`选择，`X`为包名，详见。对于装了全套方正字体的用户，可以一键`[fontset=founder]`使用全套方正字体配置。

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

首先是寻找字体，代码寻找字体需要使用字体的系统名称，在Windows中，简单的查找系统字体方法是运行`fc-list`命令。注意$\LaTeX$只能找到$\LaTeX$内安装的字体和`C:\Windows\Fonts\`目录下的字体。因此安装字体时，需要选择*为所有用户安装*。

不知道字体系列名时，可以用系统命令`fc-list >> fonts.txt`生成一个字体表文件进行查找。增加`:lang-zh`参数可以指定检索中文字体。

确定**英文系列名**时，可以用`fc-list | Select-String "系列名"`来筛选字体列表。注意中文字体名可能会是乱码，这里建议只用英文名进行检索。

这里使用开源字体*Vollkorn*系列举例，`fc-list | Select-String "Vollkorn"`得到的结果如下

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

其中`:`和`:style`之间的即为字体在系统里的名称。对于非主字体，使用`字体名 风格`进行指定，如`Vollkorn Semibold Italic`。切记区分大小写，有的字体里会是`SemiBold`，有的是`Semibold`。

注：一些字体名中含有`-`，在打印时会增加转义符会显示为`\-`，使用这些字体时输入`-`即可。

## 基础字符字体配置

$\LaTeX$很有意思的一点是，它的字体配置是**只对部分字符生效**的，可以彻底分开配置并叠加指定。

我们先说基础字符。`ctex`包只对中日韩三语起效，其他语言的字符（不止为ASCII，还包括章节符$\S$和摄氏度$\textcelsius$）都是使用默认字体渲染的。对这些字符，只有`fontspec`包配置的字体才能起效。

```latex
% 引用包
\usepackage{fontspec}
% 设置主字体
\setmainfont{Vollkorn}
% 无衬线字体和打印机字体这里略过，本来也不好用
```

用`\newfontfamily`配置新的字体。

```latex
% 设置字体，并自定义字体名
\newfontfamily\medfont{Vollkorn Medium}
```

配置名为字体时，$\LaTeX$默认寻找同系列的字体作为其加粗和斜体，但可以自行进行指定。

```latex
% 设置字体，并自行配置加粗和斜体
\newfontfamily\medfont{Vollkorn Medium}[BoldFont=Vollkorn Semibold, ItalicFont=Vollkorn Semibold Italic]
```

使用非主字体时，只需要输入配置时设定的字体名即可。

```latex
\begin{document}
% ...
\medfont semibold text
% ...
\end{document}
```

## 中文字符字体配置

中文字符，如`你`，`我`，`；`（中文分号），`“”`（中文引号），均需要使用`ctex`包内的命令进行字体配置。在引入包时，需要用`[fontset=none]`避免加载默认字体集产生冲突。

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
\newCJKfontfamily\songti{Source Han Sans} % 思源黑体

\newCJKfontfamily\shusong{FZShuSong-Z01}% 方正书宋
\newCJKfontfamily\fangsong{FZFangSong-Z02} % 方正仿宋
\newCJKfontfamily\heiti{FZHei-B01} % 方正黑体
\newCJKfontfamily\kaiti{FZKai-Z03} % 方正楷体
```

其中，方正系列四个字体都只有一个字重，而思源两个系列都具有extralight, light, regular, medium, semibold, bold, heavy七个字重，可以进行指定。所有字体中都不含斜体。

实际使用时，建议将方正书宋或思源宋体Regular作为主字体，这样易读性较好。两种字体的根本区别在于，书宋是完全针对书籍印刷设计的，印出来效果最好，正因如此，被大量出版社采用，看起来会很眼熟；思源宋体在屏幕显示和印刷之间端了水，印出来的效果略逊于书宋，但是不会那么眼熟。字重上，书宋略重于思源宋体Light，略轻于思源宋体Regular。

使用上，思源宋体可以自行指定粗体的程度；方正书宋只有一个字重免费，注意不要用加粗，固然技术上可以将较粗的思源宋体作为粗体使用，但因为细节差异众多，看起来会非常难受。

不管用什么主字体，都推荐指定方正楷体作为斜体，以便于在正文中标注少量字符（如引用）。

各级标题建议使用不同字重的思源宋体，装饰性文字（脚注、页眉等）使用方正仿宋或楷体。

注：由于Windows系统的渲染问题，在Windows电脑上面的宋体就没有好看的，建议将文档传到其他设备上检阅效果。

## 英文字符配置中文字体

大部分中文字体都含有英文字符设计，想中英文使用同字体的话，将其用`fontspec`包内命令加载，然后叠加使用即可。

```latex
\newfontfamily\songtien{Source Han Serif}

\songti\songtien 中英文mixed文本
```

## 字体找不到的常见解决方案

第一步，确定字体确实安装在了`C:\Windows\Fonts`文件夹里。

第二步，检查拼写和`fc-list`命令获得的一样，特别是大小写。

第三步，在字体外面加个中括号。别问为什么，我也不知道，总而言之亲测有效。

```latex
% 修改前
\newCJKfontfamily\songti{Source Han Serif SemiBold}
% 修改后
\newCJKfontfamily\songti{[Source Han Serif SemiBold]}
```

第四步，天涯何处无芳草，字体到处都是，换一个吧。

# 建立文档

相信在前文中，读者已经建立过一些测试文件来研究代码了，在这一节中，我们所讨论的是正经的本子文档。

## 文档类型和字号

```latex
\documentclass[10pt]{book}
```

$\LaTeX$原生有着`article`、`book`、`report`三种文档类别，对应的`ctex`类分别为`ctexart`、`ctexbook`、`ctexrep`。三种类别的主要区别在默认层深和排版方式上，虽然排版之后肯定要自己改，但为了直观，本教程推荐使用`book`类。

`book`类默认支持三种字号10,11,12pt，pt即为磅数。三种字号可读性都属不错，不建议更大或者更小。具体选择时，可以用“磅数÷2.845=毫米数”来计算文字大小，也可以参考word。word中的五号字是10.5磅，小四则是12磅。

`ctex`文档类别支持word款的两种字号，配置方法如下

```latex
% 正文五号字
\documentclass[zihao=5]{ctexbook}
% 正文小四号字
\documentclass[zihao=-4]{ctexbook}
```

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

## 自动空白页

`\chapter`及以上级别的标题会自动新起一张纸。`book`类文档中，默认为双页模式，右页为新纸。当上文结束在奇数页时，会产生一页空白页。不想要的话，可以在定义`documentclass`的时候增加一个参数`openany`，允许在偶数页开启新内容。

```latex
\documentclass[...,openany]{...}
```

相对的，如果在使用了`openany`参数后，希望某页在右页上开始，则可以使用`\cleardoublepage`命令。该命令会自动插入空白页，使后续内容从下一个右页铺开。

`\clearpage`命令可以使后续内容从新的一页上开始，类似于`\newpage`。

## 行高和段距

行高：上一行的底边到这一行底边的距离；行距：上一行底边到这一行顶边的距离。

段距：换段时，在行距基础上额外增加的距离。

段距应为**行高的整数倍**（包括0），不然特别的丑。

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

字号就是文字高度。

其中，定义好的三个命令以文字高度为基础值，即，单倍行高会使得行高等同于文字高度。

但自定义行高的机制则不然。`\setstrectch`的基础倍数为**字号的120%**。对于10pt的文档字号，`\setstrectch{1}`会使得行高为12pt，其他倍数时也是以12pt为1倍计算的。

这些方式都会使`\baselineskip`（记录正文行高的变量）自动跟着变化，可以以此为参数设置缩进。

### 段距

改变`\parskip`即可，该变量指两段之间普通行距之外的额外空白，默认为0。

```latex
\setlength{\parskip}{段距}
```

使用时，最好不要只给一个数，容易导致每页出现大量`Overfull/Underfull \vbox`错误，解决方法有两种。

1. 设置段距时，给出弹性空间。不要让最短段距低于0，会使得段间空白小于行间。
2. 使用命令允许每页下缘不齐。不推荐，在页面布局做不到行对齐时，该命令会使得整体看起来像狗啃的一样。

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

## 文档内跳转

虽然是按印刷品的标准的制作，但是为了检阅方便，还是建议使用`hyperref`包来启用超链接跳转。

超链接会带来格式的变化，可以使用一条命令来避免。

```latex
% 启用超链接
\usepackage{hyperef}
% 超链接不影响格式
\hypersetup{hidelinks}
```

# 注释

## 脚注

页底脚注可以`\footnote[编号]{内容}`命令来添加。

引入`footnpag`包可以在每页重置脚注编号。

```latex
\usepackage{footnpag}
```

脚注所使用的字体可以自行设定，方法如下

```latex
\usepackage{etoolbox}
\makeatletter
\patchcmd{\@footnotetext}{\footnotesize}{【字体和字号的命令】}{}{}
\makeatother
```

## 尾注

建议使用`endnotes`包来管理尾注。

添加尾注使用`\endnote[编号]{内容}`，在文章任意地方使用`\theendnotes`命令输出尾注。第二次使用`\theendnotes`会输出第一次输出后新增的尾注。

尾注标题使用以下进行修改。

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

对于`book`类而言，文档随着进行会自动更新两个标，以便于在页眉页脚中使用。其中`\leftmark`记录章名，`\rightmark`记录节名。

`\Xmark`默认为`X 序号. 目录中的标题名称`，可以用重定义的方法来去除章标记中`X 序号.`的部分，节标记同理。

```latex
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
```

## 页面风格使用

在文档中使用`\pagestyle{风格名}`命令设置这一页起的风格。

使用`\thispagestyle{风格名}`设置当前页的风格，下一页自动还原。

`fancyhdr`包提供`fancy`，`plain`，`empty`几种内置风格。

`fancy`：页眉外侧角落偶数页为`\leftmark`，奇数页为`\rightmark`，页脚中央为`\pagenumber`。

`plain`：页脚中央为`\pagenumber`。

`empty`：什么都没有。

## 问题处理

对于由于标题位置而补充的空页，其页面风格默认与前文相同，可以使用引入`emptypage`包，使得空页面上不显示页眉页脚。

页眉下默认有一条横线，可以用以下命令来设置横线宽度，0为去除。

```latex
\renewcommand{\headrulewidth}{宽度}
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
% 下一页，也可用\vfill或\cle实现
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
% 宽度为0的rule命令可以在破折号左右固定留白
\rule{0em}{0.15em}{0em}\rule[0.35em]{1.7em}{0.03em}\rule{0em}{0.15em}{0em}
% 用\hspace命令来生成左右空白，可以允许留白被挤压
\hspace{0.15em}\makebox[1.7em]{\rule[0.35em]{1.7em}{0.03em}}\hspace{0.15em}
% 直接把破折号用盒子框起来也是个办法
\makebox[2em]{——}
```

## 特殊字符换字体

对于个别字符，你可能不满意它的默认字体，（例：在思源宋体中，间隔号·的宽度大约为一个空格的宽度，而非应有的一个字，但方正书宋中则不会出现这个问题，因此如果主字体选用思源，将间隔号专门设置为书宋会合适一些）。可以用如下写法进行修改。

给它起名`\mysymbol`，在全文中将中文字符替换成`{\mysymbol}`，大括号防止文字粘连。

设定函数，让`\mysymbol`用指定字体渲染。注意大括号需要有两层，限制字体应用范围。

```latex
\newcommand{\mysymbol}{{\symfont 符号}}
```

## 行溢出

行溢出，即`Overfull \hbox`警告。可以增加一个`sloppypar`域来一劳永逸地解决，即

```latex
\begin{document}
\begin{sloppypar}
内容
\end{sloppypar}
\end{document}
```

但这样的解决方法会导致某一行字距过大，影响观感。

更优雅的解决方法是调整文本，增减几个字或标点来解决问题。

## 纸面不充盈

即`Underfull \vbox`警告。该警告出现是因为某页前一部分内容不足以填充页面，后一部分内容又所需内容又过多，致使页面无法容纳。

调整行宽、行高、段距等基础布局数值，都可能产生或解决该警告。可以在合适的地方进行手动换页（`\clearpage`或`\newpage`）解决。但由于这样的手动解决方案不是很优雅，所以应当**在排版过程的最后**进行此调整。

## 扉页

虽然可以选择用`\maketitle`命令生成一页现成的扉页，但是真的很丑。中文出版物的扉页通常是封面的黑白朴素版，内外呼应，我个人推荐按此办理。根据封面的设计来手动布局，或直接导出一页适于黑白印刷的封面pdf文件（注意出血），插入正文开头作为扉页。

```latex
\usepackage[pdfpages]
\begin{document}
\includepdf[
    pages={1,2},% 插入文档的第一页、第二页
    angle=0 %逆时针旋转45°
    ]{文件名}
\end{document}
```

## 子文件

最简单的方法是用`\input`命令，将另一个`.tex`文件引入当前文件，效果相当于用该文件的全部内容替换`\input`这一行。善用该命令可以实现内容与格式的代码分离，便于管理。

```latex
% 子文件，head.tex
\documentclass[10pt]{book}
\usepackage{hyperref}
\hypersetup{hidelinks}

% 主文件，main.tex
\input{head}
```

对于较厚的本，可以使用`\subfiles`来拆分出子文档，使用该包可以在不影响整体编译的情况下，独立编译子文档。由于换页的位置会直接影响效果，每个子文档头尾都应当有换页机制。

```latex
% 子文件，在main.tex同层级的Chapter文件夹内创建的ch1.tex
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

`subfiles`包有时会出现一些bug，如果主文件和子文件渲染出来有页码之外的区别的话，大概就是原生bug造成的。如果调整不出来的话，可以釜底抽薪，删除开头结尾的`document`相关声明，改用`\input`引入。
