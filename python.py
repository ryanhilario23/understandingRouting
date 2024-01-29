from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def nice():
    return'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    print(name)
    return f'Hello {name}'

@app.route('/repeat/<int:nums>/<string:name>')
def repeat(nums,name):
    message = f"{name}\n" * nums
    return message 

if __name__ == "__main__":
    app.run(debug=True)