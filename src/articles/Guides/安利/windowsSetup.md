---
title: windows设置备份
date: 2022-02-09 19:24:45
---
````toc
:::

最近想重装一下电脑，重新组织软件和资料，万一坏了电脑重装也不至于因为东西太多而耗费太多精力。保持工作环境一致，提高效率不浪费时间。顺带分享一下自己用的日常软件和win10美化调教。
<!-- more -->

## 重装前注意事项
重装必然会格盘这个不用说，所有的更新和预览版会失效重新下载，存储的ssh本机公钥私钥会消失需要重新生成。注意资料都保存一下不要弄没了。我使用的是Win10专业版，先安完然后让他自己更新系统，更新为最新版之后再开始安软件，不然会出现奇怪的兼容性或者损坏之类的。  
::: warning Warning
重装好的系统没有网卡驱动，不能自动连wifi  
:::
## 空间分配
C盘至少给80个G，我的surface上给了78个G，电脑上给了85，可能surface系统是定制的，占用小一些。除了所有要求装在C之外的软件，剩下的都扔到其他盘，常用的需要加载的(美工，编程，办公)放在D,游戏，资料，桌面，系统文档等放在机械E盘。

## 基本步骤
::: tip 📌Tip
步骤拆解成好几步，每一步都是一组操作，目前我按照这个顺序弄的
:::

<font color=#008c9e size=4>

1. 更改windows本身的设置
2. 安装MS商店原生APP，火狐，谷歌
3. 魔改默认设置
4. 体验增强
5. 安装办公软件
6. 安装通讯和下载软件
7. 依次安装实用工具，编程工具，网络工具
8. 安装美工软件
9. 安装编程环境
10. 安装编程软件
11. 美化windows
12. 优化启动和服务

</font> 


## windows本身的设置
### 设置
1. 设置默认`关闭屏幕不休眠`，可以连接外部显示器
2. 开始`更新系统`，当系统显示为最新版的系统时就可以开始设置了，过低的系统不能更新，搜那个错误码微软回答里会给出一个方案用Assistant升级
3. 电脑用的是英文版，先在控制面板设置中把`地区改为China`
4. 右键我的电脑->高级设置名字设置为一个纯英文的（中文写程序会有BUG
5. `任务栏`用大任务栏，去掉除多任务视图和文件管理器以外的任何东西，锁定任务栏
6. 设置从头开始设置一遍设置，并且安装好火狐和Chrome，把火狐设置为默认
  - `系统` 关闭更新后向我显示。。，电源通电时改为永不睡眠，关闭 平板模式下隐藏图标，关闭时间线中显示建议，剪贴板历史记录 关
  - `设备` 蓝牙不用的话关闭，自动播放关闭。
  - `网络` 更改适配器设置->wifi->属性->配置->高级->wifi频率。Auto，看情况设置
  - `个性化` 显示锁屏界面的应用 天气闹钟和日历，使用全屏开始菜单，关闭向我显示某些建议，任务栏已满时合并，壁纸设置 图片/wallpaper 文件夹
  - `应用` a.删除 3Dviewer 3Dbuidler feedbackhub MSNews MSSolitaireCollection MSmoney 自带的office print3D Skype Sports Tips Yourphone 然后默认Email设置为Outlook，浏览器设置为火狐，自动升级地图，离线地图存储在E，下载中国的，网站应用全关掉，开机启动全关掉。
  - `账户` 登陆你的MS账户
  - `时间和语言` 自动设置时间，地区中国，英文系统记得把时间设置为EnglishUS，地区设置为中国，在控制面板设置的时候不要勾选尝试使用utf-8，会乱码
  - `xbox` 能关的全关
  - `轻松使用` 光标2指针1黑色指针，讲述人全关启动选项全关，关闭滞粘键切换键和下面的什么键都关。
  - `小娜`关掉热键呼出
  - `搜索` 筛选少儿不宜关掉，云搜索历史搜索关掉，确保经典模式
  - `隐私` 关闭windows跟踪应用，诊断反馈都关闭，反馈频率从不，历史活动记录全都停止存储，权限设置看应用需不需要设置开关。
  - `更新` 保持最新最好，传递优化开 本地和网络上的电脑，Windows安全全删了，开发者选项-开发者模式，不要加入预览者计划。

