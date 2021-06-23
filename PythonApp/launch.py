from flask import Flask
from flask import jsonify
helloworld = Flask(__name__)

data = {
  "users": [
    {
      "username": "bootcamp",
      "mail": "test2@test2.com"
    },
    {
      "username": "tbb2021",
      "mail": "test1@test1.com"
    },
    {
      "status": "DevOps Engineer",
      "source": "test@test.com"
    }
  ]
}

@helloworld.route("/data")
def run():
    return jsonify(data)
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)
