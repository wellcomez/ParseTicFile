class KLType(object):
    """
    k线类型定义
    ..  py:class:: KLType
     ..  py:attribute:: K_1M
      1分钟K线
     ..  py:attribute:: K_5M
      5分钟K线
     ..  py:attribute:: K_15M
      15分钟K线
     ..  py:attribute:: K_30M
      30分钟K线
     ..  py:attribute:: K_60M
      60分钟K线
     ..  py:attribute:: K_DAY
      日K线
     ..  py:attribute:: K_WEEK
      周K线
     ..  py:attribute:: K_MON
      月K线
    """
    K_1M = "K_1M"
    K_3M = "K_3M"
    K_5M = "K_5M"
    K_15M = "K_15M"
    K_30M = "K_30M"
    K_60M = "K_60M"
    K_DAY = "K_DAY"
    K_WEEK = "K_WEEK"
    K_MON = "K_MON"
    K_1M = "K_1M"
    K_QUARTER = "K_QUARTER"
    K_YEAR = "K_YEAR"


KTYPE_MAP = {
    KLType.K_1M: 1,
    KLType.K_3M: 10,
    KLType.K_5M: 6,
    KLType.K_15M: 7,
    KLType.K_30M: 8,
    KLType.K_60M: 9,
    KLType.K_DAY: 2,
    KLType.K_WEEK: 3,
    KLType.K_MON: 4,
    KLType.K_QUARTER: 11,
    KLType.K_YEAR: 5
}



# 实时数据定阅类型
class SubType(object):
    """
    实时数据定阅类型定义
    ..  py:class:: SubType
     ..  py:attribute:: TICKER
      逐笔
     ..  py:attribute:: QUOTE
      报价
     ..  py:attribute:: ORDER_BOOK
      买卖摆盘
     ..  py:attribute:: K_1M
      1分钟K线
     ..  py:attribute:: K_5M
      5分钟K线
     ..  py:attribute:: K_15M
      15分钟K线
     ..  py:attribute:: K_30M
      30分钟K线
     ..  py:attribute:: K_60M
      60分钟K线
     ..  py:attribute:: K_DAY
      日K线
     ..  py:attribute:: K_WEEK
      周K线
     ..  py:attribute:: K_MON
      月K线
     ..  py:attribute:: RT_DATA
      分时
     ..  py:attribute:: BROKER
      买卖经纪
     ..  py:attribute:: ORDER_DETAIL
      委托明细
    """
    TICKER = "TICKER"
    QUOTE = "QUOTE"
    ORDER_BOOK = "ORDER_BOOK"
    # ORDER_DETAIL = "ORDER_DETAIL"
    K_1M = "K_1M"
    K_3M = "K_3M"
    K_5M = "K_5M"
    K_15M = "K_15M"
    K_30M = "K_30M"
    K_60M = "K_60M"
    K_DAY = "K_DAY"
    K_WEEK = "K_WEEK"
    K_MON = "K_MON"
    K_QUARTER = "K_QUARTER"
    K_YEAR = "K_YEAR"
    RT_DATA = "RT_DATA"
    BROKER = "BROKER"


KLINE_SUBTYPE_LIST = [SubType.K_DAY, SubType.K_MON, SubType.K_WEEK,
                      SubType.K_1M, SubType.K_3M, SubType.K_5M, SubType.K_15M,
                      SubType.K_30M, SubType.K_60M, SubType.K_QUARTER, SubType.K_YEAR,
                      ]


SUBTYPE_MAP = {
    SubType.QUOTE: 1,
    SubType.ORDER_BOOK: 2,
    SubType.TICKER: 4,
    SubType.RT_DATA: 5,
    SubType.K_DAY: 6,
    SubType.K_5M: 7,
    SubType.K_15M: 8,
    SubType.K_30M: 9,
    SubType.K_60M: 10,
    SubType.K_1M: 11,
    SubType.K_WEEK: 12,
    SubType.K_MON: 13,
    SubType.BROKER: 14,
    SubType.K_QUARTER: 15,
    SubType.K_YEAR: 16,
    SubType.K_3M: 17,
    # SubType.ORDER_DETAIL: 18
}


class Market(object):
    """
    标识不同的行情市场，股票名称的前缀复用该字符串,如 **'HK.00700'**, **'HK_FUTURE.999010'**
    ..  py:class:: Market
     ..  py:attribute:: HK
      港股
     ..  py:attribute:: US
      美股
     ..  py:attribute:: SH
      沪市
     ..  py:attribute:: SH
      深市
     ..  py:attribute:: HK_FUTURE
      港股期货
     ..  py:attribute:: NONE
      未知
    """
    HK = "HK"
    US = "US"
    SH = "SH"
    SZ = "SZ"
    HK_FUTURE = "HK_FUTURE"
    NONE = "N/A"


MKT_MAP = {
    Market.NONE: 0,
    Market.HK: 1,
    Market.HK_FUTURE: 2,
    Market.US: 11,
    Market.SH: 21,
    Market.SZ: 22
}


USPRE = 'USPRE'
RT_DATA_PRE = 'RT_DATA_PRE'

ktypemap = {
    KLType.K_1M: '1min',
    KLType.K_5M: '5min',
    KLType.K_15M: '15min',
    KLType.K_30M: '30min',
    KLType.K_60M: '60min',
    KLType.K_DAY: 'day',
    KLType.K_WEEK: 'week',
    KLType.K_MON: 'month',
    KLType.K_YEAR: 'year'
}
tv2Ktypemap = {}
for k in ktypemap:
    tv2Ktypemap[ktypemap[k]] = k

def get_code_market(market, codeall):
    try:
        b = codeall.split('.')
        code = b[1]
        if market is None:
            market = b[0]
            market = market.replace('"', '')
    except:
        code = codeall
        pass
    return code, market
