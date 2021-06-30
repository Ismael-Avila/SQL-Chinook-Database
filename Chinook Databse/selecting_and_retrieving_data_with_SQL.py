import numpy as np
import pandas as pd
import sqlite3

"""
#=========================================================================#
#																	Main   											  					#
#=========================================================================#
"""

#Setting the connection between our code and the chinook database
pd.set_option("display.max_rows", None, "display.max_columns", None)
database = "./Chinook_Sqlite.sqlite"
conn = sqlite3.connect(database)



"""
Query 1: Retrieve all the records from the Employees table.
"""
query_1 =  pd.read_sql("""
					SELECT *
					FROM Employee
					""", conn)
#print(query_1)



"""
Query 2: Retrieve the FirstName, LastName, Birthdate, Address, City, and State
from the Employees table.
"""
query_2 = pd.read_sql(
					"""
					SELECT FirstName, LastName, BirthDate, Address, City, State
					FROM Employee
					""", conn)
#print(query_2)



"""
Query 3: Retrieve all the columns from the Tracks table, but only return 20 rows.
"""
query_3 = pd.read_sql(
					"""
					SELECT *
					FROM Track
					LIMIT 20
					""", conn)
#print(query_3)