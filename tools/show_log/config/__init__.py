# coding:utf-8

# 打印到控制台的log级别 1-debug  2-info 3-warn 4-error
PRINT_LOG_LEVEL = 2
# 比对过程中不同的字典
DICT_DIFF_PARAM = {}

DICT_LOG_MAP = {
    "1": ("/data/adn_logs/adnet/corsairreq", "midway"),
    "2": ("/data/adn_logs/corsair/request", "midway"),
    "3": ("/data/adn_logs/adnet/request", "adn"),
    "4": ("/data/adn_logs/stat_v3/request", "adn"),
    "5": ("/data/adn_logs/adnet/request", "adn"),
    "6": ("/data/adn_logs/stat_v3/request", "adn"),
    "7": ("/data/adn_logs/midway_tracking/play", "midway"),
    "8": ("/data/adn_logs/stat_v3/tracking", "adn"),
    "9": ("/data/adn_logs/stat_v3/tracking_no_report", "adn"),
    "10": ("/data/adn_logs/midway_tracking/impression", "midway"),
    "11": ("/data/adn_logs/midway_tracking/click", "midway"),
    "12": ("/data/adn_logs/midway_tracking/only_impression", "midway"),
    "13": ("/data/adn_logs/stat_v3/impression", "adn"),
    "14": ("/data/adn_logs/stat_v3/click", "adn"),
    "15": ("/data/adn_logs/stat_v3/only_impression", "adn")
}


DICT_LOG_KEYS = {
    "adn": [
        'date',
        'time',
        'created',
        'publisherId',
        'appId',
        'unitId',
        'advertiserId',
        'campaignId',
        'creativeId',
        'scenario',
        'adType',
        'imageSize',
        'requestType',
        'platform',
        'osVersion',
        'sdkVersion',
        'deviceModel',
        'screenSize',
        'orientation',
        'countryCode',
        'language',
        'networkType',
        'mobileCode',
        'extra',
        'extra2',
        'extra3',
        'extra4',
        'extra5',
        'extra6',
        'extra7',
        'extra8',
        'extra9',
        'extra10',
        'requestId',
        'ip',
        'imei',
        'mac',
        'devId',
        'serverId',
        'reduce',
        'priceIn',
        'priceOut',
        'googleAdvertisingId',
        'idfa',
        'appVersionName',
        'deviceBrand',
        'remoteIp',
        'sessionId',
        'parentSessionId',
        'extra11',
        'extra12',
        'extra13',
        'extra14',
        'extra15',
        'extra16',
        'extra17',
        'extra18',
        'extra19',
        'extra20',
        'ext_btclass',
        'ext_finalsubid',
        'ext_deleteDevid',
        'ext_installFrom',
        'ext_stats',
        'ext_packageName',
        'ext_nativeVideo',
        'ext_flowTagId',
        'ext_cdnType',
        'ext_endcard',
        'ext_rushNoPre',
        'ext_dspRealAppid',
        'ext_finalPackageName',
        'ext_nativex',
        'ext_attr',
        'ext_stats2',
        'ext_adstacking',
        'ext_ctype',
        'ext_rv_template',
        'ext_abtest1',
        'ext_creativeCdnFlag',
        'ext_creativeSizeFlag',
        'ext_playable',
        'ext_priceIn',
        'ext_priceOut',
        'ext_b2t',
        'ext_channel',
        'ext_advInstallTime',
        'ext_threesInstallTime',
        'ext_abtest2',
        'ext_bp',
        'ext_source',
        'ext_reject',
        'ext_algo',
        'ext_thirdCid',
        'ext_ifLowerImp',
        'ext_nvt2',
        'ext_trueNvt2',
        'ext_systemUseragent',
        'ext_autoClick'
    ],
    "midway": [
        "date",
        "created",
        "request_id",
        "publisherId",
        "appId",
        "unitId",
        "ad_backend",
        "ad_backend_data",
        "countryCode",
        "city_code",
        "platform",
        "adType",
        "osVersion",
        "sdkVersion",
        "appVersionName",
        "deviceBrand",
        "deviceModel",
        "screensize",
        "orientation",
        "language",
        "networkType",
        "mcc_mnc",
        "client_ip",
        "remoteIp",
        "server_ip",
        "imei",
        "mac",
        "android_id",
        "gaid",
        "idfa",
        "flow_tag_id",
        "request_num",
        "true_num",
        "rand_value",
        "backend_config",
        "play_info",
        "scenario"
    ]
}