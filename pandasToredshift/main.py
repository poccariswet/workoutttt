import pandas_redshift as pr
import pandas as pd
import os

"""
 Column   |          Type          | Collation | Nullable | Default
-----------+------------------------+-----------+----------+---------
 date_ymdh | character varying(256) |           |          |
 ten_cd    | character varying(256) |           |          |
 sku_cd    | character varying(256) |           |          |
 dpt_cd    | character varying(256) |           |          |
 line_cd   | character varying(256) |           |          |
 class_cd  | character varying(256) |           |          |
 sku_name  | character varying(256) |           |          |
 urisu     | numeric(10,2)          |           |          |
 urikin    | numeric(10,2)          |           |          |
 gsagsu1   | numeric(10,2)          |           |          |
 gsaggk1   | numeric(10,2)          |           |          |
 gsagsu2   | numeric(10,2)          |           |          |
 gsaggk2   | numeric(10,2)          |           |          |
 gsagsu3   | numeric(10,2)          |           |          |
 gsaggk3   | numeric(10,2)          |           |          |
 garari    | numeric(10,2)          |           |          |
"""

pr.connect_to_redshift(dbname =os.getenv('REDSHIFT_DB'),
                       host = os.getenv('REDSHIFT_HOST'),
                       port = os.getenv('REDSHIFT_PORT'),
                       user = os.getenv('REDSHIFT_USER'),
                       password = os.getenv('REDSHIFT_PASS')
                       )

pr.connect_to_s3(aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
                bucket = 'jisseki-nichiji'
                )


data  = {"date_ymdh": ["2018063012"],
         "ten_cd": ["0001"]
         }
f = pd.DataFrame(data)

pr.pandas_to_redshift(f, 'jisseki_nichiji')

