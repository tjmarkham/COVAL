import requests
from datetime import datetime
from collections import namedtuple

# v0.1.315

# ******************************************************************************
#                            SET ZIP CODE RANGE HERE
# ******************************************************************************
#
# Set `zipMin` and `zipMax` variables below to limit what stores are searched.
#
# This is helpful so that someone living in, e.g. KoP, doesn't waste time
# looking at appointments in Pittsburgh while all of the KoP appointments are
# busy being taken.
#
# `zipMin` must always be less than your ZIP code, while `zipMax` must always be
# greater than your ZIP code.
#
# Example - if you live in 19406, set `zipMin` around `19100` and `zipMax`
# around `19700`.
#
# Too may results? Make `zipMin` higher and `zipMax` lower.
# Too few results? Make `zipMin` lower and `zipMax` higher.
# To search all stores, set `zipMin` to `0` and `zipMax` to `99999`.
#

zipMin = 00000
zipMax = 99999


# ******************************************************************************
#                              SET STORE DATA HERE
# ******************************************************************************
#
# To update the data used by this program, download the latest
# "Rite Aid - Week X" and "Pfizer Retail Pharmacy Partnership - Week X" Excel
# files from:
#
# https://www.health.pa.gov/topics/disease/coronavirus/Vaccine/Pages/Distribution.aspx
#
# Then use that data to update the variables below (`pfizerStoreNumbers`,
# `pfizerZipCodes`, `modernaStoreNumbers`, `modernaZipCodes`)
#

# Data from "Pfizer-BioNTech Doses to Retail Partners Week of March 8.xlsx"
# (file updated 3/10/2021)
pfizerStoreNumbers = [
    274,
    726,
    1355,
    1672,
    2248,
    4004,
    7880,
    7886,
    10904,
    10907,
    10908,
    10909,
    10939,
    10950,
    10995,
    11109,
    17783
]
pfizerZipCodes = [
    15217,
    18505,
    18322,
    19057,
    18436,
    18052,
    19454,
    17403,
    15101,
    15106,
    15108,
    15116,
    15224,
    15236,
    16148,
    19047,
    17050
]

# Data from "Rite Aid Week 8.xlsx"
# (file updated 3/8/2021)
modernaStoreNumbers = [
    170,
    188,
    205,
    208,
    213,
    218,
    229,
    232,
    233,
    264,
    291,
    293,
    321,
    415,
    451,
    467,
    501,
    517,
    558,
    596,
    679,
    696,
    721,
    729,
    740,
    790,
    793,
    803,
    819,
    856,
    857,
    866,
    923,
    926,
    992,
    995,
    1081,
    1144,
    1274,
    1304,
    1314,
    1320,
    1370,
    1398,
    1406,
    1415,
    1429,
    1448,
    1450,
    1494,
    1495,
    1496,
    1514,
    1548,
    1566,
    1567,
    1640,
    1662,
    1668,
    1699,
    1709,
    1733,
    1758,
    1780,
    1800,
    1830,
    1887,
    1894,
    1902,
    1922,
    1925,
    1955,
    1963,
    1975,
    1976,
    2017,
    2264,
    2271,
    2277,
    2380,
    2382,
    2426,
    2433,
    2442,
    2474,
    2476,
    2478,
    2480,
    2631,
    2693,
    2768,
    2769,
    2797,
    3273,
    3400,
    3425,
    3443,
    3447,
    3449,
    3527,
    3602,
    3609,
    3610,
    3768,
    3804,
    3972,
    4256,
    4284,
    4286,
    4288,
    4293,
    4415,
    4616,
    4682,
    4684,
    4840,
    6738,
    6739,
    6778,
    7850,
    7853,
    7861,
    10888,
    10890,
    10891,
    10899,
    10900,
    10914,
    10919,
    10934,
    10954,
    10958,
    10962,
    10964,
    10967,
    10975,
    10976,
    10979,
    10983,
    10987,
    10988,
    10990,
    10991,
    10994,
    10998,
    10999,
    11002,
    11015,
    11016,
    11018,
    11019,
    11021,
    11023,
    11025,
    11034,
    11036,
    11038,
    11040,
    11045,
    11058,
    11059,
    11060,
    11062,
    11073,
    11076,
    11082,
    11084,
    11093,
    11096,
    11097,
    11099,
    11100,
    11101,
    11104,
    11105,
    11110,
    11113,
    11116,
    11117,
    11119,
    11122,
    11142,
    11148,
    11151,
    11158,
    11160,
    11162,
    11166,
    11169,
    11170,
    12999
]
modernaZipCodes = [
    18301,
    19006,
    17872,
    17976,
    16504,
    18634,
    18431,
    17222,
    16652,
    15701,
    18951,
    18974,
    19363,
    18701,
    17404,
    19611,
    18503,
    17401,
    19001,
    16407,
    19082,
    17948,
    17101,
    17603,
    16830,
    19083,
    16801,
    15901,
    19464,
    19076,
    19003,
    17104,
    19053,
    15370,
    19320,
    19087,
    19026,
    19087,
    19014,
    17113,
    18661,
    19072,
    15132,
    16438,
    16735,
    19382,
    15537,
    15108,
    18071,
    15714,
    17066,
    16301,
    15419,
    16242,
    19036,
    19008,
    17356,
    17078,
    16121,
    16417,
    15683,
    19403,
    19018,
    15963,
    18302,
    18848,
    17110,
    17315,
    17362,
    17566,
    15045,
    18466,
    15401,
    19608,
    16915,
    19401,
    19013,
    17345,
    15009,
    16335,
    16508,
    18704,
    15066,
    19050,
    16743,
    15853,
    17921,
    15059,
    19064,
    17954,
    18407,
    16137,
    19027,
    19002,
    19567,
    19526,
    15442,
    16127,
    16125,
    15136,
    17350,
    17201,
    17512,
    19335,
    17074,
    16146,
    19001,
    17109,
    17090,
    17032,
    17020,
    17701,
    16354,
    15120,
    17602,
    18201,
    16648,
    16686,
    18101,
    15834,
    15857,
    19543,
    15001,
    15010,
    15012,
    15068,
    15068,
    15136,
    15146,
    15221,
    15238,
    15301,
    15401,
    15425,
    15601,
    15767,
    15801,
    15904,
    16001,
    16046,
    16046,
    16101,
    16105,
    16142,
    16201,
    16316,
    16323,
    16823,
    16901,
    17013,
    17019,
    17042,
    17257,
    17319,
    17584,
    17701,
    17815,
    18017,
    18045,
    18235,
    18235,
    18252,
    18344,
    18603,
    18657,
    18801,
    18848,
    18954,
    19006,
    18976,
    19006,
    19007,
    19010,
    19025,
    19026,
    19047,
    19063,
    19073,
    19082,
    19087,
    19096,
    19320,
    19348,
    19380,
    19406,
    19428,
    19446,
    19465,
    19530,
    19602,
    17331
]

