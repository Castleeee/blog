---
icon: operate
title: 服务器规格说明书
date: 2022-03-19 12:50:00
order: 4
comment: false
---
::: tip 📌Tip
折腾死我了，服务器资源利用的差不多了，踩好多坑。
:::
<!-- more -->
 

## 安装基础的软件
记录一下主服务器的常驻服务，比如什么nginx，博客，docker，gitea之类的。  
使用的是**centos8**  
::: warning Warning
```
service ssh status
Redirecting to /bin/systemctl status ssh.service
Failed to get properties: Access denied
```
一直出现这个错误，最后在stackoverflow找到了一个偏门的方法，我都不知道他在干嘛,不知道有什么隐患
**kill -TERM 1**

直接换系统了，好像是CentOS的问题直接换大便系统
:::
**Ubuntu**记得装LTS软件源支持五年  
加个源
```bash
deb http://security.ubuntu.com/ubuntu focal-security main restricted
deb http://security.ubuntu.com/ubuntu focal-security universe
deb http://security.ubuntu.com/ubuntu focal-security multiverse
deb http://archive.canonical.com/ubuntu focal partner
```
更新
```bash
apt-get update
apt-get upgrade
```
- 基本的软件：`apt-get install -y wget vim tree net-tools supervisor gcc  sl curl  neofetch`
- 一些依赖`apt-get install -y tk perl cpio asciidoc xmlto build-essential libpcre3-dev libssl-dev sqlite3`  
- Centos基本的软件和依赖：`yum install -y yum-utils wget vim tree net-tools supervisor crontabs gcc  sl  neofetch curl openssl neofetch tk zlib-devel openssl-devel perl cpio expat-devel gettext-devel asciidoc xmlto util-linux-user` 

