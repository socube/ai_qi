import tushare as ts
import pandas as pd
from get_data import engine, TABLE_STOCK, TABLE_STOCK_AREA, TABLE_STOCK_CONCEPT, TABLE_STOCK_INDUSTRY

'''
相关接口 get_stock_basics、get_industry_classified、get_area_classified、get_concept_classified

__tablename__ = 'Stock'
# 代码
code = Column(Integer, index=True)
# 股票名
name = Column(String)
# 细分行业
industry = Column(String)
# 地区
area = Column(String)
# 概念名称
c_name = Column(String)
# 上市日期
timeToMarket = Column(String)
'''


def sql_for_basic_stock():
    '''
    股票基础表
    :return:
    '''
    df = ts.get_stock_basics()
    name = df['name']
    timeToMarket = df['timeToMarket']
    df = pd.DataFrame({'name': name, 'timeToMarket': timeToMarket})
    df.to_sql(TABLE_STOCK, engine, if_exists='replace')


def sql_for_industry_stock():
    '''
    股票 行业表
    :return:
    '''
    df = ts.get_industry_classified()
    df.to_sql(TABLE_STOCK_INDUSTRY, engine, if_exists='replace')


def sql_for_area_stock():
    '''
    股票 地区表
    :return:
    '''
    df = ts.get_area_classified()
    df.to_sql(TABLE_STOCK_AREA, engine, if_exists='replace')


def sql_for_concept_stock():
    '''
    股票 概念表
    :return:
    '''
    df = ts.get_concept_classified()
    df.to_sql(TABLE_STOCK_CONCEPT, engine, if_exists='replace')


# sql_for_basic_stock()
# sql_for_industry_stock()
# sql_for_area_stock()
# sql_for_concept_stock()