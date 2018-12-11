
## 对我个人来说，搭个博客，最基本的需求就是：

1. 有一个个人链接，呈现一个看起来不那么low的页面
2. 能够像文件系统一样，可以一层层的创建路径，分门别类的存放自己的文档
3. 能够用链接把自己的文档组织起来，通过网页进行浏览

这几项需求，目前看来，直接使用github pages就可以实现了，完全不需要涉及其他的东西，网上那些个攻略，搞得那么复杂，怕新人不会被劝退么

## 创建一个基本可用的github pages以下几步就可以了

### 创建repository
---
点击github吉祥物章鱼猫，跳转到你账号的总览界面，点击new repository创建新的repository。

设置repository name格式为 **你的账号昵称.github.io**

选择初始化一个readme

选择create repository

创建完成

### 设置repository
---
进入新建的repository，选择settings  
在settings栏下拉，可以看到有个github pages的配置
在上一步设置repository name时，如果命名格式是正确的，这里应该会有显示一句 

`Your site is published at https://xxx.github.io/`

如果没有，就返回页面上方重新设置repository name

下面选择choose a theme，选择一个主题。github pages提供的几个主题都挺好看的，随便选一个就可以了，以后可以换

### 选择github pages的使用方式
---
选择theme完成后，你的代码仓库里存在两个文件：

README.md  
_config.yml

README.md里教你使用markdown和jekyll去玩转github pages，但是对于新手<del>的我</del>来说,立刻玩转这两样东西，是不现实的。jekyll的主题我也下载测试了，根据教程配置后，出了不少问题，因为头一次接触这些，也找不到原因

_cofnig.yml里就就一句代码  

`theme: jekyll-theme-cayman`

指定了使用的主题

- 有前端经验的可以使用README.md提供的方式来自由的配置
- 像我一样没有经验的，只需要熟悉下markdown的基本语法，只通过markdown来创建blog

### 一些基本操作
- 创建新文档  
直接使用github的create new file创建.md后缀的文档即可  

- 创建新路径：创建新路径，可以通过create new file创建  
`新路径名/README.md`， 即，需要创建一个test路径，通过创建一个   `test/README.md`  
实现，需要注意，路径名不能为中文，`README.md`文件内可以编写本路径各个文档的链接

- 链接其他文件
直接使用markdown的超链接语法即可，如果需要链接其他路径的文档，可以使用相对路径和绝对路径  
相对路径可以使用 `.` 或者 `..`进行路径切换
绝对路径需要加上 `xxx.github.io/`, 即你的blog的repository name

