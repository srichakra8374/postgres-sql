## Create a new end point
1. created a new end point.
2. created a new API in my flask application
   (app.py)                 
                   * End point /greeting
                   * Response : Welcome to flask 
@app.route('/greeting')

   def greeting():

   return "welcome to flask app"

2. created a new image myflaskapp and runned in container.

      eg :docker build -t myflaskapp .

          docker run -p 8000:8000 --name myflaskcontainer1 myflaskapp

RETURN :
  A Special statement that you can use inside a function or method to send the functions result back to the caller.

REDIRECT :
  Function or utillity in flask which allows developers to redirect users to a specified URL and assign a specified status code.

@app.route() : it is a python decorator that flask provides to assign URLs in our app to functions easily.
          eg :Flask's  "HELLO WORLD"