7. 进入`控制面板`,修改
  - 卸载Vulkan图形接口，不卸载也行。特性，开启 。net3.5，4.8，虚拟机平台，powershell2.0 IE11
  - `时间和地区`，时区东八区，地区一定选中国，其他随意
  - `电源电池高性能`，盒盖不休眠
  - `安全`-用户安全控制等级最低不提示。
  - `控制面板`->系统和安全设置->windowsDefender->改变通知设置，不提示我，关闭WDF。

8. 编辑右下角通知栏快捷方式

## 常用软件
### MS商店
在MS商店中值得安装的:
- **weibo plus**(搜weibo就能搜到)
- **snipaste** 截图好帮手
  - 使用HEX大写HEX开机启动管理员启动增强托盘按钮，快速保存到桌面
- **soundEditor**(PC上用AU不用安)
- **哔哩哔哩UWP**
  - 这是个第三方的WUP，第一方的不如这个好用
  - pin把那个视频av70553533到开始菜单
- **pixiv** UWP（长得像office的图标哪个）
- **必应词典**
  - 登上自己的MS账号，下载本地缓存包
- **Telegram**(电报)
- **slack**(团队协作)
- **Termius**(超好用ssh终端界面)
  - 字号调大(14)，右键粘贴
  - 服务器添加KnownHosts
  - 不能开启本地回环，这个软件会连不上网
- **Trello**(团队协作板)
- **Ubuntu** 18.04(WSL)
  - 在我[另一篇](windows子系统.md)里有介绍
- 萌娘百科UWP
- **wechat**（微信）UWP微信只能扫码登陆，傻吊设计，需要先登陆一次
- **QQ音乐**(不常用)
  - 品质-极高，下载目录是music
- **网易云音乐** 有时候会崩溃，不能最小化其他与正式版无异
- **ACGplayer**
- **MPEG-2 Video Extension**
- **Web Media Extensions**
- **QQ**
  - 只有很少的功能，消息显示有BUG，群不好屏蔽，设置无法同步，不能显示表情包，粘贴图片会直接发送，打字没法换行，传送文件只能单个传送，一定几率会失败，大文件一定会失败。
  - 启动快，适合那种查看完消息就关的场景，实际使用十分频繁

### 办公软件
- office+visio
  - 我用的是2016+visio，KMS，记得全安完之后再用KMS激活，Visio要用神龙KMS，有时候也不行，visio难搞，记得断网
  - 淘宝买个Key
- WPS没必要，用到再说，原生很好用。
- Acrobat
  - 也是安完之后移动完之后再打补丁，默认用SumatraPDF阅读，用Acrobat编辑批注和格式转换
- SumatraPDF<a href="https://github.com/sumatrapdfreader/sumatrapdf">开源</a>超级轻的PDF阅读器，只能阅读，适合配置低的机器，批注啥的还是Acrobat。

### 通讯和下载
1. 百度网盘
  - 下载默认目录为download，去掉完成后气泡提示，去掉提示备份照片，线程数拉满，开机启动关闭，我的电脑中显示百度网盘关闭。
3. 迅雷老版
  - 这一版迅雷很珍贵，官方已经不发行了,但是没广告启动快能下载,提示你升级死活不要升,保留安装包，多多传播。
  - 这个迅雷会自己突然流氓更新，解决办法是当他一次更新中间，迅速断网别让他更新完，然后到  迅雷目录你会发现产生了一个ThunderPsuh，复制他的名字然后删掉文件夹，新建一个txt，重命名为刚才复制的名字，不保留后缀名，右键属性只读，安全把所有用户所有权限都禁了，世界清静了。
  - 在设置中目录放到download，关闭在windows中设置迅雷下载库，高级设置中线程数刷新数缓存拉满
4. QQ+Tim
  - 照片保存到picture，传输文件保存到download，QQ乱七八糟的订阅取消，不要安装flash
  - 安全模块提醒我不自动安装，防钓鱼禁用。


### 游戏平台
暴雪<a href="https://www.battlenet.com.cn/account/download/">战网</a>,
<a href="https://store.steampowered.com/about/">steam</a>,
<a href="https://www.origin.com/hkg/en-us/store/download">烂橘子</a>，游戏都安在机械盘


