# REST APIs
#Request Method:
    # GET           Endpoint: www.godev.today/api/v1/testApi, It returns message 'Simple API Test: This App is working'
    # GET           Endpoint: www.godev.today/api/v1/student, It returns list of all the students (JSON)
    # POST
    # PATCH
    # DELETE

# localhost = 127.0.0.1
# Port number: 8000

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def testApp():
    return jsonify({'message':'Simple API Test: This App is working'})

if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0)