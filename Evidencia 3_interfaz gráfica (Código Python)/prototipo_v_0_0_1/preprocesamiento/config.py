"""
Created on Mon Dec  9 19:43:57 2019
@author: Carlos Padierna
"""
dts  = ['breast', 'chronic', 'column_2C', 'cryotherapy', 'diabetes',
        'fertility', 'haberman', 'heart', 'immunotherapy', 'liver',
        'mammo', 'parkinsons', 'thoracic', 'transfusion', 'wpbc']
cfgs = ['all','best','classic','rest']
algs = ['GP','GPBUMDA','GPEDA'] # ['GP','GPBUMDA','GPEDA']    
path = 'C:/Users/TUF-PC8/Google Drive/2018.12 work/1 - HEEKS/Final Results/'
user = 'C:/Users/TUF-PC8/'
#user     = 'C:/Users/Carlos Villaseñor/'
#user     = 'C:/Users/Carlos/'
#user     = '/home/carlos/google-drive/'
#datapath = user+'Google Drive/2018.12 work/datasets/csv/'
#datapath = user+'2018.12 work/datasets/csv/'
datapath = user+'Google Drive/2018.12 work/1 - HEEKS/Final Results/'
#diresult = user+'Google Drive/2018.12 work/1 - HEEKS/DeleteMee/sin_rep/'
diresult = datapath+'/breast/all breast/s_rep/'
#diresult = user+'2018.12 work/1 - HEEKS/DeleteMeb/'

# PARÁMETROS ÓPTIMOS (Artículo Gegenbauer)    
# ** pendiente ** Cargar tablas de parámetros en Dataframes
dicRBF = {"a1a":       {"C": 11.83, "gamma":  0.18, "degree":0},
          "breast":    {"C": 19.34, "gamma":  0.03, "degree":0},
          "fourclass": {"C": 30.42, "gamma":  3.82, "degree":0},
          "ionosphere":{"C": 18.30, "gamma":  0.05, "degree":0},
          "monks-1":   {"C": 16.86, "gamma":  0.08, "degree":0}}

dicsHerm ={"a1a":      {"C": 00.00, "gamma": 'auto', "degree":0},
          "breast":    {"C": 07.44, "gamma": 'auto', "degree":4},
          "fourclass": {"C": 25.20, "gamma": 'auto', "degree":6},
          "diabetes":  {"C": 3.05, "gamma":  'auto', "degree":4},
          "immunotherapy":  {"C": 32, "gamma":  'auto', "degree":4},
          "cryotherapy":  {"C": 32, "gamma":  'auto', "degree":4},
          "fertility":  {"C": 24.57813, "gamma":  'auto', "degree":3},
          "ionosphere":{"C": 00.00, "gamma": 'auto', "degree":0},
          "monks-1":   {"C": 20.61, "gamma": 'auto', "degree":2}}

dicLinear={"a1a":      {"C": 12.85, "gamma":  'auto', "degree":0},
          "breast":    {"C": 00.28, "gamma":  'auto', "degree":0},
          "fourclass": {"C": 00.75, "gamma":  'auto', "degree":0},
          "diabetes":  {"C": 3.05, "gamma":  'auto', "degree":1},
          "ionosphere":{"C": 00.62, "gamma":  'auto', "degree":0},
          "mammo":{"C": 31.9550768315323, "gamma":  'auto', "degree":0},
          "monks-1":   {"C": 0.003, "gamma":  'auto', "degree":0}}

dicsGegen ={"a1a":     {"C": 00.00, "gamma": 'auto', "degree":0, "alpha":0.1},
          "breast":    {"C": 07.44, "gamma": 'auto', "degree":4, "alpha":0.1},
          "fourclass": {"C": 31.52, "gamma": 'auto', "degree":6, "alpha":-0.42},
          "diabetes":  {"C": 3.05, "gamma":  'auto', "degree":4, "alpha":0.1},
          "immunotherapy":  {"C": 32, "gamma":  'auto', "degree":4, "alpha":0.1},
          "cryotherapy":  {"C": 16.83121, "gamma":  'auto', "degree":3, "alpha":-0.02765},
          "fertility": {"C": 24.57813, "gamma":  'auto', "degree":3, "alpha":0.1},
          "ionosphere":{"C": 00.00, "gamma": 'auto', "degree":0, "alpha":0.1},
          "monks-1":   {"C": 20.61, "gamma": 'auto', "degree":2, "alpha":0.1}}

#return {'accs':accs, 'psvs':psvs, 'times':times, 'cs':cs,'intrs':intrs,'ns':ns}    