##  魔改默认
### 修改文件
- **intel核显**关闭网络键盘，关闭热键，把勾全去了不显示通知，不显示小图标，然后退出
- **英伟达控制面板**，所有能启用独显的地方都设置为独显优先，关闭托盘图标和右键菜单，退出。
- 设置->存储->更改新内容保存位置，全都选E盘.在E盘新建Download文件夹（有必要的就新建一个Desktop），然后我的电脑打开就有的七个文件夹除了3D对象都移动过去，属性->位置->移动（把文件一块移动过去）
- 先进入安全中心，然后管理实时保护，关闭实时保护，再通过组策略禁止windowsDefender和Onedrive，更新组策略。
- 用win10小工具禁用defender，卸载Onedrive和原生应用。
- 编辑host(C:\windows\system32\drivers\etc),加入 ***0.0.0.0 account.jetbrains.com 和 127.0.0.1 www.xmind.net***
- 关闭安全警告，自行百度
- 开启WSL，链接<a href="https://docs.microsoft.com/zh-cn/windows/wsl/install-win10?redirectedfrom=MSDN">在这</a>，配置WSL在这。
- WindowsLoopbackManager或者使用Fiddler中的config，修改本地回环使得UWP应用能使用本地的网络。
### 默认文件app
1. pdf默认使用SumatraPDF
2. 视频类默认用自带的movie
3. 音频类用GrooveMusic
4. 默认使用火狐，调试使用Chrome
  1. 火狐默认使用mijisou作为引擎，同步我的设置
  2. 安装mijisou插件，启用主题，删除多余标签，修改主页启动页，定制工具栏。
  3. about:config->browser.safebrowsing.downloads.enabled改为false
  4. Chrome同步我的Chrome，主要是安装Yapi和postman等调试工具
5. tim和QQ一起用，大部分用Tim，Tim不支持的用QQ，设置看通讯和下载
### 删除原生应用
使用win10工具箱里的黑色猫头能删除。  
禁用defender右键，删除Onedrive  
顺带在组策略里禁用

## 编程环境
::: tip 📌Tip
不是程序猿就不需要安装编程环境和编程工具，网络工具
:::
### IDE
Jetbrain全家桶，设置直接导入。有一个专门为rubu准备的  
版本:
- CLion 2018.2.5
- GoLand 2018.3.2
- IntelliJ IDEA 2018.3.2
- PyCharm 2018.2.4
- Ruby Mine 2019.1.1
- WebStorm 2018.2.5

使用之前先修改换缓存数据位置  
修改idea.properties的配置
```
#---------------------------------------------------------------------
idea.config.path=D:/Program Files (x86)/JetBrains/IntelliJ IDEA 2016.1.3/config

#---------------------------------------------------------------------
# Uncomment this option if you want to customize path to IDE system folder. Make sure you're using forward slashes.
#---------------------------------------------------------------------
idea.system.path=D:/Program Files (x86)/JetBrains/IntelliJ IDEA 2016.1.3/system

#---------------------------------------------------------------------
# Uncomment this option if you want to customize path to user installed plugins folder. Make sure you're using forward slashes.
#---------------------------------------------------------------------
idea.plugins.path=${idea.config.path}/plugins

#---------------------------------------------------------------------
# Uncomment this option if you want to customize path to IDE logs folder. Make sure you're using forward slashes.
#---------------------------------------------------------------------
idea.log.path=${idea.system.path}/log

```
再迁移C盘的数据到对应的位置即可。    
去掉SearchEvery,两下shift切换输入法很容易呼出  
打开 lib/resources.jar/idea/PlatformActions.xml,删除或注释掉
```
<action id="SearchEverywhere" class="com.intellij.ide.actions.SearchEverywhereAction" />
```

VScode从Anaconda里面安装，同步插件(setting sync)登上你的github，然后回到文件界面，`Shift+Alt+D`

### 语言
所有的编程语言都要预留出一个层级目录来，不然后面装很多东西会乱。

#### Python
1. 不要用原生的直接Anaconda，会帮你解决一大堆问题，记得django和python要加入系统路径
2. 安装必要包，更换豆瓣源
  - win+R 打开用户目录%HOMEPATH%，在此目录下创建 pip 文件夹，在 pip 目录下创建 pip.ini 文件
