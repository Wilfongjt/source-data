import pandas as pd
import p3_data_structures as stru
def get_patient_dataframe():
    return pd.DataFrame.from_dict({'age': {517: 43,
  1201: 43,
  1315: 16,
  1570: 6,
  2093: 60,
  2647: 43,
  3314: 88,
  4006: 56,
  4225: 28,
  5988: 56,
  6910: 52,
  8203: 10,
  9001: 72,
  10857: 1,
  11271: 2,
  14812: 45,
  15257: 21,
  18384: 62,
  18687: 47,
  19090: 20,
  20044: 12,
  20058: 48,
  22811: 71,
  23378: 48,
  23569: 55,
  26655: 30,
  26750: 52,
  26970: 69,
  30334: 15,
  30551: 39,
  32578: 22,
  35258: 36,
  36919: 2,
  37329: 7,
  37570: 73,
  42736: 61,
  43274: 50,
  44572: 78,
  46048: 48,
  48084: 15,
  48252: 44,
  49163: 73,
  54018: 17,
  57334: 38,
  57725: 79,
  57962: 77,
  58877: 1,
  61283: 31,
  61492: 55,
  61770: 85},
 'alcoholism': {517: 0,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 1,
  2647: 0,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 0,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 0,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 0,
  30334: 0,
  30551: 0,
  32578: 0,
  35258: 0,
  36919: 0,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 0,
  48252: 0,
  49163: 0,
  54018: 0,
  57334: 0,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0},
 'appointments': {517: 1,
  1201: 4,
  1315: 2,
  1570: 2,
  2093: 2,
  2647: 6,
  3314: 5,
  4006: 5,
  4225: 5,
  5988: 2,
  6910: 1,
  8203: 2,
  9001: 4,
  10857: 2,
  11271: 2,
  14812: 3,
  15257: 2,
  18384: 3,
  18687: 1,
  19090: 2,
  20044: 1,
  20058: 1,
  22811: 2,
  23378: 2,
  23569: 1,
  26655: 5,
  26750: 1,
  26970: 1,
  30334: 1,
  30551: 2,
  32578: 2,
  35258: 1,
  36919: 1,
  37329: 1,
  37570: 1,
  42736: 1,
  43274: 1,
  44572: 1,
  46048: 2,
  48084: 1,
  48252: 3,
  49163: 1,
  54018: 5,
  57334: 1,
  57725: 1,
  57962: 1,
  58877: 1,
  61283: 1,
  61492: 1,
  61770: 1},
 'diabetes': {517: 0,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 0,
  2647: 0,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 0,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 0,
  18384: 1,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 1,
  30334: 0,
  30551: 0,
  32578: 0,
  35258: 0,
  36919: 0,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 0,
  48252: 0,
  49163: 0,
  54018: 0,
  57334: 0,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0},
 'female': {517: 0,
  1201: 1,
  1315: 1,
  1570: 1,
  2093: 1,
  2647: 0,
  3314: 1,
  4006: 1,
  4225: 1,
  5988: 1,
  6910: 1,
  8203: 0,
  9001: 1,
  10857: 0,
  11271: 1,
  14812: 0,
  15257: 1,
  18384: 1,
  18687: 1,
  19090: 1,
  20044: 1,
  20058: 0,
  22811: 1,
  23378: 1,
  23569: 1,
  26655: 1,
  26750: 0,
  26970: 1,
  30334: 0,
  30551: 0,
  32578: 1,
  35258: 1,
  36919: 0,
  37329: 1,
  37570: 1,
  42736: 1,
  43274: 1,
  44572: 1,
  46048: 1,
  48084: 0,
  48252: 0,
  49163: 0,
  54018: 1,
  57334: 1,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 1,
  61492: 1,
  61770: 1},
 'gender': {517: 1,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 0,
  2647: 1,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 1,
  9001: 0,
  10857: 1,
  11271: 0,
  14812: 1,
  15257: 0,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 1,
  26970: 0,
  30334: 1,
  30551: 1,
  32578: 0,
  35258: 0,
  36919: 1,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 1,
  48252: 1,
  49163: 1,
  54018: 0,
  57334: 0,
  57725: 1,
  57962: 1,
  58877: 1,
  61283: 0,
  61492: 0,
  61770: 0},
 'handcap': {517: 0,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 0,
  2647: 0,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 0,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 0,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 0,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 0,
  30334: 0,
  30551: 0,
  32578: 0,
  35258: 0,
  36919: 0,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 0,
  48252: 0,
  49163: 1,
  54018: 0,
  57334: 0,
  57725: 0,
  57962: 1,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0},
 'hipertension': {517: 1,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 1,
  2647: 0,
  3314: 1,
  4006: 0,
  4225: 0,
  5988: 1,
  6910: 0,
  8203: 0,
  9001: 1,
  10857: 0,
  11271: 0,
  14812: 1,
  15257: 0,
  18384: 1,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 0,
  22811: 1,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 1,
  30334: 0,
  30551: 0,
  32578: 0,
  35258: 0,
  36919: 0,
  37329: 0,
  37570: 1,
  42736: 0,
  43274: 0,
  44572: 1,
  46048: 0,
  48084: 0,
  48252: 0,
  49163: 1,
  54018: 0,
  57334: 0,
  57725: 0,
  57962: 1,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 1},
 'male': {517: 1,
  1201: 0,
  1315: 0,
  1570: 0,
  2093: 0,
  2647: 1,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 1,
  9001: 0,
  10857: 1,
  11271: 0,
  14812: 1,
  15257: 0,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 0,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 1,
  26970: 0,
  30334: 1,
  30551: 1,
  32578: 0,
  35258: 0,
  36919: 1,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 1,
  48252: 1,
  49163: 1,
  54018: 0,
  57334: 0,
  57725: 1,
  57962: 1,
  58877: 1,
  61283: 0,
  61492: 0,
  61770: 0},
 'no_shows': {517: 0,
  1201: 1,
  1315: 0,
  1570: 2,
  2093: 1,
  2647: 0,
  3314: 0,
  4006: 1,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 0,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 1,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 1,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 0,
  30334: 0,
  30551: 1,
  32578: 0,
  35258: 0,
  36919: 1,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 1,
  44572: 0,
  46048: 0,
  48084: 1,
  48252: 1,
  49163: 0,
  54018: 0,
  57334: 1,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0},
 'patient_id': {517: 5981284675659,
  1201: 655178995128,
  1315: 867939654645914,
  1570: 31567938888819,
  2093: 186446542345557,
  2647: 31791955269122,
  3314: 3176755233235,
  4006: 58348141577833,
  4225: 6318759887818,
  5988: 47139771421218,
  6910: 31535687964361,
  8203: 8593573479798,
  9001: 589994953262624,
  10857: 5935996648517,
  11271: 166488596585128,
  14812: 1435465416,
  15257: 5153179397485,
  18384: 65569547255497,
  18687: 84583575348792,
  19090: 245228567791123,
  20044: 69951422599455,
  20058: 622214244874144,
  22811: 49526323237883,
  23378: 5217762165383,
  23569: 94625184729987,
  26655: 92164812584834,
  26750: 621641795796522,
  26970: 19789149685985,
  30334: 8862282115788,
  30551: 6725574494387,
  32578: 32454612476629,
  35258: 67223931585819,
  36919: 32543176819,
  37329: 41456369623794,
  37570: 8684118659383,
  42736: 123958312559695,
  43274: 381175387273,
  44572: 9147174923,
  46048: 417227523597638,
  48084: 368852569996353,
  48252: 714453526688231,
  49163: 22815554764481,
  54018: 6229533559636,
  57334: 475279179783251,
  57725: 19243516978413,
  57962: 8144234824461,
  58877: 689472872464323,
  61283: 9674825536277,
  61492: 479353655841,
  61770: 268829849475},
 'scholarship': {517: 0,
  1201: 0,
  1315: 0,
  1570: 1,
  2093: 0,
  2647: 0,
  3314: 0,
  4006: 0,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 1,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 0,
  18384: 0,
  18687: 1,
  19090: 0,
  20044: 0,
  20058: 0,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 0,
  30334: 0,
  30551: 0,
  32578: 0,
  35258: 0,
  36919: 0,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 0,
  44572: 0,
  46048: 0,
  48084: 0,
  48252: 1,
  49163: 0,
  54018: 0,
  57334: 0,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0},
 'skipper': {517: 0,
  1201: 1,
  1315: 0,
  1570: 1,
  2093: 1,
  2647: 0,
  3314: 0,
  4006: 1,
  4225: 0,
  5988: 0,
  6910: 0,
  8203: 0,
  9001: 0,
  10857: 0,
  11271: 0,
  14812: 0,
  15257: 1,
  18384: 0,
  18687: 0,
  19090: 0,
  20044: 1,
  20058: 1,
  22811: 0,
  23378: 0,
  23569: 0,
  26655: 0,
  26750: 0,
  26970: 0,
  30334: 0,
  30551: 1,
  32578: 0,
  35258: 0,
  36919: 1,
  37329: 0,
  37570: 0,
  42736: 0,
  43274: 1,
  44572: 0,
  46048: 0,
  48084: 1,
  48252: 1,
  49163: 0,
  54018: 0,
  57334: 1,
  57725: 0,
  57962: 0,
  58877: 0,
  61283: 0,
  61492: 0,
  61770: 0}})

