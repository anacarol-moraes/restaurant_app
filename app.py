from flask import Flask, render_template
from routes.reception_routes import reception_blueprint
app = Flask (__name__)
app.register_blueprint(reception_blueprint)

@app.route("/reception")
def recception():
    tables = [
        {"id": 1, "status": "available"},
        {"id": 2, "status": "occupied"},
        {"id": 3, "status": "reserved"},
    ]
    return render_template("reception.html", tables = tables)
if __name__ == "__main__":
    app.run(debug=True)
