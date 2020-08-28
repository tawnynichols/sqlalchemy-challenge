from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates for each prcp value"""
    # Query all passengers
    results = session.query(Measurement.date, Measurement.tobs).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitations
    all_precipitations = []
    for date, tobs in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["tobs"] = tobs
        all_precipitations.append(precipitation_dict)

    return jsonify(all_precipitations)


if __name__ == '__main__':
    app.run(debug=True)