def get_appointment_dataframe():
    return pd.DataFrame.from_dict({'age': {1203: 14,
  1267: 23,
  3915: 61,
  6539: 51,
  7662: 45,
  7861: 9,
  7956: 16,
  9153: 19,
  9389: 17,
  9463: 60,
  10260: 12,
  11129: 5,
  14008: 57,
  18361: 76,
  23572: 69,
  25771: 6,
  27205: 39,
  27355: 20,
  29145: 44,
  29347: 34,
  30610: 36,
  34532: 65,
  36688: 2,
  37136: 7,
  43160: 7,
  49295: 19,
  49500: 87,
  52314: 10,
  54788: 51,
  58232: 85,
  59518: 90,
  65139: 16,
  65866: 62,
  72117: 69,
  74309: 59,
  78590: 0,
  79795: 20,
  85642: 47,
  85920: 5,
  87655: 44,
  88857: 6,
  91910: 54,
  96070: 53,
  97615: 14,
  102454: 43,
  102941: 67,
  103389: 17,
  108127: 26,
  108902: 4,
  110383: 8},
 'appointment_id': {1203: 5635691,
  1267: 5578980,
  3915: 5644272,
  6539: 5637418,
  7662: 5696148,
  7861: 5726445,
  7956: 5730706,
  9153: 5722604,
  9389: 5641515,
  9463: 5596391,
  10260: 5665613,
  11129: 5528081,
  14008: 5702862,
  18361: 5617599,
  23572: 5541580,
  25771: 5700709,
  27205: 5368098,
  27355: 5629810,
  29145: 5643511,
  29347: 5648324,
  30610: 5684900,
  34532: 5656679,
  36688: 5733124,
  37136: 5620508,
  43160: 5674013,
  49295: 5574785,
  49500: 5565815,
  52314: 5657468,
  54788: 5625743,
  58232: 5627073,
  59518: 5709621,
  65139: 5605321,
  65866: 5607972,
  72117: 5705472,
  74309: 5721683,
  78590: 5685473,
  79795: 5616937,
  85642: 5789386,
  85920: 5780512,
  87655: 5783585,
  88857: 5685794,
  91910: 5669607,
  96070: 5770568,
  97615: 5769120,
  102454: 5780368,
  102941: 5784174,
  103389: 5776474,
  108127: 5766429,
  108902: 5755089,
  110383: 5747442},
 'attendance': {1203: 1,
  1267: 1,
  3915: 1,
  6539: 1,
  7662: 1,
  7861: 1,
  7956: 1,
  9153: 1,
  9389: 0,
  9463: 1,
  10260: 0,
  11129: 1,
  14008: 1,
  18361: 1,
  23572: 1,
  25771: 1,
  27205: 1,
  27355: 1,
  29145: 1,
  29347: 0,
  30610: 1,
  34532: 1,
  36688: 1,
  37136: 1,
  43160: 1,
  49295: 1,
  49500: 0,
  52314: 1,
  54788: 1,
  58232: 1,
  59518: 1,
  65139: 1,
  65866: 1,
  72117: 1,
  74309: 1,
  78590: 1,
  79795: 1,
  85642: 1,
  85920: 1,
  87655: 1,
  88857: 1,
  91910: 1,
  96070: 1,
  97615: 1,
  102454: 1,
  102941: 1,
  103389: 1,
  108127: 1,
  108902: 1,
  110383: 1},
 'attendance_label': {1203: 'Show',
  1267: 'Show',
  3915: 'Show',
  6539: 'Show',
  7662: 'Show',
  7861: 'Show',
  7956: 'Show',
  9153: 'Show',
  9389: 'No-Show',
  9463: 'Show',
  10260: 'No-Show',
  11129: 'Show',
  14008: 'Show',
  18361: 'Show',
  23572: 'Show',
  25771: 'Show',
  27205: 'Show',
  27355: 'Show',
  29145: 'Show',
  29347: 'No-Show',
  30610: 'Show',
  34532: 'Show',
  36688: 'Show',
  37136: 'Show',
  43160: 'Show',
  49295: 'Show',
  49500: 'No-Show',
  52314: 'Show',
  54788: 'Show',
  58232: 'Show',
  59518: 'Show',
  65139: 'Show',
  65866: 'Show',
  72117: 'Show',
  74309: 'Show',
  78590: 'Show',
  79795: 'Show',
  85642: 'Show',
  85920: 'Show',
  87655: 'Show',
  88857: 'Show',
  91910: 'Show',
  96070: 'Show',
  97615: 'Show',
  102454: 'Show',
  102941: 'Show',
  103389: 'Show',
  108127: 'Show',
  108902: 'Show',
  110383: 'Show'},
 'no_show': {1203: 0,
  1267: 0,
  3915: 0,
  6539: 0,
  7662: 0,
  7861: 0,
  7956: 0,
  9153: 0,
  9389: 1,
  9463: 0,
  10260: 1,
  11129: 0,
  14008: 0,
  18361: 0,
  23572: 0,
  25771: 0,
  27205: 0,
  27355: 0,
  29145: 0,
  29347: 1,
  30610: 0,
  34532: 0,
  36688: 0,
  37136: 0,
  43160: 0,
  49295: 0,
  49500: 1,
  52314: 0,
  54788: 0,
  58232: 0,
  59518: 0,
  65139: 0,
  65866: 0,
  72117: 0,
  74309: 0,
  78590: 0,
  79795: 0,
  85642: 0,
  85920: 0,
  87655: 0,
  88857: 0,
  91910: 0,
  96070: 0,
  97615: 0,
  102454: 0,
  102941: 0,
  103389: 0,
  108127: 0,
  108902: 0,
  110383: 0},
 'patient_id': {1203: 141646244146,
  1267: 61893284664,
  3915: 637856944154716,
  6539: 52349343461228,
  7662: 89239687393655,
  7861: 534349183459,
  7956: 786887452499318,
  9153: 83718455216416,
  9389: 527228142197,
  9463: 74445528337867,
  10260: 5588216122471,
  11129: 343585374351119,
  14008: 54874349811574,
  18361: 285911421633872,
  23572: 161653675452,
  25771: 54835686438796,
  27205: 465973344293743,
  27355: 6677773338282,
  29145: 35132947495613,
  29347: 4432846297811,
  30610: 436976179749428,
  34532: 75877836993,
  36688: 25733223473129,
  37136: 89262738573433,
  43160: 471683612376882,
  49295: 631475785729473,
  49500: 23536636324682,
  52314: 6783335445363,
  54788: 6999114298948,
  58232: 5332755368823,
  59518: 91276162632377,
  65139: 58477941957789,
  65866: 8997839194551,
  72117: 13253582337431,
  74309: 113983713335,
  78590: 3874751773999,
  79795: 71367633519595,
  85642: 7995129515948,
  85920: 8633721112942,
  87655: 58881255967391,
  88857: 35717521513867,
  91910: 543777925813944,
  96070: 9286872373713,
  97615: 74998398912742,
  102454: 2779279618836,
  102941: 31758319283921,
  103389: 66687873654216,
  108127: 53515827671,
  108902: 19198819269321,
  110383: 866121327363158},
 'scheduled_day_of_week': {1203: 3,
  1267: 2,
  3915: 0,
  6539: 4,
  7662: 4,
  7861: 4,
  7956: 1,
  9153: 4,
  9389: 4,
  9463: 0,
  10260: 3,
  11129: 2,
  14008: 0,
  18361: 0,
  23572: 1,
  25771: 0,
  27205: 4,
  27355: 2,
  29145: 0,
  29347: 0,
  30610: 2,
  34532: 2,
  36688: 1,
  37136: 1,
  43160: 0,
  49295: 1,
  49500: 0,
  52314: 2,
  54788: 2,
  58232: 2,
  59518: 1,
  65139: 2,
  65866: 2,
  72117: 1,
  74309: 3,
  78590: 2,
  79795: 0,
  85642: 2,
  85920: 1,
  87655: 1,
  88857: 2,
  91910: 4,
  96070: 4,
  97615: 4,
  102454: 1,
  102941: 1,
  103389: 0,
  108127: 3,
  108902: 2,
  110383: 0},
 'scheduled_day_of_week_label': {1203: 'Thursday',
  1267: 'Wednesday',
  3915: 'Monday',
  6539: 'Friday',
  7662: 'Friday',
  7861: 'Friday',
  7956: 'Tuesday',
  9153: 'Friday',
  9389: 'Friday',
  9463: 'Monday',
  10260: 'Thursday',
  11129: 'Wednesday',
  14008: 'Monday',
  18361: 'Monday',
  23572: 'Tuesday',
  25771: 'Monday',
  27205: 'Friday',
  27355: 'Wednesday',
  29145: 'Monday',
  29347: 'Monday',
  30610: 'Wednesday',
  34532: 'Wednesday',
  36688: 'Tuesday',
  37136: 'Tuesday',
  43160: 'Monday',
  49295: 'Tuesday',
  49500: 'Monday',
  52314: 'Wednesday',
  54788: 'Wednesday',
  58232: 'Wednesday',
  59518: 'Tuesday',
  65139: 'Wednesday',
  65866: 'Wednesday',
  72117: 'Tuesday',
  74309: 'Thursday',
  78590: 'Wednesday',
  79795: 'Monday',
  85642: 'Wednesday',
  85920: 'Tuesday',
  87655: 'Tuesday',
  88857: 'Wednesday',
  91910: 'Friday',
  96070: 'Friday',
  97615: 'Friday',
  102454: 'Tuesday',
  102941: 'Tuesday',
  103389: 'Monday',
  108127: 'Thursday',
  108902: 'Wednesday',
  110383: 'Monday'},
 'scheduled_hour': {1203: 13,
  1267: 14,
  3915: 8,
  6539: 6,
  7662: 11,
  7861: 13,
  7956: 9,
  9153: 7,
  9389: 13,
  9463: 14,
  10260: 14,
  11129: 14,
  14008: 13,
  18361: 16,
  23572: 8,
  25771: 9,
  27205: 7,
  27355: 14,
  29145: 7,
  29347: 15,
  30610: 9,
  34532: 8,
  36688: 13,
  37136: 9,
  43160: 10,
  49295: 15,
  49500: 9,
  52314: 9,
  54788: 7,
  58232: 9,
  59518: 14,
  65139: 8,
  65866: 13,
  72117: 7,
  74309: 17,
  78590: 10,
  79795: 15,
  85642: 14,
  85920: 8,
  87655: 14,
  88857: 11,
  91910: 11,
  96070: 10,
  97615: 8,
  102454: 7,
  102941: 15,
  103389: 11,
  108127: 15,
  108902: 7,
  110383: 15},
 'scheduled_hour_label': {1203: '13:00',
  1267: '14:00',
  3915: '8:00',
  6539: '6:00',
  7662: '11:00',
  7861: '13:00',
  7956: '9:00',
  9153: '7:00',
  9389: '13:00',
  9463: '14:00',
  10260: '14:00',
  11129: '14:00',
  14008: '13:00',
  18361: '16:00',
  23572: '8:00',
  25771: '9:00',
  27205: '7:00',
  27355: '14:00',
  29145: '7:00',
  29347: '15:00',
  30610: '9:00',
  34532: '8:00',
  36688: '13:00',
  37136: '9:00',
  43160: '10:00',
  49295: '15:00',
  49500: '9:00',
  52314: '9:00',
  54788: '7:00',
  58232: '9:00',
  59518: '14:00',
  65139: '8:00',
  65866: '13:00',
  72117: '7:00',
  74309: '17:00',
  78590: '10:00',
  79795: '15:00',
  85642: '14:00',
  85920: '8:00',
  87655: '14:00',
  88857: '11:00',
  91910: '11:00',
  96070: '10:00',
  97615: '8:00',
  102454: '7:00',
  102941: '15:00',
  103389: '11:00',
  108127: '15:00',
  108902: '7:00',
  110383: '15:00'},
 'scheduled_time': {1203: 13.977222222222224,
  1267: 14.031666666666668,
  3915: 8.4686111111111106,
  6539: 6.8394444444444433,
  7662: 11.852222222222224,
  7861: 13.731111111111113,
  7956: 9.0211111111111126,
  9153: 7.4741666666666671,
  9389: 13.826111111111109,
  9463: 14.524444444444445,
  10260: 14.928055555555556,
  11129: 14.712222222222223,
  14008: 13.131388888888885,
  18361: 16.719166666666666,
  23572: 8.1272222222222226,
  25771: 9.6974999999999998,
  27205: 7.2108333333333325,
  27355: 14.140277777777778,
  29145: 7.5116666666666676,
  29347: 15.408055555555556,
  30610: 9.3469444444444427,
  34532: 8.3727777777777774,
  36688: 13.409166666666668,
  37136: 9.125,
  43160: 10.283611111111108,
  49295: 15.8475,
  49500: 9.4530555555555544,
  52314: 9.4066666666666663,
  54788: 7.5438888888888886,
  58232: 9.0066666666666659,
  59518: 14.124722222222225,
  65139: 8.8613888888888876,
  65866: 13.014166666666664,
  72117: 7.2275,
  74309: 17.560833333333335,
  78590: 10.436388888888887,
  79795: 15.059444444444445,
  85642: 14.911388888888887,
  85920: 8.1488888888888891,
  87655: 14.225277777777777,
  88857: 11.164722222222224,
  91910: 11.2225,
  96070: 10.6075,
  97615: 8.4352777777777774,
  102454: 7.9572222222222218,
  102941: 15.321666666666667,
  103389: 11.191666666666665,
  108127: 15.130555555555556,
  108902: 7.0744444444444445,
  110383: 15.646111111111109}})

