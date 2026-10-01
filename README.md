# 🩸 Online Blood Donation Management & Analytics System

## 📌 Project Overview

The **Online Blood Donation Management & Analytics System** is a Python-based web application developed to manage blood donor information and blood requests.

The project also includes a **Data Analytics component using Python and Pandas** to analyze donor data and identify useful patterns such as blood group distribution, city-wise donor distribution, donor availability, and blood request status.

The system provides simple web pages where users can view donors, search for donors, add new donor records, manage blood requests, and view analytical results.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To maintain blood donor information.
* To manage blood donation requests.
* To search donors based on blood group and city.
* To identify available blood donors.
* To analyze blood group distribution.
* To analyze city-wise donor distribution.
* To analyze donor availability.
* To analyze blood request status.
* To demonstrate Python web development and data analytics skills.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Web Development

* Flask
* HTML
* CSS

### Data Analytics

* Pandas
* Matplotlib
* Jupyter Notebook

### Data Storage

* CSV files

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## ⭐ Main Features

### 1. Home Dashboard

The home page displays important information such as:

* Total number of donors
* Available donors
* Total blood requests
* Pending blood requests

---

### 2. Donor Management

The system allows users to:

* View donor information
* Add new donors
* Search donors by blood group
* Search donors by city
* Check donor availability

Donor information includes:

* Name
* Age
* Gender
* Blood Group
* City
* Phone Number
* Availability

---

### 3. Blood Request Management

Users can add and view blood requests.

Each request contains:

* Patient Name
* Blood Group
* City
* Required Units
* Request Status

The request status can be:

* Pending
* Completed

---

### 4. Data Analytics

The project uses **Pandas** to analyze donor and blood request data.

The analysis includes:

#### Blood Group Distribution

```python
blood_group_count = donors["blood_group"].value_counts()
```

This identifies the number of donors belonging to each blood group.

#### City-wise Donor Analysis

```python
city_count = donors["city"].value_counts()
```

This identifies the number of registered donors in each city.

#### Donor Availability Analysis

```python
availability = donors["available"].value_counts()
```

This identifies how many donors are currently available and unavailable.

#### Blood Request Analysis

The project also analyzes the status of blood requests.

---

## 📊 Jupyter Notebook

The file:

```text
blood_donation_analysis.ipynb
```

contains the data analytics part of the project.

The notebook performs the following steps:

```text
Load Dataset
     ↓
Explore Dataset
     ↓
Clean Data
     ↓
Analyze Donor Data
     ↓
Analyze Blood Groups
     ↓
Analyze Cities
     ↓
Analyze Availability
     ↓
Create Charts
     ↓
Generate Insights
```

---

## 📁 Project Structure

```text
Blood_Donation_Management_System
│
├── app.py
│
├── donors.csv
│
├── blood_requests.csv
│
├── blood_donation_analysis.ipynb
│
├── README.md
│
├── templates
│   ├── index.html
│   ├── donors.html
│   ├── requests.html
│   └── analytics.html
│
└── static
    └── style.css
```

---

# 🚀 How to Run the Project

## Step 1: Download the Project

Clone the GitHub repository or download the ZIP file.

Using Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project folder:

```bash
cd Blood_Donation_Management_System
```

---

## Step 2: Install Python

Make sure Python is installed on your computer.

Check Python:

```bash
python --version
```

Example:

```text
Python 3.x.x
```

---

## Step 3: Install Required Libraries

Open Command Prompt or Terminal inside the project folder.

Run:

```bash
pip install flask pandas matplotlib jupyter
```

---

## Step 4: Run the Flask Application

Run:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

---

## Step 5: Open the Website

Open your browser.

Enter:

```text
http://127.0.0.1:5000
```

The Blood Donation Management System will open.

---

# 🌐 Web Application Pages

## 🏠 Home

URL:

```text
http://127.0.0.1:5000/
```

The home page displays the project dashboard.

---

## 👥 Donors

URL:

```text
http://127.0.0.1:5000/donors
```

From this page you can:

* View donors
* Search donors
* Add new donors

