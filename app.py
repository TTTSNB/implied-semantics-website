from flask import Flask

# create a flask application
app = Flask(__name__)

# Register a route to the application
@app.route("/")  #"@" is a python decorator

# Define functions to run within the app
def helloworld():
  return "Hello world!"

# Check to see if we are running the app.py file as a script.
if __name__ == "__main__":
  print("I'm inside the if now")
  app.run(host='0.0.0.0', debug=True)
  