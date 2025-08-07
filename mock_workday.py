from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/workday/employees", methods=["GET"])
def get_employees():
    return jsonify([
        {"id": "E001", "name": "Alice Johnson", "title": "Data Analyst", "start_date": "2022-01-15"},
        {"id": "E002", "name": "Bob Smith", "title": "Backend Engineer", "start_date": "2021-03-12"}
    ])

if __name__ == "__main__":
    app.run(port=5001)
