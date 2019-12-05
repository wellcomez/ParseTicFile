# CREATE TABLE security(id INTEGER PRIMARY KEY,
# code VARCHAR, sequence INTEGER, instrument INTEGER, instrument_sub INTEGER,
# name_en VARCHAR, name_zh_cn VARCHAR, name_zh_hk VARCHAR, pinyin VARCHAR, pinyin_short VARCHAR, key_words VARCHAR,
# currency_code INTEGER, lot_size INTEGER, spread_code INTEGER,
# listing_date INTEGER,
# market_code INTEGER,
# warrnt_owner INTEGER, warrnt_type INTEGER, delete_flag INTEGER, linkage_stock_id INTEGER, plate_type INTEGER,
# tradetime_code INTEGER, delisted INTEGER, no_search INTEGER, no_subscription INTEGER, cas INTEGER, vcm INTEGER,
# margin INTEGER, sell_short INTEGER, underlying_stock_id INTEGER, adr_linkage_stock_id INTEGER )
import sqlite3
from constdefine import Market,KLType
import os
market_code_sh = 30
market_code_sz = 31
market_code_hk = 1
market_code_us = 10
market_code_map = {
    market_code_sz: Market.SZ,
    market_code_sh: Market.SH,
    market_code_us: Market.US,
}
Market.CN = 'CN'
market_name_to_code = {
    Market.SH: market_code_sh,
    Market.SZ: market_code_sz,
    Market.HK: market_code_hk,
    Market.US: market_code_us,
}


def get_stock_list(file='SecList.db', market_select=[Market.SH, Market.SZ]):
    conn = sqlite3.connect(file)
    c = conn.cursor()
    market_select = ' or ' .join(
        list(map(lambda x: 'market_code='+str(market_name_to_code[x]), market_select)))
    cursor = c.execute(
        'SELECT id,code,market_code ,name_zh_cn from security  WHERE  %s ' % (market_select))
    for row in cursor:
        stock_id, code, market_code, name_zh_cn = row
        market = market_code_map[market_code]
        print(stock_id, code, market, name_zh_cn)
    conn.close()

def parser_kldata_filename(file):
    file = os.path.basename(file)
    map2KLType = {
    '_min1':KLType.K_1M,
    '_min5':KLType.K_5M,
    '_min15':KLType.K_15M,
    '_min30':KLType.K_30M,
    '_min60':KLType.K_60M,
    '_month':KLType.K_MON,
    '_week':KLType.K_WEEK,
    '_day':KLType.K_DAY,
    }
    tv = None
    market = None
    if file[0:2]=='hk':
        market = Market.HK

    if file[0:2]=='cn':
        market = Market.CN

    for a in map2KLType:
        if file.find(a)!=-1:
            tv = map2KLType[a]
            break
    return market,tv
            
def build_kdata_index(file='cn_kl_day_1.db'):
    conn = sqlite3.connect(file)
    market,tv = parser_kldata_filename(file)
    c = conn.cursor()
    sql = 'select stock_id from KLData group by stock_id'
    cursor = c.execute(sql)
    ketlist = []
    for row in cursor:
        stock_id = row[0]
        ketlist.append(stock_id)
    conn.close()
    return tv,market,file,ketlist