#*******************************************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   DO NOT MODIFY ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#*******************************************************************************

Store = namedtuple('Store', 'number zipCode')

def makeListOfStores(list1, list2):
    tupleLamabda = lambda element1, element2: Store(element1, element2)
    return list(map(tupleLamabda, list1, list2))

print()
print('======================================================================')
print('                                 COVAL                                ')
print('                 COVID-19 Vaccine Appointment Locator                 ')
print('                  Pennsylvania Rite Aid Stores ONLY                   ')
print('======================================================================')
print()

print('Date / time:')
print()
print('  ', datetime.now())
print()

print('ZIP code range:')
print()
print('  ', zipMin, '-', zipMax)
print()

testStoreNumbers = [
    274,
    726,
    1355
]
testZipCodes = [
    15217,
    18505,
    18322,
]
testStores = makeListOfStores(testStoreNumbers, testZipCodes)

allStoreNumbers = pfizerStoreNumbers + modernaStoreNumbers
allZipCodes = pfizerZipCodes + modernaZipCodes
allStores = makeListOfStores(allStoreNumbers, allZipCodes)
closeStores = []

for store in allStores:
    zipCode = store.zipCode
    if (zipCode >= zipMin and zipCode <= zipMax):
        closeStores.append(store)

storesWithSlot1 = []
storesWithSlot2 = []
storesWithErrors = []

print('Finding slots:')

#storesToCheck = testStores
storesToCheck = closeStores

for store in storesToCheck:
    storeNumber = store.number
    url = 'https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber=' + str(storeNumber)
    websiteRequest = requests.get(url)

    if (websiteRequest):
        jsonData = websiteRequest.json()

        status = jsonData.get('Status')
        #errorCode = jsonData.get('ErrCde')
        #errorMessage = jsonData.get('ErrMsg')
        #errorMessageDetail = jsonData.get('ErrMsgDtl')

        if (status == 'ERROR'):
            storesWithErrors.append(store)
            print('E', end = '', flush = True)
        else:
            data = jsonData.get('Data')
            slots = data.get('slots')
            slot1 = slots.get('1')
            slot2 = slots.get('2')

            if (slot1):
                storesWithSlot1.append(store)
                print('1', end = '', flush = True)
            elif (slot2):
                storesWithSlot2.append(store)
                print('2', end = '', flush = True)
            else:
                print('.', end = '', flush = True)
    else: # url request failed
        storesWithErrors.append(store)
        print('E', end = '', flush = True)

print()
print()

storesWithSlots = list(set(storesWithSlot1) | set(storesWithSlot2))
storesWithSlotsCount = len(storesWithSlots)
totalStoreCount = len(allStores)
checkedStoreCount = len(storesToCheck)
storesWithErrorsCount = len(storesWithErrors)

print('Results:')
print()
print('   ', checkedStoreCount, ' out of ', totalStoreCount, ' stores within ZIP code range analyzed (', storesWithErrorsCount, ' errors)', sep = '')
print()
print('  ', storesWithSlotsCount, 'stores with available slots')
print()

if (len(storesWithSlots) > 0):
    print('  ', '{: <9} {: >8} {: >11}'.format(*['Result #', 'Store #', 'ZIP code']))
    for resultNumber, store in enumerate(storesWithSlots, start = 1):
        print('  ', '{: <9}'.format(resultNumber), end = '')
        print('', '   {:0>5} {: >11}'.format(*store))
else:
    print('  ', 'None')

print()
print('======================================================================')
print()