```
[global] 
timeout = 6000 
index-url = https://pypi.douban.com/simple 
trusted-host = https://pypi.douban.com
```
- 安装eric和Qt配合pycharm编写界面看<a href="/docs/blog/front/pyqt.html">这一篇</a>

#### JAVA
1. 调试好java和javac命令，对接好IDEA跑个hello world就行了
2. 加入系统路径
  - (1)新建->变量名`JAVA_HOME`，变量值`C:\Java\jdk1.8.0_05`（即JDK的安装路径）
  - (2)编辑->变量名Path，在原变量值的最后面加上`;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin`”
  - (3)新建->变量名 `CLASSPATH`,变量值`.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar`
#### C/C++
1. cygwin安装配置和调试
2. 看这篇<a href="/blog/back/C和Cpp/environment.html">C环境配置</a>
#### Ruby

看这篇<a href="/blog/back/Ruby/美丽的ruby.html">环境配置</a>
#### Nodejs+web
依次运行
```
npm install -g cnpm --registry=https://registry.npm.taobao.org
npm install -g yarn
//更心淘宝镜像源，不更新也行
yarn config set registry https://registry.npm.taobao.org
```

修改全局包的存放位置  
查看配置：  
`npm config ls`  
修改目录：  
`npm config set prefix "E:\nodejs\npm"`  
`npm config set cache "E:\nodejs\npm\cache"`  
添加环境变量：  
`E:\nodejs\`  
`E:\nodejs\npm`

#### Golang
### Other
- <a href="https://git-scm.com/downloads">git</a>+<a href="https://tortoisegit.org/download/">tortoiseGit</a>+<a href="https://www.gitkraken.com/download/windows64">Gitkarken</a>用git管理项目
  - git config --global user.name "xxxxx"
  - git config --global user.email "xxxxxxxx@qq.com"
  - git config --global core.editor vim
- <a href="https://www.docker.com/products/docker-desktop">Docker</a>
  - 设置docker存储文件位置,控制面板->管理工具->HyperV管理->虚拟机右键设置，把vhdx复制到你想要移动到的目录，然后在设置中浏览选中。
  - 在Dockerdesktop中设置取消自启取消自动更新不要发送数据，DiskImagelocation修改到刚才的目录
  - `export DOCKER_HOST=tcp://127.0.0.1:2375`加入.zshrc
- <a href="http://graphviz.org/download/">graphviz</a>支持图形可视化的
- <a href="https://ffmpeg.org/download.html">ffmpeg</a>支持视频解码编码
- <a href="https://phantomjs.org/">phantomjs</a>爬虫的无界面浏览器

## 美工软件
我用的是CC2017，如果性能太弱就去找CS6。CC默认会给你装再C盘中，切记当你装完所有Adobe家的东西的时候再移动到其他盘。使用软链接链接到C盘，这样ME就能渲染了
### 我的surface
- PR(带转场) PS AI Acrobat
### PC或笔记本
首选项->媒体缓存打开一遍都设置为新建一个文件夹，不要在C。其他不用动，PS和LR汉化
- PS
  - 字体
  - 滤镜
  - 如果出现语言错误就用另一个
- AE
  - 滤镜
  - 特效
  - 插件
- PR
  - 转场插件
- AI主要用来编辑一下SVG
- ME
  - 移动至其他盘后会导致ME找不到路径无法渲染，使用软连接链接到C盘，测试能否渲染。
- DW
  - DW使用的CS6版本，和其他全家桶不一个版本，因为耗资源太多
  - 不常用太老了，不过还是放上吧
- ID
- AU
- LR
- Acrobat
  - 这个被归类到常用软件里去了
  - 版本我也不知道哪个，安装包收集到了
  - 同样也是安完了剪切到另一个盘