git安装最新版[^1]
```bash
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
git config --global user.email "xxxxxx@gmail.com"
git config --global user.name "remoteServer"
```
- 调整时间和本地化
```bash
sudo timedatectl set-ntp true # 启用 NTP 服务  
sudo ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime # 将时区设为“亚洲/上海”  
sudo hwclock --systohc # 将硬件时钟调整到与当前系统时间一致  
date -R # 以 RFC 5322 格式输出日期和时间。例如 Mon, 18 Jan 2021 11:04:16 +0800
#语言本地化 避免以后字符集问题
sudo apt-get install  -y language-pack-zh-hans
sudo ./install-language-pack zh_CN # dpkg 可以忽略
sudo vim /etc/environment # 修改这个文件 LANG="zh_CN.UTF-8"
source /etc/environment # 启用
```
改一下ssh端口，root下有个snap作者一直不修复[^2]
## 装OhMyZSH
把[这个](../Guides/安利/windows子系统.md#^7ab766)重组搬过来了  
安装zsh切换默认
```bash
# yum install -y zsh
apt-get install -y zsh
chsh -s /bin/zsh
```
脚本安装Ohmyzsh
```bash
sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```
所有的设置都存放在`~/.zshrc`文件里  
主题
```bash
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```
文件改变`ZSH_THEME="powerlevel9k/powerlevel9k"`
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
安装autojump，支持j直接跳转
```bash
git clone https://github.com/joelthelion/autojump.git
cd autojump
./install.py
```
把提示的东西添加到`~/.zshrc`文件尾。  
修改插件
```
plugins=(git extract ruby gem rails rvm python pip npm node scala docker ant gradle golang redis-cli colored-man-pages zsh-syntax-highlighting zsh-autosuggestions)
```
需要添加的:
- `ZSH_THEME="powerlevel9k/powerlevel9k"`
- `export DEFAULT_USER="whoami"`
- `export TERM="xterm-256color"`
- `POWERLEVEL9K_CONTEXT_TEMPLATE="%n"`
最后这个是用来去掉阿里云前面又臭又长的主机名的，留下了用户名  

nvm [^3]一定要安完zsh之后搞，这样就不用手动加了  
`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`  
`nvm ls-remote` 记得安个最新的LTS

## 起docker各种服务
compose文件都起好了，安装然后就行了  
安装docker[^4]和docker-compose[^5]命令行去文档找  
::: tip 📌Tip
我都写了docker-compose.yml里了
:::
### 启动服务
| 端口:容器端口 | 功能                        |
|:------------- |:--------------------------- |
| 22:22         | gitea的ssh顶替本机的ssh     |
| 8000:80       | gitea的web页面              |
| 8001:25       | 轻量SMTP                    |
| 8002:8000     | portainer不知道干嘛的端口   |
| 8003:9000     | portainer的web页面          |
| 8004:80       | zfile页面                   |
| 8005:host     | nginxwebui页面              |
| 8006:host     | nps的web页面                |
| 8007:host     | nps的bridge端口             |
| 8008:host     | nps的http                   |
| 8009:host     | nps的https                  |
| 8010          | webhook穿透到群辉的相同端口 |
| 9443:9443     | portainer不知道干什么的端口 |
| 22233         | ssh                         |

**群辉的端口(约定优于配置)**  

| 端口   | 功能->服务器穿透端口 |
|:-----|:------------------|
| 5000 | nas面板->8014    |
| 8096 | jellyfin->8015 |


- [portainer](https://docs.portainer.io/)
    - 端口 8003:8000不知道干嘛的端口 8002:9000web 管理端口 9443:9443通信端口
    - 域名 admindocker;portainer
    - 这个没有composer，现用现开，要提前创建volume
    - 如果web出现not found，就开9000映射到8003我也不知道干啥的映射了就能用[^6]
- 博客 主NginxwebUI
    - 端口 8005管理
    - 域名 admin.nginx
- zfile图床 
    - 端口 8004
    - 域名 static
    - [使用3.2版本不要用3.2.1](https://github.com/zhaojun1998/zfile/issues/327) 短链管理会出错
- gitea自建git
    - 端口 8000web访问 ssh端口默认用22了，本应该直接ssh能复制，现在不行。
    - 域名 git需要在控制台改，ssh不能分流
    - 客户端加入这个命令否则无法复制会显示ssl证书过期`git config --global http.sslVerify false`
    - ssh是用来克隆私有仓库的，添加key才能用，http能用
    - 邮件不能用(以后用群辉)
- [nps](https://www.bilibili.com/video/BV1X44y1n7Te)内网穿透
    - 端口 8006web端口 8007桥接client bridge代理 8008http 8009https[^8]
    - 域名 nps \*.nps 
- webhook
    - 域名blogupdate
    - 端口 8010
    - 目前用来自动拉取博客，以后可能会有更大作用
    - url列表
        - `/BlogUpdate` 自动拉取并部署博客
    - 部署flask[^11]，测试完毕后就上线，做好备份。进入receiveWebHooks直接`nohup python receiveHook.py > flask.log 2>&1 &`。不会有人闲着没事攻击我的webhook吧，就算是攻击反正也是返回字符串，应该顶得住。
    - 顶不住了，小身板编译都费劲，以后移到群辉[^15]
- 自建邮件docker[^14]，不安全
    - 域名smtp
    - 端口8001:25
    - 只有一个SMTP功能，没有任何安全校验，注意发出去大概率会被认为是垃圾邮件，反正我自己用，添加白名单就行.
- 群辉以后要有的
    - Yapi
    - 邮件服务器-穿
    - jellyfin
    - moment照片
    - 苹果时间机器
    - Surveillance Station监控
    - Calibre web
    - 导航页
    - 博客webhook-穿
    - HomeAssistant智能家居
    - filerun网盘
    - 群辉chat私人聊天
    - drive 想办法融合onedrive
    - cloudsync统筹一下网盘
    - rsshub -可以穿
    - Docker装Aria2 With WebUI
    - smb 
### 域名配置
nginxWebUI里面直接添加。  
几个资源，[自动生成配置文件](<[NGINXConfig | DigitalOcean](https://nginxconfig.io/)>)，[申请证书](https://www.bilibili.com/video/BV1Ef4y1F7Pe)。  
申请SSL，cloudflare->个人配置->API key -> Global API Key -> view API key 邮箱+key填进去  
  
ssl 接收到一个超出最大准许长度的记录。 错误代码 ssl_error_rx_record_too_long 谷歌搜索443 ssl[^7]  
加了ssl之后不能自动跳转https，纯域名访问就可以，原理我也没深究[^9]  
头部添加特殊的header自动跳转https

### ufw
用户防火墙，配置完nginx之后，依然可以通过http+域名:端口访问，配置user fire wall禁止端口特定放行。  
配合http跳转https，就可以强制只能通过域名访问了。  
记得配置nginx的转发要用127.0.0.1。  
[^10]
::: warning Warning
开了个 Docker 容器，绑定了 `-p 3306:3306` 并开启了 `ufw` 。发现竟然外网可以直接访问！！  
原来 Docker 会默认直接加规则到 iptables，所以 UFW 防火墙对 docker 无效。  
基本上可以找到的解决办法就是首先禁用 docker 的 iptables 功能，但这也意味着放弃了 docker 的网络管理功能  
github有个答案
:::
**无法解决，就这样了，丑陋**  
因为docker是直接添加iptables管理网络，ufw直接没用，如果手动更改它的iptables那就相当于docker的网络管理没用了，没办法，正式生产环境肯  定会有网关和内部服务器，就可以完美避免了。丑陋。
## 安装v2ray相关
[参考](https://ericclose.github.io/V2Ray-TLS-WebSocket-Nginx-with-Cloudflare.html)  
执行一键脚本
- 把证书映射进去
- v2ray.conf 映射进去
- nginx 中include
- 别忘了开bbr

本质上就是nginx把访问这个路径的流量转发到本地v2监听的端口，流量的参数注意要对齐。

::: tip 📌Tip
不要试图修改证书和移动证书位置，不要上传，直接映射，不然没法续期，这东西很脆弱。  
把本地的nginx关了并禁止自动启动，修改update_ssl.sh不要让它启动本地的nginx
:::

[^1]: [如何在 Ubuntu 上安装最新版本的 Git - 知乎](https://zhuanlan.zhihu.com/p/108991735)  
[^2]: [Bug #1575053 “Please move the “$HOME/snap” directory to a less o...” : Bugs : snapd package : Ubuntu](https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/1575053)  
[^3]: [GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions](https://github.com/nvm-sh/nvm)  
[^4]: [Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/)  
[^5]: [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)  
[^6]: [HTTP return "Not found" · Issue #4143 · portainer/portainer · GitHub](https://github.com/portainer/portainer/issues/4143).  
[^7]: [SSL 接收到一个超出最大准许长度的记录。 错误代码:SSL_ERROR_RX_RECORD_TOO_LONG](https://icode9.com/content-4-1203155.html)  
[^8]: [nginx实现对ssh的反代 | 好好单调](https://monotone.github.io/2017/12/16/reverse-proxy-for-ssh-by-nginx/)  
[^9]: [当虚拟目录不是在80端口且打开ssl时出错 ssl_error_rx_record_too_long _ikmb的博客-CSDN博客](https://blog.csdn.net/ikmb/article/details/3863705)  
[^10]: [GitHub - chaifeng/ufw-docker: To fix the Docker and UFW security flaw without disabling iptables](https://github.com/chaifeng/ufw-docker#%E8%A7%A3%E5%86%B3-ufw-%E5%92%8C-docker-%E7%9A%84%E9%97%AE%E9%A2%98)  
[^11]: [supervisord 部署 Flask](https://liqiang.io/post/deploy-flask-gunicorn-by-supervisord)  
[^12]: [supervisor多个env变量 | Gary Wu](https://garywu520.github.io/2021/03/15/supervisor%E5%A4%9A%E4%B8%AAenv%E5%8F%98%E9%87%8F/)  
[^13]: [Just a moment...](https://ednovas.xyz/2022/02/08/yandexdomainmail/#%E7%BB%91%E5%AE%9A%E5%9F%9F%E5%90%8D).  
[^14]: [使用Docker搭建SMTP服务器 - Jeff.Chen的技术博客](https://chenqing24.github.io/tech_tutorial/linux%E5%B7%A5%E5%85%B7/smtp_docker/)  
[^15]: [升级到umi 3.1.0 打包项目卡死，不知道为什么，哪位大佬给看下 · Issue #4423 · umijs/umi · GitHub](https://github.com/umijs/umi/issues/4423)  
[^16]: [利用Docker部署cloudreve+aria2实现私有网盘和离线下载](https://dongjianghan.com/archives/cloudreve)  
[^17]: [xavierniu/cloudreve - Docker Image | Docker Hub](https://hub.docker.com/r/xavierniu/cloudreve)  