from flask import Flask
import os 

print("Welcome to my docker image")
print("Current working directory is",os.getcwd())

app=Flask(__name__)

@app.route('/')

def Hello_world():
    return "Hello_World, this is our docker demo!"

if __name__ =="__main__":
    app.run(debug=True,host='0.0.0.0')

    

    


