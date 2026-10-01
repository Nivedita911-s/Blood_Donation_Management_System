from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

DONOR_FILE = "donors.csv"
REQUEST_FILE = "blood_requests.csv"


def load_donors():
    if not os.path.exists(DONOR_FILE):
        columns = [
            "name",
            "age",
            "gender",
            "blood_group",
            "city",
            "phone",
            "available"
        ]
        return pd.DataFrame(columns=columns)

    return pd.read_csv(DONOR_FILE)


def load_requests():
    if not os.path.exists(REQUEST_FILE):
        columns = [
            "patient_name",
            "blood_group",
            "city",
            "units",
            "status"
        ]
        return pd.DataFrame(columns=columns)

    return pd.read_csv(REQUEST_FILE)


@app.route("/")
def home():
    donors = load_donors()
    requests_df = load_requests()

    total_donors = len(donors)
    available_donors = len(
        donors[donors["available"].astype(str).str.lower() == "yes"]
    )
    total_requests = len(requests_df)
    pending_requests = len(
        requests_df[
            requests_df["status"].astype(str).str.lower() == "pending"
        ]
    )

    return render_template(
        "index.html",
        total_donors=total_donors,
        available_donors=available_donors,
        total_requests=total_requests,
        pending_requests=pending_requests
    )


@app.route("/donors")
def donors():
    donors_df = load_donors()

    blood_group = request.args.get("blood_group", "")
    city = request.args.get("city", "")

    if blood_group:
        donors_df = donors_df[
            donors_df["blood_group"].astype(str).str.upper()
            == blood_group.upper()
        ]

    if city:
        donors_df = donors_df[
            donors_df["city"].astype(str).str.lower()
            == city.lower()
        ]

    donor_records = donors_df.to_dict(orient="records")

    return render_template(
        "donors.html",
        donors=donor_records
    )


@app.route("/add_donor", methods=["POST"])
def add_donor():

    donors_df = load_donors()

    new_donor = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gender": request.form["gender"],
        "blood_group": request.form["blood_group"],
        "city": request.form["city"],
        "phone": request.form["phone"],
        "available": request.form["available"]
    }

    donors_df = pd.concat(
        [donors_df, pd.DataFrame([new_donor])],
        ignore_index=True
    )

    donors_df.to_csv(DONOR_FILE, index=False)

    return redirect(url_for("donors"))


@app.route("/requests")
def blood_requests():

    requests_df = load_requests()

    request_records = requests_df.to_dict(orient="records")

    return render_template(
        "requests.html",
        requests=request_records
    )


@app.route("/add_request", methods=["POST"])
def add_request():

    requests_df = load_requests()

    new_request = {
        "patient_name": request.form["patient_name"],
        "blood_group": request.form["blood_group"],
        "city": request.form["city"],
        "units": request.form["units"],
        "status": request.form["status"]
    }

    requests_df = pd.concat(
        [requests_df, pd.DataFrame([new_request])],
        ignore_index=True
    )

    requests_df.to_csv(REQUEST_FILE, index=False)

    return redirect(url_for("blood_requests"))


@app.route("/analytics")
def analytics():

    donors_df = load_donors()
    requests_df = load_requests()

    blood_group_count = (
        donors_df["blood_group"]
        .value_counts()
        .to_dict()
    )

    city_count = (
        donors_df["city"]
        .value_counts()
        .to_dict()
    )

    available_count = (
        donors_df["available"]
        .value_counts()
        .to_dict()
    )

    request_status_count = (
        requests_df["status"]
        .value_counts()
        .to_dict()
    )

    return render_template(
        "analytics.html",
        blood_group_count=blood_group_count,
        city_count=city_count,
        available_count=available_count,
        request_status_count=request_status_count
    )


if __name__ == "__main__":
    app.run(debug=True)