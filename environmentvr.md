## ENVIROMENT VARIABLES
1. Made changes in the code in (app.py)file.

     conn = psycopg2.connect(database="achievers",
user = os.environ.get('DB_USER'),
password =os.environ.get('DB_USER_PWD'),
host =os.environ.get("DB_HOST"),
port="5432").
3. exported changes
         export DB_USER=flaskdevl
         export DB_USER_PWD=flaskdevl01
         export DB_HOST=dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com
         
2. Runned app.py file by using command
     python3 app.py
3. Made changes in dockerfile to run env variables in dockercontainer.
      
 ENV DB_USER=flaskdevl

ENV DB_USER_PWD=flaskdevl01

ENV DB_HOST=dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com
4. Build  image 

     docker build -t myflaskimageenv .
5. Runned image in container 
  docker run -p 8000:8000 --name myflaskcontainerenv myflaskimageenv
