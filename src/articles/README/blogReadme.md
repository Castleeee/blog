---
icon: write
title: 博客写作技术说明
date: 2022-04-16 13:46:00
order: 2
comment: false
---

## 博客的目的
上一个博客因为各种原因，废弃了，一开始是因为写得多了之后太过于庞杂，没有后台管理导致内容和组织越来越混乱，一边写一边思考解决方法，最后发现了Obsidian简直是理想中的模式，遂直接重开，用Obsidian写笔记，寻找最大兼容的语法，直接放进博客渲染。  
所以这次就不赶潮流了，Obsidian直接固定下来，博客只要稳定就固定下来，感觉这个模式已经成熟了，不出意外不去更新，这个页面是关于博客如何组织的说明，上一篇是关于Obsidian的事项
## 博客的写作
安装helloworld什么的我就不多说了，文档上很齐全，照着来就是了。  
::: danger ⚡️Danger
**吸取教训**<br/>
一定要留下各个平台的node_modules，以免几年之后项目跑不起来了，留下M1的，x86windows的和x86windows的，存onedrive，存的时候验证可用性
:::

### metadata信息 
^18f313
文件的开头会有metadata信息，如下代码块
``` yaml
---
icon: info
title: first page  
date: 2022-02-11 15:31:09 
order: 1
sticky: 1
toc: true
sidebar: true
prev: false  
next: false  
comment: false
category:  
- 系列1
tag: 
- 说明
footer: true 
backtotop: true

navbar: true  
breadcrumb: true  
pageInfo: true  
contributors: true  
editLink: true  
lastUpdated: true  
---
```
- icon 非必填在文章前面显示图标，[图标样式大全](https://vuepress-theme-hope.github.io/v2/zh/guide/interface/icon.html#iconfont-%E7%B2%BE%E9%80%89%E5%9B%BE%E6%A0%87)
- title 必填不要重名
- date 必填用@可以直接生成
- order 在侧边栏中的排序
- sticky 接受数字，降序排列(大在前)置顶
- toc 是否要右边栏
- sidebar 是否在此篇中显示侧边栏
- next和prev，就是上下页，如果已经被纳入侧边栏系列文章就可以不用配置，自己会生成
- comment 要不要评论区
- category 可以用中文，类似于系列，只要新出现的都会自动创建，可以一篇文章多个category
- tag 标签可以用中文，vuepress只会解析metadata里的[标签](Obsidian.md#^d604fe)，可以用Tag Wrangler插件管理
- footer 是否显示页脚
- backtotop 是否显示回到顶部小火箭
- navbar 是否显示顶部导航栏
- breadcrumb 是否显示面包屑导航
- pageInfo 是否显示一些页面信息分类之类的
- contributors 是否显示作者
- editLink 是否显示edit on github
- lastUpdated 是否显示最近更新时间


### 写作注意事项
[库写作时的注意事项](Obsidian.md#^5c3a93)^255951
1. **在 `vuepress-theme-hope` 中，请摒弃一级标题，使用 `front-matter` 生成标题以及其他文章信息，正文从*二级标题*开始，二三级标题生成左侧子目录** 二级标题在前面会有一个小竖条定位   
2. 日期一定要 ==2022-01-02 00:00:00== 要全不然会报错
3. 前后空格的双等号才会被渲染为==高亮==
4. 所有的一级二级侧边栏文件夹最好==不要有空格用-代替==，但是tag和category可以
    1. 在使用toc为false的时候侧边栏会提取header生成子标题，使用headerDepth: 0来禁用
    2. 侧边栏配置，由python读取config生成，Course和社科读书笔记下默认每个目录生成一个侧边栏
5. 使用Admonition时的对应关系，事先约定规则，写一个python脚本，转换Admonition语法为Markdown-it-container，想的是用的regex替换
    1. vuepress使用markdown-it-container,支持 tip danger warning theorem details，类型 标题
    2. Admonition支持`note`,`abstract`,`info`,`tip`,`success`,`question`,`warning`,`failure`,`danger`,`bug`,`example`,`quote`
    3. example默认collapse是open，用detail，不加前缀，其他的collapse默认关闭直接删除。
    4. 把所有的`(./static/` 替换为`(./static/` 省得自己配置了
    5. 其他的把title拿上去，前面加前缀，例子ad-note 你好= 📝Note 你好
    - info:`note` =📝Note,`info`=📄Info，蓝色
    - tip: `abstract`=📘Abstract,`tip`=📌Tip,`success`=🎉Success，绿色
    - warning: `question`=❓Question,`warning`=⚠️Warning，橙色
    - danger: `failure`=❌Failure,`danger`=⚡️Danger,`bug`=🐛BUG，红色
    - theorem,details: `details` 这俩直接加标题白色
6. \<\!-- more --> 之上的是文章简介，~~其实可以搭配:::使用但是Obsidian里面不渲染，有点突兀~~ 自己写脚本解决了
7. 默认是toc代码块用(四个点的)渲染，用脚本直接更改为双括号[\[toc]\] 就可以在vuepress中渲染
8. 标签和分类
    - 成系列的文章放一个category
    - category分类
        - 课程，书和电影，语言分类，工具安利，随笔，代码之外，剩下的按技术方向
    - 非系列连续文章也需要配置
    - tag尽量精简而全
    - 阅读顺序从上往下
9. 已经全配置好了，展示组件也写好了  
::: warning Warning
Card给的id一定要和ThreePageJson里面的id匹配，最好还能和课程名字匹配  
图床做了baseUrl在/.vuepress/public/js/pgmanor-self换地址要记得修改  
sidebarConfig的路径是博客里的路径不要混了，希望自动生成就[],不然自己配置顺序  
Course自动生成侧边栏是匹配的是regex ^第xx章 文件名以第多少章开头才会排序预留2000。  
去除侧边栏连续非系列文章看下面  
:::

## 自己修改文件
### 脚本说明书


git pull **拼装**  
笔记路径->博客路径:  

```
/blogs -> /articles/blogs  
/Courses -> /articles/Courses  
/others/public/Guides-> /articles/Guides  
/others/public/README-> /articles/README  

mkdir -p /articles/socialsci/  
/others/public/社科读书笔记-> /articles/socialsci/社科读书笔记  
/others/public/FilmBookReview-> /articles/socialsci/FilmBookReview  
 
```

articles**执行语法兼容转化**:   

生成sidebar请查看sidebarConfig  

侧边栏使用structure会自己排序，使用order排序，嵌套文件夹，首先在文件夹下创建README.md，在此文件中使用dir order 为文件夹排序。更多的选项看[这里](https://vuepress-theme-hope.github.io/v2/zh/guide/layout/sidebar.html#%E9%80%9A%E8%BF%87%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90)  
```yaml
# 本文件夹里的
order: 3
# README中控制本文件夹在上层的排序
dir:  
    order: 3
```
- 写了个展示卡，用来展示连续的课程
- 展示卡页面需要去掉所有的代码块符号，按Guides/config下的文件生成侧边栏配置项替换掉原来的文件，json先去掉代码符然后切分塞入inrtoduction并删除
- flask nginx部署

### 配置
把插件，侧边栏，分离出去.[^1]  
注册自定义组件，配置一些标题，首页文字，去掉双语能切换颜色黑白主题等  
本来想自己写个按钮，直接强制定位到那里，但是vuepress2的我不会注入插件，在首页readme.md  
## 插件
插件都是文档上给的，插件引入是一个调用了插件函数的列表，否则报错  
很多插件都内置了，不用自己配置，还有`pnpm add -D axios`需要安装  
### 评论
上次评论用的Vaillne，又更新服务了没法用了还得绑定手机号，直接换Vssue用github  
内置了Giscus 去照着文档配置一下  
### 注册全局组件
`pnpm add -D @vuepress/plugin-register-components@next`
在client中配置并且注册才能生效
### 看板娘
`pnpm add -D  vuepress-plugin-live2d-plus`  
模型下载到了本地public不能出声了，但是其东西是没问题的  
### 搜索插件
`vpnpm add -D  vuepress-plugin-search-pro@next`
官网文档上有，配置如下

::: details Click to see more

```ts
export default function MyPlugin(){  
    return [  
    searchProPlugin({  
        indexContent:true,  
        customFields: [  
            {                name: "category",  
                // @ts-ignore  
                getter: (page) => page.frontmatter.category,  
                formatter: {  
                    "/": "分类：$content",  
                },            },            {                name: "tag",  
                // @ts-ignore  
                getter: (page) => page.frontmatter.tag,  
                formatter: {  
                    "/": "标签：$content",  
                },            },        ],    }),    live2dPlugin({  
        enable: true,  
        model: {  
            url: '/live2d-models/model-library/haru01/haru01.model.json'  
        },  
        display: {  
            position: 'right',  
            width: '135px',  
            height: '300px',  
            xOffset: '35px',  
            yOffset: '-45px'  
        },  
        mobile: {  
            show: true  
        },  
        react: {  
            opacity: 0.8  
        }  
    }),  
]}
```
:::