def get_no_show_bar_chart(bar_stacked_layers):
 return  {
    'title': 'No-Shows by Feature',
    'xlabel': 'Features',
    'ylabel': 'No-Shows',
    'figsize': (15,5),
    'layers': bar_stacked_layers,
    'domain_labels': ['Scholarship','Alcoholism', 'Diabetes','Hipertension','Handcap','Gender'],
    'bbox_to_anchor': (1.15, 1.00)
}
def deprecate_get_no_show_bar_chart(bar_stacked_layers):
 return  {
    'title': 'No-Shows by Feature',
    'xlabel': 'Features',
    'ylabel': 'No-Shows',
    'figsize': (15,5),
    'layers': bar_stacked_layers,
    'bar_labels': ['Scholarship','Alcoholism', 'Diabetes','Hipertension','Handcap','Gender'],
    'bbox_to_anchor': (1.15, 1.00)
}
def get_patient_groupings():
    return stru.Grouping(stru.Group('scholarship', ['Non-Scholar', 'Scholar'])) \
        .add(stru.Group('hipertension', ['Non-hipertensive', 'Hipertensive'])).toDict()
'''
def get_patient_groupings():
    return {'appointments': [],
            'no_shows': [],
            'scholarship': ['Non-Scholar', 'Scholar'],
            'hipertension': ['Non-hipertensive', 'Hipertensive'],
            'diabetes': ['Non-diabetic', 'Diabetic'],
            'alcoholism': ['Non-alcoholic', 'Alcoholic'],
            'handcap': ['Not', '1-HC', '2-HC', '3-HC', '4-HC'],
            'gender': ['Female', 'Male'],
            'age': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
            'skipper': ['Non-skipper', 'Skipper']}
'''
def main():
    df = get_appointment_dataframe()
    assert type(df).__name__ == 'DataFrame'

    df = get_patient_dataframe()
    assert type(df).__name__ == 'DataFrame'

    groupings = get_patient_groupings()
    print(groupings)


if __name__ == "__main__":
    # execute only if run as a script
    main()