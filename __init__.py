from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/projects")
def get_projects():
    return jsonify(["test"])

def main():
    app.run(host="0.0.0.0", port="4000")

if __name__ == "__main__":
    main()