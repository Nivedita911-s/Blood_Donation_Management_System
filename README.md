\# Blood Donation Management System



\## Project Overview



The Blood Donation Management System is a web-based project developed using Python, Pandas, HTML, and CSS. It helps store and manage blood donor and blood request information.



The project also performs basic data analysis on donor information to understand blood group availability and donor distribution by city.



\## Technologies Used



\* Python

\* Pandas

\* Jupyter Notebook

\* HTML

\* CSS

\* CSV

\* Flask



\## Features



\* Register and store blood donor information

\* Store blood request information

\* View donor details

\* Analyze donor data using Pandas

\* Count donors according to blood group

\* Analyze donors according to city

\* Display basic project information through web pages



\## Data Analysis



The project uses Pandas to analyze the donor data.



Examples of analysis:



\* Total number of registered donors

\* Number of donors in each blood group

\* Number of donors from each city



Example:



```python

blood\_group\_count = donors\["blood\_group"].value\_counts()

print(blood\_group\_count)

```



This helps identify how many registered donors belong to each blood group.



\## Project Structure



```text

Blood\_Donation\_Management\_System

│

├── app.py

├── blood\_donation\_analysis.ipynb

├── donors.csv

├── blood\_requests.csv

├── README.md

│

├── templates

│   ├── index.html

│   ├── donors.html

│   └── requests.html

│

└── static

&#x20;   └── style.css

```



\## How to Run the Project



1\. Install Python.

2\. Install the required libraries:



```bash

pip install pandas flask

```



3\. Open the project folder.

4\. Run the Flask application:



```bash

python app.py

```



5\. Open the URL displayed in the terminal in a web browser.



\## Data Analysis



The Jupyter Notebook `blood\_donation\_analysis.ipynb` contains the Python/Pandas data analysis.



The analysis includes:



\* Loading donor data

\* Finding the total number of donors

\* Blood group distribution

\* City-wise donor distribution



\## Future Enhancements



\* Add a database such as MySQL

\* Add user login and authentication

\* Add search and filter functionality

\* Add email/SMS notifications

\* Add dashboards and visualizations

\* Add real-time blood availability



\## Author



Nivedita



