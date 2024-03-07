## Postgresql - Migrateing flask app to Postgres RDS instance.
1. Created a RDS Instance in AWS .
2. Connected to RDS Instance from my dbeaver.
   Connection details 

        1. URL: dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com

        2. UserName: flaskdevl
        3. Password: flaskdevl01
        4. DB: achievers
3. Made code changes to my flask application.
        1. Dependencies (module)
           installed psycopg2 i got error then installed psycopg2-binary.
            * psycopg2-binary (install)
            * psycopg2.connect
            * cur = conn.cursor()
            * conn.commit()
        


  
