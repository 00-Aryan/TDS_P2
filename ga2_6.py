from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# # Define the path to the JSON file
# json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')

# print(json_file_path)
# # Load student marks from the JSON file
# def load_student_marks():
#     try:
#         with open(json_file_path, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return [{"name": "Default", "marks": 0}] 

STUDENT_DATA = [{"name":"lQ","marks":83},{"name":"gJD5oDPSfz","marks":32},{"name":"T0K","marks":11},{"name":"yYR","marks":47},{"name":"4Ell","marks":60},{"name":"eaxCBh","marks":80},{"name":"OEh5w","marks":79},{"name":"WdZqDWh","marks":93},{"name":"2","marks":44},{"name":"VX8aL8","marks":32},{"name":"0n2C3","marks":92},{"name":"C8bGS1tGh","marks":88},{"name":"2JeG","marks":73},{"name":"U4","marks":34},{"name":"NNu4","marks":2},{"name":"3wFomCQ","marks":96},{"name":"FBE12amm","marks":44},{"name":"za","marks":81},{"name":"VwY8","marks":62},{"name":"JMdeEBH","marks":70},{"name":"d1","marks":11},{"name":"4BT","marks":48},{"name":"8AyUC","marks":73},{"name":"jzRraSFnRW","marks":7},{"name":"Gw7ErH","marks":48},{"name":"W5GiSdoPL8","marks":4},{"name":"YIrwLQrWnT","marks":68},{"name":"KbAXynKEx","marks":38},{"name":"GwSPpEoaL","marks":51},{"name":"00N0","marks":87},{"name":"wPNOP","marks":1},{"name":"24","marks":32},{"name":"P","marks":71},{"name":"7K0wBoW","marks":93},{"name":"r5cDdU7","marks":79},{"name":"PmV","marks":27},{"name":"IIbV","marks":41},{"name":"GNmUCL","marks":64},{"name":"DvSrB8sLK3","marks":28},{"name":"ADQNMdYPh","marks":58},{"name":"S6oMnhjHZY","marks":73},{"name":"Z3N4mZ61","marks":17},{"name":"MIzTwv","marks":99},{"name":"J","marks":91},{"name":"oVgO0h0Y1","marks":35},{"name":"peD8THc","marks":50},{"name":"j2hdH3bfDa","marks":55},{"name":"rK2","marks":99},{"name":"Atm711MbN","marks":35},{"name":"VyWCD","marks":84},{"name":"uHD0","marks":98},{"name":"3vYTto","marks":17},{"name":"m","marks":73},{"name":"iDTanKNEVN","marks":88},{"name":"6J2QNog","marks":54},{"name":"0MT32MS7","marks":22},{"name":"0IZ","marks":61},{"name":"bHZPF","marks":39},{"name":"5ql","marks":1},{"name":"yJ93PW","marks":27},{"name":"C62","marks":74},{"name":"qjL","marks":0},{"name":"MMwjKN7","marks":75},{"name":"u99O84","marks":82},{"name":"G2uch","marks":72},{"name":"xqS","marks":74},{"name":"wuearG","marks":93},{"name":"wuoMPZ","marks":62},{"name":"nzZOG2","marks":84},{"name":"e","marks":4},{"name":"jkIKVJj2V","marks":37},{"name":"mYm","marks":27},{"name":"UyfpA3Ws","marks":98},{"name":"Uok","marks":63},{"name":"6l","marks":50},{"name":"z1g3","marks":41},{"name":"66I","marks":51},{"name":"4D9","marks":40},{"name":"3TWfOZ7q","marks":84},{"name":"SGYk","marks":15},{"name":"7Y4U","marks":63},{"name":"CpN4B0x","marks":37},{"name":"UQAw0ich","marks":81},{"name":"eID8h","marks":49},{"name":"QoyAT8rVB0","marks":80},{"name":"D","marks":80},{"name":"17Ckwj","marks":91},{"name":"hxK","marks":58},{"name":"MSGVAP","marks":74},{"name":"B","marks":62},{"name":"fgs4hT","marks":57},{"name":"OOu6Hzc7Y","marks":47},{"name":"qiY","marks":68},{"name":"gV","marks":34},{"name":"beeSzvsoQ","marks":87},{"name":"0","marks":93},{"name":"yRJ","marks":84},{"name":"Q","marks":57},{"name":"hbc0","marks":56},{"name":"8","marks":21}]
def load_student_marks():
    return STUDENT_DATA
@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from the query string
    names = request.args.getlist('name')
    student_marks = load_student_marks()

    # Look for the student marks in the list of dictionaries
    marks = []
    for name in names:
        # Search for the student's mark based on the name
        student = next((item for item in student_marks if item["name"] == name), None)
        
        if student:
            marks.append(student["marks"])
        else:
            marks.append(0)

    return jsonify({"marks": marks})

# if __name__ == '__main__':
#     app.run(debug=True)