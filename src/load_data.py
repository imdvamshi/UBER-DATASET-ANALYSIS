import sqlite3 as sql
import pandas as pd

def load_tables():
    conn = sql.connect('../Data/rideshare.db')
    tables = {
    'users' : pd.read_sql_query("SELECT * FROM users",conn),
    'drivers' : pd.read_sql_query("SELECT * FROM drivers",conn),
    'riders' : pd.read_sql_query("SELECT * FROM riders",conn),
    'locations' : pd.read_sql_query("SELECT * FROM locations",conn),
    'trips' : pd.read_sql_query("SELECT * FROM trips",conn),
    'payments' : pd.read_sql_query("SELECT * FROM payments",conn),
    'reviews' : pd.read_sql_query("SELECT * FROM  reviews",conn),
    'cancellations' : pd.read_sql_query("SELECT * FROM cancellations",conn)
    }
    return tables