### 卸载掉CreativeCloud
- 首先打开CreativeCloud，把里面能关的全关了，啥自动更新，开机启动联网检测之类的。
- 使用<a href="https://helpx.adobe.com/cn/creative-cloud/help/uninstall-creative-cloud-desktop-app.html">官网工具</a>卸载程序卸载掉
- 使用<a href="https://helpx.adobe.com/cn/creative-cloud/kb/remove-cc-files-folder-shortcut-navigation-panel.html">官网工具</a>删除系统内添加的AdobeCC文件夹
### 移动到D
所有的东西按完之后用软连接移动到D，最好用PE这样就不会出现没有移动干净的情况，移动完之后使用ME渲染一次如果成功了就行了
```
mklink /J D:\dest  D:\source
mklink /J "C:\Program Files\Adobe" "D:\Adobe\Adobe"
mklink /J "C:\Program Files\Common Files\Adobe" "D:\Adobe\Common Files\Adobe"
```
### cooledit
这个软件可以简单去人声。步骤留坑以后整理
### 达芬奇&C4D-R18
也是安装完之后剪切到D盘。这俩软件一般用不到，留个资源充个数而已，可以不安用到了再说。
## 工具
### 编程工具
1. `RedisCX` <a href="https://github.com/Sidfate/redisCX/releases">开源的</a>用来管理Redis的GUI工具
2. `xmind`分为zen和8。  
   - zen:有大纲视图，好看，导出的视图和分级比8好看。不能另存图片出来，导出word会失败无法打开，导出时无法一块导出图片。 断网先打补丁，剪切到D
   - 8：丑。
3. `starUML`开源不过高级功能要钱的UML画图工具，<a href="http://staruml.io/">官网</a>可以下载,<a href="https://github.com/staruml">github</a>有对应语言的插件
  - 剪切到D
4. bat启动anaconda,从pycharm启动太慢了，直接做个bat吧，太简单还不会的不教自己悟。
5. `Navicat Premium`管理sql
6. `devc++`，没啥好说的，用的时候用就是了。
7. <a href="https://notepad-plus-plus.org/">`notepad++`</a>这货作者是个台du,但是目前没有比这个好用的纯文本编辑器。不要打开超过你内存的文本，不要安插件不要升级，基础功能就足够。
8. <a href="https://github.com/gephi/gephi">Gephi</a>基于jvm的科学作图软件
### 实用工具
1. `keePass2`用来管理密码的，<a href="https://keepass.info/">单机免费</a>管理密码，可以和mijisou通用一个格式
2. `ScreenToGif`<a href="https://www.screentogif.com/">免费开源</a>的录屏转Gif的工具。
  - 设置中文，开始前倒计时，文件夹和配置文件使用本地
  - 下载ffmpeghe Gifski(失败了从其他电脑上拷贝)
3. <a href="https://www.ccleaner.com/ccleaner">`CCleaner`</a>+<a href="https://www.chuyu.me/en/index.html">`Dism++`</a> 清理用的
  - 设置->不发送数据,语言中文
4. `FreeDownloadManager`<a href="https://www.freedownloadmanager.org/zh/">免费</a>的下载工具，可以代替吸血迅雷。
  - 语言设置中文，不自动安装更新，不捕获小于5120k的文件
5. `Captura`<a href="https://github.com/MathewSachin/Captura">开源</a>好用录屏机
  - 目录设置到video，语言中文，录制最小化，三秒启动
  - 设置ffmpeg文件夹到本身目录，下载解码器
6. <a href="https://www.utorrent.com/">`uTorrent`</a>代替吸血雷的BT下载器，免费版不要钱够用了
7. <a href="http://client.jijidown.com/">`jjdown`</a> B站视频下载器
  - 设置并行任务数，下载文件夹
8. `卡硬工具箱`<a href="http://www.kbtool.cn/">卡吧开发的</a>用来检测硬件配置的工具大合集
9. <a href="https://maruko.appinn.me/">`小丸`</a>十分好用小巧的视频压缩软件
10. <a href="https://calibre-ebook.com">`calibre`</a>电子书管理
  - 图书存放位置在 文档->Book
11. <a href="http://pandownload.com/">`pandownload`</a>网盘加速版
  - 保存路径Download，默认为下载路径，并行任务连接数满
12. <a href="https://www.ctfile.com/p/storage">`城通网盘`</a>指不定啥时候就用到的网盘
  - 任务数只能为1除非会员，设置下载目录Donwload播放器potplayer
13. `CNKI+CAJviewer`看论文用的,<a href="https://www.cnki.net/software/xzydq.htm#CNKIe-Learning">知网</a>下载
14. <a href="http://globalpotplayer.cn/">`potplayer`</a>韩国的，目前为止最强大的播放器。（丑是丑了点,倍速话音不同步就使用以下设置
  - 右键->滤镜->不使用DXVA
  - 右键->播放->优先运行权：高配置 换为 实时性
  - 右键->滤镜-滤镜/解码器管理-视频解码器-内置解码器/DXVA设置->√图像滞后时允许漏帧保证同步，√使用硬件加速
