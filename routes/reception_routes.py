from flask import Blueprint, render_template
reception_blueprint = Blueprint("recepption", __name__)
@reception_blueprint.route("/reception")
def show_tables():
    tables = [
        {"id": 1, "status": "available"},
        {"id": 2, "status": "occupied"},
        {"id": 3, "status": "reserved"},
    ]
    
    return render_template("reception.html", tables=tables)