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
Query 1: Find all the tracks that have a length of 5,000,000 milliseconds or
more.
"""
query_1 = pd.read_sql(
					"""
					SELECT *
					FROM Track
					WHERE Milliseconds >= 5000000
					""", conn)
#print(query_1)



"""
Query 2: Find all the invoices whose total is between $5 and $15 dollars.
"""
query_2 =pd.read_sql(
					"""
					SELECT *
					FROM Invoice
					WHERE Total BETWEEN 5 AND 15
					""", conn)
#print(query_2)



"""
Query 3: Find all the customers from the following States: RJ, DF, AB, BC, CA, WA, NY.
"""
query_3 =pd.read_sql(
					"""
					SELECT *
					FROM Customer
					WHERE State IN ('RJ', 'DF', 'AB', 'BC', 'CA', 'WA', 'NY');
					""", conn)
#print(query_3)



"""
Query 4: Find all the invoices for customer 56 and 58 where the total was
between $1.00 and $5.00.
"""
query_4 =pd.read_sql(
					"""
					SELECT *
					FROM Invoice
					WHERE (CustomerId IN (56,58)) AND (Total BETWEEN 1 AND 5)
					""", conn)
#print(query_4)



"""
Query 5: Find all the tracks whose name starts with 'All'.
"""
query_5 =pd.read_sql(
					"""
					SELECT *
					FROM Track
					WHERE Name LIKE "All%"
					""", conn)
#print(query_5)



"""
Query 6: Find all the customer emails that start with "J" and are from gmail.com.
"""
query_6 =pd.read_sql(
					"""
					SELECT *
					FROM Customer
					WHERE Email LIKE 'J%gmail.com'
					""", conn)
#print(query_6)



"""
Query 7: Find all the invoices from the billing city Brasília, Edmonton, and
Vancouver and sort in descending order by invoice ID.
"""
query_7 =pd.read_sql(
					"""
					SELECT *
					FROM Invoice
					WHERE BillingCity IN ('Brasília', 'Edmonton', 'Vancouver')
					ORDER BY InvoiceID DESC
					""", conn)
#print(query_7)



"""
Query 8: Show the number of orders placed by each customer (hint: this is
found in the invoices table) and sort the result by the number of orders in
descending order.
"""
query_8 =pd.read_sql(
					"""
					SELECT CustomerID, COUNT(InvoiceId) as total_order
					FROM Invoices
					GROUP BY CustomerID
					ORDER BY total_order DESC
					""", conn)
#print(query_8)



"""
Query 9: Find the albums with 12 or more tracks.
"""
query_9 =pd.read_sql(
					"""
					SELECT AlbumId, COUNT(TrackId) AS Number_of_tracks
					FROM Track
					GROUP BY AlbumId
					HAVING Number_of_tracks >= 12
					""", conn)
#print(query_9)
