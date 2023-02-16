import numpy as np
import pandas as pd
import cx_Oracle
import json
import os

cx_Oracle.init_oracle_client(lib_dir="C:\Program Files\instantclient_21_9") # Initialize the client

import warnings
warnings.simplefilter("ignore")

connection =cx_Oracle.connect(user='websem', password='websem108', dsn='tirpitz.ms.mff.cuni.cz:1511/jedenact.ms.mff.cuni.cz')
ratings=pd.read_sql_query('''select * from FRATINGS where MOVIEID<20''', connection)
print(ratings)