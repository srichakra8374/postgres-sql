## BUILD DOCKER IMAGE WITH POSTGRES
1. checked wheather doker is logedin.
2. Build image by using syntax
   ````commandline
   docker build -t my-flask-image .
   
* Showed error that my librarys are missing
* Rectified by changing missing librarys  (psycopg2-binary)
in dockerfile .
3. Runned container by using syntax
   ```commandline
   docker run -p 8000:8000 --name my-flask-container my-flask-container
    ```
