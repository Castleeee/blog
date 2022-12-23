---
title: clickhouse-1
date: 2022-06-07 15:49:50
prev: false  
next: false  
category:
- 大数据🐘
tag:
- clickhouse
---

<!-- more -->
````toc
:::
<div align="center"><h1><strong> clickhouse-1</strong></h1></div>

定位是OLAP离线处理,真列式存储数据库，没列一个文件，使用场景数据量很大，单次导入分析，查询多响应快修改少。  
对系统资源尤其是内存和CPU消耗大，简单的查询占用也不低，最好作为单独机器单独数据仓  
- [文档](https://clickhouse.com/docs/en/intro)  
- [playground](https://play.clickhouse.com/play?user=play)  
- [官网源压缩包](https://repo.yandex.ru/clickhouse/tgz/stable/)
## 安装
clickhouse一共有四个组件，`clickhouse-common-static`，`clickhouse-common-static-dbg`，`clickhouse-server`，`clickhouse-client`,下载对应版本的就可以，下载解压完后分别进入四个文件夹中的install文件夹，运行`doinstall.sh`脚本就完了。
#TODO 不知道原因，我没有clickhouse-server和client命令，但是直接clickhouse server client是可以的  
默认端口9000，默认用户default