---

## 🩸 Blood Requests

URL:

```text
http://127.0.0.1:5000/requests
```

From this page you can:

* View blood requests
* Add new blood requests
* Check request status

---

## 📊 Analytics

URL:

```text
http://127.0.0.1:5000/analytics
```

This page displays:

* Blood group analysis
* City-wise donor analysis
* Donor availability
* Blood request status

---

# 📓 How to Open the Jupyter Notebook

Open Command Prompt inside the project folder.

Run:

```bash
jupyter notebook
```

A browser window will open.

Find:

```text
blood_donation_analysis.ipynb
```

Click the file to open it.

---

# 📈 How to Run the Jupyter Notebook

Inside Jupyter Notebook:

1. Open `blood_donation_analysis.ipynb`.
2. Run the first cell.
3. Run each cell from top to bottom.
4. Check the output after each cell.
5. View the tables and charts generated by the analysis.

The notebook reads:

```text
donors.csv
```

and performs data analysis using Pandas.

---

# 🔍 Sample Analytics

### Total Donors

```python
print("Total Donors:", len(donors))
```

### Blood Group Analysis

```python
blood_group_count = donors["blood_group"].value_counts()

print(blood_group_count)
```

### City Analysis

```python
city_count = donors["city"].value_counts()

print(city_count)
```

### Availability Analysis

```python
availability = donors["available"].value_counts()

print(availability)
```

---

# 💡 Example Insights

After analyzing the dataset, the system can provide insights such as:

* Which blood group has the highest number of donors.
* Which cities have more registered donors.
* How many donors are currently available.
* How many blood requests are pending.
* How many blood requests have been completed.

These insights can help demonstrate how Python and Pandas can be used to analyze real-world data.

---

# 🧪 Testing

The application was tested for:

* Adding donor records
* Searching donors
* Adding blood requests
* Viewing donor information
* Viewing blood request information
* Loading CSV datasets
* Performing Pandas analysis
* Running the Flask application
* Running the Jupyter Notebook

---

# 📌 Example Workflow

```text
User
  ↓
Open Website
  ↓
Home Dashboard
  ↓
View / Add Donor
  ↓
Search Donor
  ↓
Create Blood Request
  ↓
View Request
  ↓
Open Analytics
  ↓
Analyze Donor Data
```

---

# 🔐 Data Note

This project is created for **educational and portfolio purposes**.

The sample dataset contains fictional/demo information and should not be used as real medical or personal data.

For a production system, appropriate authentication, authorization, database security, privacy controls, and secure handling of personal information would be required.

---

# 🚀 Future Enhancements

The project can be further improved by adding:

* MySQL database
* User authentication
* Admin dashboard
* Donor login
* Email notifications
* SMS notifications
* Real-time blood availability
* Google Maps integration
* Advanced charts
* Power BI dashboard
* REST API
* Database-based search
* Deployment to a cloud platform

---

# 👩‍💻 Skills Demonstrated

This project demonstrates:

* Python programming
* Flask web development
* Pandas
* Data cleaning
* Data analysis
* Data visualization
* CSV data handling
* HTML
* CSS
* Jupyter Notebook
* Git
* GitHub
* Problem solving

---

# 📚 Learning Outcomes

Through this project, I learned how to:

* Build a basic Python web application.
* Work with CSV datasets.
* Read and process data using Pandas.
* Perform basic exploratory data analysis.
* Analyze categorical data.
* Create data visualizations.
* Connect Python logic with HTML pages.
* Organize a software project.
* Use Git and GitHub to manage and present a project.

---

# 👤 Author

**Nivedita Sharanappa**

B.E. Computer Science Engineering

Interested in:

* Python Development
* Data Analytics
* Software Development

---

# ⭐ Project Summary

The **Online Blood Donation Management & Analytics System** combines a Python Flask web application with Pandas-based data analysis.

It demonstrates how donor information and blood requests can be managed through a web interface while also extracting useful insights from the collected data.

---

## ⭐ If you find this project useful

Feel free to explore the project, study the code, and improve it with additional features.
