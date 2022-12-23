# -*-coding:utf-8-*-
# SettingCode here
__author__ = "a_little_rubbish"
__date__ = "2022/7/5 15:06"

# import your model here

import time
from contextlib import contextmanager

from queue import Empty
import multiprocessing
from multiprocessing import Manager

import timeline_spider
import detail_spider
import persistence
from conf import *


def is_done(status_table, p_type):
    """
    检查某一类线程是否全都结束了
    :param status_table: 状态表
    :param p_type: 线程类型
    :return:
    """
    done = []
    print("ProcessStatus:", status_table)
    for k, v in status_table[p_type].items():  # 遍历状态表

        if v == 0:  # 添加状态
            done.append(True)
        else:
            done.append(False)
    return all(done)  # 全完成就返回Tuee


@contextmanager
def process_info_logger(status_table, p_type, p_name):
    """
    进程函数状态管理
    :param status_table: 状态表
    :param p_type: 哪类进程
    :param p_name: 进程名，初始化用
    :return:
    """
    temp = status_table[p_type]  # 进程嵌套字典需要中间转一下赋值
    temp[p_name] = 1
    status_table[p_type] = temp
    print("%s starting..." % p_name)
    yield
    temp = status_table[p_type]  # 进程结束
    temp[p_name] = 0
    status_table[p_type] = temp
    print("%s has done" % p_name)


def timeline_crawler(status_table, detail_Q):
    """
    爬时间线的进程函数
    只能起一个，多用户才能多个，因为不能切片只能下滑
    """
    name = multiprocessing.current_process().name
    with process_info_logger(status_table, "timeline", name):
        cursor = ""  # 第一次为空
        while True:
            try:
                result = timeline_spider.crawl(cursor)
            except Exception as e: # 出现错误就返回
                print(e)
                break
            if result == 0:  # 这个人的已经爬完了
                break
            for i in result["detail_list"]:
                detail_Q.put(i)  # 结果加进去
            cursor = result["cursor"]  # 获得下一次的标

            time.sleep(TIMELINE_SLEEP)  # 控制频率


def detail_crawler(status_table, detail_Q, ready_data_Q):
    """
    爬推文细节的进程函数,放到ready_data_Q
    """
    name = multiprocessing.current_process().name

    with process_info_logger(status_table, "detail", name):
        while True:
            try:
                tw_id = detail_Q.get(timeout=3)

            except Empty as e:
                if is_done(status_table, "timeline"):
                    break
                continue
            except Exception as e:
                print(e)
                break
            ready_data = detail_spider.crawl(tw_id)
            ready_data_Q.put(ready_data)

            time.sleep(DETAIL_SLEEP)  # 控制频率


def persist(status_table, ready_data_Q):
    """
    从ready_data_Q拿数据持久化，存数据库
    """
    name = multiprocessing.current_process().name

    with process_info_logger(status_table, "persist", name):
        while True:
            try:
                data = ready_data_Q.get(timeout=3)
            except Empty as e:
                if is_done(status_table, "detail"):
                    break
                continue
            persistence.persist_sql(data)


def main():
    """
    主函数
    """
    pool = []
    for i in range(1, 2):  # 爬时间线的线程
        p = multiprocessing.Process(target=timeline_crawler,
                                    args=(status_table, detail_Q),
                                    name='timelineCrawlr%d' % i)
        pool.append(p)

    for i in range(1, 3):  # 爬推文的线程
        p = multiprocessing.Process(target=detail_crawler,
                                    args=(status_table, detail_Q, ready_data_Q),
                                    name='detailCrawler%d' % i)
        pool.append(p)

    for i in range(1, 3):  # 持久化线程
        p = multiprocessing.Process(target=persist,
                                    args=(status_table, ready_data_Q),
                                    name='persister%d' % i)
        pool.append(p)

    for i in pool:
        i.start()
    for i in pool:
        i.join()


if __name__ == '__main__':
    status_table = Manager().dict({"timeline": {}, "detail": {}, "persist": {}})  # 进程状态表,1是运行，0是运行结束
    detail_Q = Manager().Queue(maxsize=200)  # 每个tweet的id队列
    ready_data_Q = Manager().Queue(maxsize=200)  # 就绪数据队列\

    persistence.init_table()  # 初始化数据库
    main()
