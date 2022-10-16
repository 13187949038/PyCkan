# PyCkan
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

## 这是干什么的？

​	项目名称中的Py代表*Python*，Ckan*代表The Comprehensive Kerbal Archive Network（全面的坎巴拉资源网络）*

> 注意：您是否正在寻找名为 CKAN 的开放数据门户软件？如果是这样，可以[在此处](https://github.com/ckan/ckan)找到他们的 GitHub 存储库。

​	CKAN的[主线](https://github.com/KSP-CKAN/CKAN)由于采用 C# 进行编写，在其他平台（如Linux）上往往需要通过mono等方式运行，代码要求编译故难以维护，PyCkan的目的是兼容 [CKAN数据规范](https://github.com/KSP-CKAN/CKAN/blob/master/Spec.md)，并能够在各平台上提供原生可执行程序（使用 *Nuitka* 进行打包）。

​	请注意，PyCkan的目的并不是取代CKAN主线，PyCkan只是为CKAN主线提供了另一种高效的模组安装方式。

## 许可证相关

​	注意！本项目采用多许可证，使用本项目前，您需要同时遵循 *Anti 996 License* 和 *LGPL v3*，并且二次分发时不得删除/更改 *Anti 996 License*。

## 新开发者指南

### 开发环境

​	推荐使用 VSCode/Pycharm 进行开发

​	缩进：4 spaces

​	换行：LF

> VSCode插件推荐：Todo Tree、vim、Python、pyLance

### 分支

#### 用途

​	develop：开发使用

​	master：主线

​	feature\_*xxx*：主要功能开发完成后，如要新增功能，创建一个 feature\_*xxx* 分支来进行开发，该功能开发完成后将本分支*变基（rebase）* 到 *develop* 分支上

#### 注意

​	提交到 master 分支前，请通过`pip freeze > requirements.txt` 导出依赖项，如合并时忘记导出依赖项，请勿通过 *改写（amend）* 来修改已经 *推送（push）* 的提交（本地提交可以直接通过 *改写（amend）* 来修改），而应当新增一个提交，并在注释中添加如下内容：

```
修补：<新增|删除|修改> <文件>
```

#### 类规范

​	大部分类应当有一个唯一 id，此 id 应当通过类相关信息生成，而非通过随机数生成！

#### 文件头

​	所有在 *master* 分支上的提交，都应当采用如下格式进行署名！

```python
示例：
"""
项目：         PyCkan
许可证：       LGPL v3    Anti996
作者：         胖虎		  哆啦a梦
最后一次更新：  13:58      2022年10月16日星期日
新建：         12:00      2022年10月16日星期日
"""
```

​	注意：所有时间都应当使用 **<span style="color: red">协调世界时（ UTC ）</span>** 进行书写，方便各地区的协作者查看！
