# Online Blood Donation Management & Analytics System

## Project Overview

The **Online Blood Donation Management & Analytics System** is a Python-based web application designed to manage blood donor information and blood requests. It also provides basic data analytics to understand blood group distribution, city-wise donor counts, donor availability, and blood request status.

The project combines Python web development with data analysis to demonstrate how technology can help organize blood donation information.

## Objectives

* Store and manage blood donor information.
* Search donors by blood group and city.
* Add and view blood requests.
* Analyze donor data using Pandas.
* Display donor and request summaries through web pages.
* Explore data and create charts using Jupyter Notebook.

## Technologies Used

* **Python** — Main programming language
* **Flask** — Web application framework
* **Pandas** — Data handling and analysis
* **Jupyter Notebook** — Exploratory data analysis
* **Matplotlib** — Data visualization
* **HTML** — Webpage structure
* **CSS** — Webpage styling
* **CSV** — Data storage

## Project Structure

```text
Blood_Donation_Management_System-main/
│
├── app.py
├── donors.csv
├── blood_requests.csv
├── blood_donation_analysis.ipynb
│
├── templates/
│   ├── index.html
│   ├── donors.html
│   ├── requests.html
│   └── analytics.html
│
└── static/
    └── style.css
```

## Features

1. **Home Dashboard** — Displays total donors, available donors, total requests, and pending requests.
2. **Donor Management** — Displays donor details, supports searching by blood group and city, and allows new donors to be added.
3. **Blood Request Management** — Allows users to add and view blood requests.
4. **Analytics Dashboard** — Displays blood-group distribution, city-wise donor distribution, donor availability, and request status.
5. **Data Analysis** — Uses Pandas in Jupyter Notebook to analyze donor records and Matplotlib to create charts.

## How to Run on Windows

### Step 1: Open Command Prompt

Press **Windows + R**, type:

```text
cmd
```

Press **Enter**.

### Step 2: Check the Downloads Folder

Type the following command:

```bat
dir C:\Users\dell\Downloads
```

Press Enter and check that the `Blood_Donation_Management_System-main` folder is present.

### Step 3: Open the Project Folder

Type:

```bat
cd /d "C:\Users\dell\Downloads\Blood_Donation_Management_System-main"
```

Press Enter.

**Note:** If your project folder is saved in a different location, replace this path with your actual folder path.

### Step 4: Check the Project Files

Type:

```bat
dir
```

Press Enter. You should see `app.py`, `donors.csv`, `blood_requests.csv`, and the other project files or folders.

### Step 5: Install the Required Libraries

Run:

```bat
py -m pip install flask pandas matplotlib jupyter
```

You only need to install the packages once in the Python environment you use. If they are already installed, you can continue.

### Step 6: Run the Flask Application

Type:

```bat
py app.py
```

Press Enter.

Wait for Flask to display a message similar to:

```text
* Running on http://127.0.0.1:5000
```

Keep Command Prompt open while using the website.

### Step 7: Open the Website

Open Chrome, Microsoft Edge, or another web browser and visit:

**http://127.0.0.1:5000**

The Blood Donation Management System home page should open.

## Website Pages

| Page           | URL                               | Purpose                      |
| -------------- | --------------------------------- | ---------------------------- |
| Home           | `http://127.0.0.1:5000/`          | View dashboard summaries     |
| Donors         | `http://127.0.0.1:5000/donors`    | Search and add donors        |
| Blood Requests | `http://127.0.0.1:5000/requests`  | View and add requests        |
| Analytics      | `http://127.0.0.1:5000/analytics` | View data analysis summaries |

## How to Run the Jupyter Notebook

Open a **second Command Prompt** and navigate to the project folder using the same `cd /d` command.

Run:

```bat
py -m jupyter notebook
```

Open `blood_donation_analysis.ipynb` in the Jupyter interface and execute the notebook cells from top to bottom.

The notebook can be used to explore the CSV datasets, calculate blood-group and city-wise counts, and generate charts using Pandas and Matplotlib.

## How the Project Works

1. Donor and blood request records are stored in CSV files.
2. Flask handles webpage requests and form submissions.
3. Pandas reads, filters, updates, and summarizes the records.
4. HTML and CSS provide the user interface.
5. The Analytics page displays summaries calculated from the stored data.
6. Jupyter Notebook is used separately for exploratory analysis and charts.

## Future Enhancements

* Integrate a MySQL database.
* Add user authentication and authorization.
* Improve data validation and security.
* Add interactive analytics charts.
* Deploy the application online.
* Add verified donor availability and request-management workflows.

## Important Note

This is an educational portfolio project using sample data. It is not a production-ready blood bank system. Donor availability is based on the stored records and is not verified in real time. The application does not determine medical eligibility or blood compatibility.

## Author

**Nivedita Sharanappa**

GitHub: [Nivedita911-s](https://github.com/Nivedita911-s)
