---
title: part 3 shell脚本
date: 2022-04-29 14:12:45
category: 
- 课程
order: 3
---

## shell
`cat /etc/shells` 查看系统支持哪些shell `$SHELL`当前用的啥  
::: danger ⚡️Danger
**指定解析器**<br/>
**#!/bin/bash**  
每个脚本开头都使用"#!"，#!实际上是一个2字节魔法数字，这是指定一个文件类型的特殊标记，在这种情况下，指的就是一个可执行的脚本。在#!之后，接一个路径名，这个路径名指定了一个解释脚本命令的程序，这个程序可以是shell，程序语言或者任意一个通用程序。
:::

使用bash a.sh的时候就不用+x  
**source** or **.**  a.sh也可以执行，***在当前shell中一条一条执行，其他的都是开启一个子shell进程执行，可能会获取不到环境变量，子 shell 中设置的 当前变量，父 shell 是不可见的***  
直接bash命令相当于直接进入了子shell操作
## 变量
::: danger ⚡️Danger
**赋值的时候等号两边一定要空格，否则会被当成一体的字符串！！！
尤其是循环判断**
变量类型会自动判断，小心！
:::
### 全局和局部环境变量
使用env和printenv命令获取所有系统定义的变量  
printenv可以不加$符，printenv HOME=echo $HOME  
set 可以看到定义的所有变量和函数，自定义的也能看到  

### 系统环境变量和用户定义环境变量
在命令行里 定义变量，`a = 2`,`echo $a` 弱类型，定义字符串用双引号括起来，双引号会自动识别变量表示符***单引号不会读取为变量表示符***  
但是定义的是**局部变量**，使用`export variable = 2`设为**全局变量**  
::: warning Warning
在子shell里面修改全局变量只会在子范围里面生效，上级不会生效，**export也没用**  
export只在本次会话中生效  
:::
***约定俗成系统变量大写，自定义变量小写***  

默认等号后面都是字符串，如果要做数值运算，应该使用`a = $((1+5))` or `a = $[5+1]`  

### 只读变量
静态常量 `readonly a = 5` `unset variable`，从环境中删除variable  
bin和sbin目录下都是系统的定义的可执行，查看$PATH就可以，路径添加到 $ PATH 的格式为 ` PATH=$PATH:<PATH1>:<PATH2>`  
或者编辑变量文件在最后直接export  

>可以设置环境变量有4个 优先级从高到底

