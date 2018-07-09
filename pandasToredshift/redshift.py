from sqlalchemy import create_engine
import pandas as pd
import os


dbname = os.getenv('REDSHIFT_DB')
host = os.getenv('REDSHIFT_HOST')
port = os.getenv('REDSHIFT_PORT')
user = os.getenv('REDSHIFT_USER')
password = os.getenv('REDSHIFT_PASS')
conn = create_engine('postgresql://'+user + ':' + password +'@'+ host + ':' + port + '/' + dbname)

df = pd.DataFrame({"date_ymdh": ["2018063012"],
                   "ten_cd": ["0001"],
                   ""
                 })

df.to_sql('jisseki_nichiji', conn, index = False, if_exists = 'append')
