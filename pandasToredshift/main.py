import pandas_redshift as pr

pr.connect_to_redshift(os.getenv('REDSHIFT_DB'),
                       os.getenv('REDSHIFT_HOST'),
                       os.getenv('REDSHIFT_PORT'),
                       os.getenv('REDSHIFT_USER'),
                       os.getenv('REDSHIFT_PASS')
                       )
