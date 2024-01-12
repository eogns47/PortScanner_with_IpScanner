import os
import logging


def setLogger():
    if not os.path.isdir('../logs'):
        os.mkdir('../logs')

    #기본 설정된 werkzeug 로그 끄기
    logging.getLogger('werkzeug').disabled = True

    logging.basicConfig(filename = "../logs/crawler.log", level = logging.INFO
                    # , datefmt = '%Y/%m/%d %H:%M:%S %p'  # 년/월/일 시(12시간단위)/분/초 PM/AM
                    , datefmt = '%Y/%m/%d %H:%M:%S'  # 년/월/일 시(24시간단위)/분/초
                    , format = '%(asctime)s:%(levelname)s:%(message)s')