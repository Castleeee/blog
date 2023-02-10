---
title: fastapi-sqlalchemy
date: 2023-01-09 21:43:28
order: 2
category:
- python🐍
- fastAPI⚡
tag:
- python🐍
- fastAPI⚡
- sqlalchemy
---

## sqlalchemy

sqlalchemy是python的orm工具，被整合进fastapi里面了  


## 踩过的坑
### 懒加载
默认的sqlalchemy的session是懒加载的，有时候update数据不进去可以考虑这个原因，使用`session.__repr__()`无感调用实现加载

### update的时候报错
update的时候synchronize_session=False参数的诡异问题
#todo 忘了哪个错误了，回头搞一下 

### 插入json字汉字被unicode编码
插入json字段的时候，其中的汉字被编码为`\u4f60\u597d` 这样在数据库里和日志里都是unicode编码，但是查出来之后是正常的。   
检查sqlalchemy的engine，pg的client db都是utf-8但是不知道为啥哪里还是latin1(我恨他)  
 [^2] 
```sql
select * from users;
alice|["𝓓𝓞Γ"]
bob|["\ud835\udcd3\ud835\udcde\u0393"]
```

在issue[^1]里有人问了，最后官方加上了个参数[^3]
在create_engine申请的时候加入参数指定json序列化器  
```python
engine = create_engine("mysql://scott:tiger@hostname/dbname",
                       encoding='utf8', echo=True,
                       json_serializer=lambda x: json.dumps(x, ensure_ascii=False))
```
之后存数据库就不会了  

## json字段的模糊查询
#todo pgsql的json字段模糊查询

### session传递和生命周期
python根据函数实际参数的类型不同进行传递:
1.  值传递：适用于实参类型为不可变类型（字符串、数字、元组）
2.  引用（地址）传递：适用于实参类型为可变类型（列表，字典）

sqlalchemy 的session是引用传递，在函数中传递的时候，子函数查询完了，在外层中可以读出来。  
>查询出来的ORM对象本身在 [`Session`](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.Session "sqlalchemy.orm.Session") ，在名为 [identity map](https://www.osgeo.cn/sqlalchemy/glossary.html#term-identity-map) -维护每个对象唯一副本的数据结构，其中“唯一”表示“只有一个具有特定主键的对象”。  Session以无状态的形式开始。一旦发出查询或其他对象被持久化，它将从 [`Engine`](https://www.osgeo.cn/sqlalchemy/core/connections.html#sqlalchemy.engine.Engine "sqlalchemy.engine.Engine") 与 [`Session`](https://www.osgeo.cn/sqlalchemy/orm/session_api.html#sqlalchemy.orm.Session "sqlalchemy.orm.Session") ，然后在该连接上建立一个事务  .  

也就是说在执行query之后的db对象维护的identity map不变，所以对这些对象还可以进行其他操作，但是此时如果query之后再update那么缓冲区就变成了update的结果，此时无法进行其他操作  
session相当于每个query返回一个cur，多个query实际上是分离的  
所以同一个query，应该先查出数据来再修改，但是取出来的数据会和db里面的不一致


## Redis

#TODO Redis OM aioredis构建池，fastapi如何同步的建立redis连接池，普通使用如何建立连接池，怎样让redis链接随着app启动和关闭  
[小记一次FastAPI使用连接池调用Redis时，切换数据库的问题 - 一灰的随手记](https://yihuilu.github.io/Blog/archives/FastAPI%20Redis%20aioredis/)  

[^1]: [Error when querying JSON columns with wide unicode characters. · Issue #4798 · sqlalchemy/sqlalchemy · GitHub](https://github.com/sqlalchemy/sqlalchemy/issues/4798)<br/>
[^2]: [Correct name for json_serializer / json_deserializer, document and test (I1dbfe439) · Gerrit Code Review](https://gerrit.sqlalchemy.org/c/sqlalchemy/sqlalchemy/+/1400/)<br/>
[^3]: [引擎配置 — SQLAlchemy 1.4 Documentation](https://www.osgeo.cn/sqlalchemy/core/engines.html?highlight=json_serializer#sqlalchemy.create_engine.params.json_serializer)