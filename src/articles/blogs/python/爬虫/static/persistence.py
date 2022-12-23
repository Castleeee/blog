# -*-coding:utf-8-*-
# SettingCode here
__author__ = "a_little_rubbish"
__date__ = "2022/7/6 10:00"

from sqlalchemy import Column, String, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()  # 生成Model类的基类


class Posts(Base):
    # 表的名字:
    __tablename__ = 'posts'

    # 表的结构:
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)  # 资增int主键
    main_posts = Column(Text, nullable=False)  # 主推文
    reply = Column(Text)  # 回复

    def __repr__(self):
        return 'Posts(id={}, posts={}, reply={})'.format(self.id, self.main_posts, self.reply)

    def __str__(self):
        return self.__repr__()


def init_table():
    engine = create_engine('mysql+pymysql://root:1118@127.0.0.1:3306/twitter', echo=True)
    Base.metadata.drop_all(engine)  # 删除所有表
    Base.metadata.create_all(engine)  # 创建所有表


def persist_sql(data):
    """
    持久化到sql的函数
    :param data: json数据，存sql
    :return:
    """
    engine = create_engine('mysql+pymysql://root:1118@127.0.0.1:3306/twitter', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 格式变一下
    main_posts = ";".join(data["posts"])
    reply = ";".join(data["reply"])

    print("inserting data", data)

    # 插入
    p = Posts(main_posts=main_posts, reply=reply)
    session.add(p)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


if __name__ == "__main__":
    # 测试数据
    demodata = {'posts': [
        '@DamonAlbarn I was such a big fan of yours until I saw this. I write ALL of my own songs. Your hot take is completely false and SO damaging. You don’t have to like my songs but it’s really fucked up to try and discredit my writing. WOW.'],
        'reply': ['PS I wrote this tweet all by myself in case you were wondering 😑',
                  '@taylorswift13 I totally agree with you. i had a conversation about songwriting and sadly it was reduced to clickbait. I apologise unreservedly and unconditionally. The last thing I would want to do is discredit your songwriting. I hope you understand. - Damon',
                  '@taylorswift13 @Damonalbarn يابنت الحلال اطلعي خلاص وجع',
                  '@taylorswift13 @Damonalbarn Must you use foul language? I understand your point and im a Christian and this just is upsetting to see ladies use such language. Im a great grandmother, grandmother and mother....I like your music just the language is upsetting.',
                  '@taylorswift13 @Damonalbarn Just gonna leave this here. Look at all of these cowrites @Damonalbarn \n\n“Day doo de bop\nDay doo de bop” really required multiple writers to come up with that… https://t.co/aU8g9bD2rx',
                  "@taylorswift13 @Damonalbarn what the fuck taylor you can't just say fucking it's rude",
                  '@taylorswift13 @Damonalbarn OMG I JUST WOKE UP TO SEE TAYLOR SWIFT END A MAN YESSSSS https://t.co/3CAAXx1VGe',
                  '@taylorswift13 @Damonalbarn https://t.co/Qb8BbHxFSY',
                  '@taylorswift13 @Damonalbarn he’s just jealous he doesn’t have tons of awards like this shiny songwriter of the year 2020 award😌 https://t.co/JdwEN18dBT']}
    init_table()
    persist_sql(demodata)
