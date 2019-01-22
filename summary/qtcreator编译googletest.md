# google test使用qtcreator编译
---

## googletest源码下载
---
gtest下载路径：github地址  

    https://github.com/google/googletest

选择需要的版本并下载到本地，解压

## 创建 googletest 的qtcreator工程
---
解压googletest后，在googletest文件夹内，创建qmake的`.pro`文件  
并在空白的`.pro`文件里添加以下配置代码

    CONFIG   += c++11
    
    TARGET = gtest
    TEMPLATE = lib
    
    DEFINES += QT_DEPRECATED_WARNINGS
    INCLUDEPATH += "./include"
    
    SOURCES += src/gtest_main.cc\
    src/gtest-all.cc \  
保存后关闭.pro文件，工程便创建完成了

## 编译 googletest 
---
使用qtcreator打开工程，选择刚才创建的`.pro`文件  
选择构建套件，并打开工程  
执行工程编译，完成googletest的编译工作，在工程上一级路径下，会出现qtcreator的构建路径，其中存在编译完成的库文件  

---
> 该部分内容根据 [Qt使用gtest](https://www.cnblogs.com/lt450196683/p/6773457.html)文章整理，并在qt5.11.1 + mingw环境下完成编译过程
