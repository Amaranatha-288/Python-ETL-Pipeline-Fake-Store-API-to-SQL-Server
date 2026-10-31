# Python-ETL-Pipeline-Fake-Store-API-to-SQL-Server


## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline developed using Python and Microsoft SQL Server.

The pipeline extracts product and user data from the Fake Store API, transforms the raw JSON data using Pandas, and loads the processed datasets into Microsoft SQL Server.

The project follows a modular approach by separating extraction, transformation, loading, and pipeline execution into different Python modules.

## 🏗️ Architecture

**ETL Workflow:**

Fake Store API → Extract → Transform → Load → Microsoft SQL Server

- **Source:** Fake Store API
- **Processing:** Python and Pandas
- **Destination:** Microsoft SQL Server

## 🛠️ Technologies Used

- Python
- Pandas
- Requests
- REST API
- SQLAlchemy
- PyODBC
- Microsoft SQL Server
- Git & GitHub

## 📂 Project Structure

```text
Python-ETL-Pipeline/
│
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

## 🔄 ETL Process

### 1. Extract

- Connected to the Fake Store API using Python Requests.
- Extracted product and user information.
- Converted API JSON responses into Pandas DataFrames.
- Implemented HTTP error handling using `raise_for_status()`.

**API Endpoints:**
- Products: `https://fakestoreapi.com/products`
- Users: `https://fakestoreapi.com/users`

### 2. Transform

Used Pandas to clean and structure the extracted datasets.

**Product Transformation:**
- Renamed columns into meaningful names.
- Selected required product attributes.
- Converted product prices into float data types.

**User Transformation:**
- Extracted nested JSON fields such as first name and last name.
- Extracted address information including street, city, and zipcode.
- Renamed columns for better readability.
- Selected the required user attributes.

### 3. Load

- Established a connection to Microsoft SQL Server using SQLAlchemy and PyODBC.
- Loaded the transformed DataFrames into SQL Server.
- Created separate tables for products and users.
- Used Pandas `to_sql()` to insert the processed datasets.

**Database:** `fake_store_db`

**Tables:**
- `products`
- `users`

### 4. Pipeline Execution

The main Python script coordinates all ETL stages:

1. Extract product and user data.
2. Transform both datasets.
3. Load the processed datasets into SQL Server.
4. Complete the ETL pipeline.

## 📊 Database Output

The pipeline loads two structured tables into Microsoft SQL Server.

| Table | Description |
|---|---|
| products | Product information including name, price, category, and description |
| users | User information including email, username, name, and address |

## ⚙️ Installation & Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure SQL Server

Update the SQL Server connection details in `load.py` according to your local SQL Server configuration.

Create the database:

```sql
CREATE DATABASE fake_store_db;
```

### Step 4: Run the Pipeline

```bash
python main.py
```

## 🎯 Key Learnings

- Understanding the ETL architecture.
- Extracting data from REST APIs.
- Working with JSON and nested JSON structures.
- Transforming datasets using Pandas.
- Integrating Python with Microsoft SQL Server.
- Using SQLAlchemy and PyODBC for database connectivity.
- Developing modular and reusable Python scripts.

## 👨‍💻 Author

**Amaranatha H**

Aspiring Data Professional | Interested in Data Engineering and Analytics

**Learning → Practicing → Building → Improving 🚀**
