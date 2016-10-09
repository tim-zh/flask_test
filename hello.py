from flask import Flask, redirect

app = Flask(__name__, static_url_path = "")

@app.route("/api/name/<n>")
def name(n):
  return n + "'s World!"

@app.route('/')
def index():
    return redirect("/index.html")

@app.route('/<path:path>')
def serve_static(path):
  return send_from_directory('static', path)

if __name__ == "__main__":
  app.run(port = 8080)
