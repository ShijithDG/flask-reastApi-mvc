# from flask import Flask, jsonify, request 

# def create_app():
#     app = Flask(__name__)
#     # Load configuration, register blueprints, etc.
#     return app

# app = create_app()


# @app.route('/', methods = ['GET', 'POST']) 
# def home(): 
#     if(request.method == 'GET'): 
  
#         data = "hello world"
#         return jsonify({'data': data}) 

# if __name__ == "__main__":
#     app.run(debug=True)

# run.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