1.  MS白板，Ubuntu，充个数，diskgenius
2.  <a href="https://www.teamviewer.cn/cn/">`team viewer`</a>，远程工具
3.  Windows Tile Color Changer
4.  diskGenius
5.  notepad++
### 网络工具
1. <a href="https://www.netsarang.com/en/xftp/">`xftp+xshell`</a>+<a href="https://putty.org">`putty`</a>
  - 其实已经有了Terminus，但是xshell兼容性有些时候简直不可或缺
  - xftp目前用的最顺手，putty以备不时之需
2. `酸酸乳和酸酸tab`，tab已经维护到头了，下最新的那个版本就行了，酸酸乳别来问我。
3. `V2RayN`，网络代理工具，可以用来混淆加密网络代理内网部署等等。
4. <a href="https://www.telerik.com/fiddler">`fiddler`</a>和<a href="https://www.charlesproxy.com/download/">`charles`</a>抓包工具，各有优劣，不过差不多都很好用。fiddler有安卓版
5. `EasyConnect+AnyConnection`网络工具，用来公司内网连接的，自己找资源吧，不买不让下。
6. `Tor`，洋葱网络，<a href="https://www.torproject.org/">官网</a>应该是打不开的,<a href="https://github.com/TheTorProject/gettorbrowser">github</a>有，别乱上网站，违法。
## 体验增强
- <a href="https://www.voidtools.com/zh-cn/">`everything`</a>可以查找系统内所有的文件，设置为服务，开机启动，去掉任务栏图标，alt+~呼出，注意关闭http和ftp，不然会把自己的文件暴露在搜索引擎上。
  - 后台运行，去掉托盘图标，实时搜索
  - 双击打开目录 使用双缓存，使用交错行，搜索关键词高亮，显示数量和搜索总数，显示提示信息
  - 显示快捷窗口Alt+`，保持http和ftp关闭
- **<a href="https://www.autohotkey.com/">autohotkey</a>** 按键映射，可以让你Ctrl+Shift转换输入法，win自带的时win+space;映射为Ctrl+Shift,win+t按键置顶当前窗口win+ctrl+t取消当前窗口置顶
  - 设置->语言->中文(中华人民共和国)->微软拼音->选项->选择默认输入法模式。自行调整切换后默认为中文即可
  - 新建一个脚本 输入法案件映射.ahk 并放入
    ***C:\Users\57635\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup*** 脚本内容
```
^Shift::#Space
+Control::#Space
#t::WinSet AlwaysOnTop,on,A
^#t::WinSet AlwaysOnTop,off,A
```  
- `diskSpaceAnalysisTool`精细查看是谁占了磁盘空间
- `天若OCR`，平时不用开，复制一个exe起名为tianruo，用的时候everything搜索，设置为F19呼出识别,F10翻译，关闭更新。老版的可以用新版的要钱了，不要更新保留安装包。
- `无广告版Winrar`
## 优化开机启动和服务
有三个地方的自启需要被关掉:
- 设置里开机启动
- 右键任务管理器->启动
- 启动时 ***C:\Users\57635\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup*** 该目录下启动时脚本会被运行一次

Win+R(services.msc)优化服务(不需要的就关掉):


| 服务                                     | 作用&设置                                              |
|:---------------------------------------- |:------------------------------------------------------ |
| Adobe Genuine Monitor Service            |                                                        |
| Adobe Genuine Software Integrity Service |                                                        |
| BitLocker Drive Encryption Service       |                                                        |
| CAJ Service Host                         | 手动                                                   |
| Certificate Propagation                  | 手动                                                   |
| Contact Data 63c78b                      | 如果停止或禁用此服务，你的搜索结果中可能会缺少联系人。 |
| Developer Tools Service                  | 远程UWP调试                                            |
| Diagnostic Execution Service             | 策略诊断                                               |
| Diagnostic Policy Service                | 策略诊断                                               |
| Diagnostic Service Host                  | 策略诊断                                               |
| Diagnostic System Host                   | 策略诊断                                               |
| Docker Desktop Service                   | 手动                                                   |
| Function Discovery Resource Publication  |                                                        |
| Google Update Service(gupdate)           |                                                        |
| Google Update Service(gupdatem)          |                                                        |
| ntel(R)HD Graphics Control Panel Service |                                                        |
| MessagingService 63c78b                  |                                                        |
| Microsoft（R）                           | 诊断中心标准收集器服务                                 |
| Offline Files                            |                                                        |
| Phone Service                            |                                                        |
| QPCore Service                           |                                                        |
| Quality Windows Audio Video Experience   |                                                        |
| SangforSP 手动                           |                                                        |
| Shared PC Account Manager                |                                                        |
| shell Hardware Detection                 |                                                        |
| Smart Card                               |                                                        |
| Smart Card Device Enumeration Service    |                                                        |
| Smart Card Removal Policy                |                                                        |
| TeamViewer 14                            | 手动                                                   |
| WalletService                            |                                                        |
| Windows Error Reporting Service          |                                                        |
| Windows Search                           |                                                        |
| Workstation                              | 手动                                                   |
| XLServicePlatform                        | 手动                                                   |
| 家长控制                                 |                                                        |
| 建议疑难解答服务                         |                                                        |


- 所有工作做完之后用Dism++ 在做最后调整。
## 美化
### 美化开始菜单
- win10美化工具修改磁贴的底色
- windowsTilecolorchanger
- 利用xml修改磁贴背景图
### 美化D盘图标
icons解压出来，分别对应好，有些是在软件里面有svg，直接使用里面的。

## 文件和资料存放位置
Music 放缓存的音乐  
Video pin到开始屏幕，里面放所有的视频  
Picture 放图片和以前的照片  
Download 放所有软件的下载和QQ保存的文件  
Documents放书和软件默认占用目录还有Adobe，jetbrain缓存  
机械盘里的Game分几个部分:每个公司占一个，自己的游戏单独占一个文件夹  
code文件夹用来放所有的代码，放固态读取启动快  
codeCommon文件夹用来放一些代码相关的资源和共用的文件  
编程的仓库放机械盘
### 备份时需要注意的文件

音乐 有绝版的歌  
视频 我的几乎所有视频  
乱七八糟不能丢的 放着以前的照片和一些重要的文件  
树莓派相关 是树莓派的一些东西  
code 是我所有的代码  
绝版安装包 是搜集的一些资源  
Game 存放收集的游戏

### 记录状态

PC : <br/>

<div align=center ><img src="./static/Snipaste_2019-11-03_16-38-14.png" style="height: 400px"/></div>
<div align=center >

<table border="0">
  <tr>
    <th><img src="./static/Snipaste_2019-11-03_16-38-41.png" style="height: 150px" alt="xxx"/></th>
    <th><img src="./static/Snipaste_2019-11-03_16-38-52.png" style="height: 150px"/></th>
    <th><img src="./static/Snipaste_2019-11-03_16-39-13.png" style="height: 150px"/></th>
  </tr>

</table>

</div>


<div align=center ><img src="./static/Snipaste_2019-11-03_16-39-03.png" style="height: 150px"/></div>

<div align=center ><img src="./static/Snipaste_2019-11-03_16-39-27.png" style="height: 150px"/></div>

surface : <br/>
<div align=center ><img src="./static/Snipaste_2019-11-01_18-16-43.png" style="height: 300px"/></div>
<div align=center >

<table border="0">
  <tr>
    <th><img src="./static/Snipaste_2019-11-01_18-17-26.png" style="height: 150px;"/></th>
    <th><img src="./static/Snipaste_2019-11-01_18-17-00.png" style="height: 150px;"/></th>
  </tr>
</table>

</div>

<div align=center >

<table border="0">
  <tr>
    <th><img src="./static/Snipaste_2019-11-01_18-17-55.png" style="height: 250px;"/></th>
    <th><img src="./static/Snipaste_2019-11-01_18-18-13.png" style="height: 250px;"/></th>
  </tr>

</table>

</div>


::: danger ⚡️Danger
本文所提到的所有软件仅供交流学习使用，请下载者在下载后24小时内删除，作者不分享任何盗版资源，有能力者请支持正版。所有通过本文寻找盗版造成的损失与作者无关。
:::