#TODO 环境变量和优先级
[理解 bashrc profile 优先级及区别 | Verne in GitHub](https://einverne.github.io/post/2017/03/bashrc-profile.html)  
[Linux文件 profile、bashrc、bash_profile区别 - 知乎](https://zhuanlan.zhihu.com/p/405174594)  
[理解 bashrc 和 profile - { wido.me }](https://wido.me/sunteya/understand-bashrc-and-profile)
1. **/etc/profile**:在登录时,操作系统定制用户环境时使用的第一个文件,此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行。
2. **/etc/environment**:在登录时操作系统使用的第二个文件,系统在读取你自己的profile前,设置环境文件的环境变量。
3. **~/.bash_profile**:在登录时用到的第三个文件是.profile文件,每个用户都可使用该文件输入专用于自己使用的shell信息,当用户登录时,该 文件仅仅执行一次!默认情况下,他设置一些环境变游戏量,执行用户的.bashrc文件。/etc/bashrc:为 每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.
4. **~/.bashrc**:激活shell时使用该文件

### 接收变量
- \$$ Shell本身的PID（ProcessID）
- $! Shell最后运行的后台Process的PID
- $0 表示脚本本身的名称,带路径
- $1 就是第一个参数，$2就是第二个以此类推
- $# 获取接收的参数个数
- $* 获取所有参数视为一个字符串"在被双引号括起来时"
- $@ 把参数作为数组
- $? 上次执行脚本的返回码 (0-255)，**这个直接在命令行执行完脚本后使用**，在脚本中用会返回上一个命令(也是脚本)而不是本次的

basename 命令路径可以获取最后一个/分割的内容，如果跟着第二个参数suffix就会去掉后缀  
dirname 返回的是该文件的路径，也是简单的字符串分割  

## 表达式
### 运算符
shell默认是不会解析基本数学表达式的，需要使用`expr 1 + 2`命令，注意**必须要有空格**，乘号使用\*  
命令替换使用两个反引号，把结果赋给变量。

为了解决麻烦，使用`$((表达式))`或`$[表达式]`，在for和if中可以`((expression))`但是不提倡  
### 判断
#### if
test 命令检查某条件是否成立，可进行数值、字符和文件的测试，使用echo $?查看返回码0代表正常运行就是一样(好怪)  
可以简写成`[ condition ]` 方括号一定要有空格，条件**非空为True 1，空为False 0**  

字符串就=,!=，数值判断不能用符号,[4 -ne 5]～4≠5  

|-eq |等于（equal）=| -ne |不等于（not equal）≠|
|:--- |:--- |:--- |:--- |
|-lt |小于（less than）< |-le |小于等于（less equal）<=|
|-gt |大于（greater than）> |-ge |大于等于（greater equal）>=|

判断文件是否有权限  
-r 读 -w 写 -x 执行  

判断文件类型  
-e 文件存在（existence） -f 存在且是文件（file） -d 存在且是目录（directory）  

&& 与 || 或 ! 非  
`[ ] && echo OK || echo notOK` 整成三元运算符  
在一个[]里进行与或判断的话，形式如下`[ condition1 -a/-o condition2 ]` and -a ; or  -o  
一般多个条件是`[ cond1 ] && [ cond2 ]`  
if 命令格式有点不一样

```shell
if [ expression ];then
    process
fi

# 完全体
if [ expression ]
then
    process 
elif [ con ]
then
    process
else
    process
fi
```
`;`作用是在一行里把两个命令隔开  
::: tip 📌Tip
**if 使用时候的小技巧**<br/>
在判断字符串后面拼接一个字符，即使不输入也不会报错  
`if [ "$1"x="condition"x ];then`  
:::

#### case
```shell
case $variable in
value1)
    process
;;
value2)
    process
;;
*)
    default
;;
esac
```

就是switch case，语法真的奇怪
### 循环
#### for
**注意变量自加的写法**

```shell
# 普通for
for ((init;condition;variables-change))
do
    process
done

# 增强for
for i in "a","b","c"
do
    echo $i
done

# 一个递加到指定数的for操作，注意变量的使用和数学表达式
for((i=1;i<=$1;i++))
do
    sum=$[ $sum + $i ]
done
echo $sum

```

#### while
一般要在外面提前定义变量  
```shell
a=1
while [ $a -le $1 ]
do # 注释里为新写法
    sum=$[ $sum+$a ] # let sum+=a
    a=$[ $a + 1 ] # let a=a+1
done
```

### console IO
```shell
read -t 10 -p "输入你的名字" name
```
read 命令，只能在脚本文件里面使用，命令行里会出现-p: no coprocess
-   -a 后跟一个变量，该变量会被认为是个数组，然后给其赋值，默认是以空格为分割符。
-   -d 后面跟一个标志符，其实只有其后的第一个字符有用，作为结束的标志。
-   -p 后面跟提示信息，即在输入前打印提示信息。
-   -e 在输入的时候可以使用命令补全功能。
-   -n 后跟一个数字，定义输入文本的长度，很实用。
-   -r 屏蔽\，如果没有该选项，则\作为一个转义字符，有的话 \就是个正常的字符了。
-   -s 安静模式，在输入字符时不再屏幕上显示，例如login时输入密码。
-   -t 后面跟秒数，定义输入字符的等待时间。
-   -u 后面跟fd，从文件描述符中读入，该文件描述符可以是exec新开启的。
#TODO 试试所有的参数

## 函数
系统命令要使用命令替换，`$( expression ) ` 实际上就是获得值赋予  

自定义函数
```shell
function f() # function 括号都能省略
{
    variable=$[ $1 + $2 ] # 注意参数的定义
    Action;
    return int; # 省略return返回值是上一个函数语句执行完的$?状态码范围必须0-255整数
    # 如果要返回数据，要配合使用
    echo $variable
}

f $a $b # 注意参数的传入

# 返回值技巧
outer=$(f $a $b) # 输出结果就会被赋到outer
```
调用之前必先声明，严格顺序，因为他就是单纯逐行执行。  
## 文本处理
### 正则表达式
grep awk sed cut vim+/ 后面可以直接使用正则，但是什么情况下会使用还不知道，之后再补充吧  
### 命令
`cut -d "spliter" -f column1,2-5 file ` 以spliter为分割符取1，2到5列，-默认不填就是截到开头结尾
awk是gawk的软链接,是GNU的gawk的实现  
默认以空格分割  
`awk -F "spliter" '/regex pattern/ {action}'`  
`awk -F ":" -v i=100 'BEGIN{print "user, shell"} {print $1+i","$7} END{print "dahaige,/bin/zuishuai"}' passwd`  
以 : 为分割符，定义变量i = 100 开始前先打印一行"user, shell"，打印第一列+i 结束时打印"dahaige,/bin/zuishuai"  
| 内置变量     | 含义    |
|:---------|:------|
| FILENAME | 文件名   |
| NR       | 行号    |
| NF       | 切割后列号 |
`awk -F " " '/^'"$VALU"'/ {print $2}'` 正则中使用外部变量
## 发送消息
`mesg，who -T `查看是否开启接收其他用户消息，`mesg n/y`关闭/打开消息  
`write user tty` 发送和接收方都会进入多行编辑模式。  


## 实例
### example 1 - 定时归档目录
要求: 
- 定时归档文件
- 用tar打包
- 附加日期
- 存储日志

::: details Click to see more


```shell
#!/bin/bash
# 判断参数是否为1
if [ $# -ne 1 ]
#!/bin/bash
# 判断参数是否为1
if [ $# -ne 1 ]
then
        echo "参数个数错误，目录应为1"
        exit
fi

# 获取路径
if [ -d $1  ]
then
        echo ""
else
        echo "目录不存在"
fi

DATE=$( date +%y-%m-%d )
DIRNAME=$( basename $1 )
DIRPATH=$(cd $(dirname $1);pwd )

FILE=archive_$DIRNAME_$DATE

echo "开始归档"
tar -czf /home/jack/$FILE $DIRPATH/$DIRNAME

if [ $? -eq 0  ]
then
        echo "压缩完成"
else
        echo "压缩失败"
fi
exit
```

:::

### example 2 - 发送消息
使用Linux自带的mesg和write命令向其他用户发送消息
- command user message
- 检测用户是否在线
- 检测用户是否打开了消息
- 基本的判空特殊字符串处理等
 
::: details Click to see more


```shell
#!/bin/bash
# 获取用户列表注意列表的使用 l=(1 2 "3")
userlist=($(who -T | awk -F " " '{print $1}') )
# 检查参数

if [ $# -eq 2 ] && [[ "${userlist[@]}" =~ $1 ]] && [ $2 != "" ];then # 判断元素是否在列表里以及判空
        USER=$1
        MSG=$2
        TTY=$(who -T | awk -F " " '/^'"$1"'/ {print $3}')
else
        echo "args number is unsuitable"
fi
# 检查用户是否在线
if [ $(who -T | awk -F " "  '/^'"$1"'/ {print $2}' ) = "+" ];then # awk 正则表达式使用外部变量
        echo $MSG |write $USER $TTY
else
        echo "user is offline"
fi

exit
```

:::

