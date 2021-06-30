import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns



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
Query 1: Using a subquery, find the names of all the tracks for the album
"Californication".
"""
query_1 = pd.read_sql(
					"""
					SELECT TrackId, Name
					FROM Track
					WHERE AlbumId IN (SELECT AlbumId
														FROM Album
														WHERE Title = "Californication")
					""", conn)
#print(query_1)



"""
Query 2: Find the total number of invoices for each customer along with the
customer's full name, city and email.
"""
query_2 = pd.read_sql("""
											SELECT ct.FirstName, ct.LastName, ct.City, ct.Email, COUNT(InvoiceId) AS number_of_invoices
											FROM Customer ct LEFT JOIN Invoice inv ON ct.CustomerId = inv.CustomerId
											GROUP BY ct.CustomerId
											""",conn)
#print(query_2)



"""
Query 3: Retrieve the track name, album, artistID, and trackID for all the
albums.	
"""
query_3 = pd.read_sql("""
											SELECT tr.Name, al.Title, al.ArtistId,tr.TrackId
											FROM Album al INNER JOIN Track tr ON al.AlbumId = tr.AlbumId
											""",conn)
#print(query_3)



"""
Query 4: Retrieve a list with the managers last name, and the last name of the
employees who report to him or her.
"""
query_4 = pd.read_sql("""
											SELECT em.LastName, re.LastName as reports_to, re.Title
											FROM Employee em, Employee re
											WHERE (em.ReportsTo = re.EmployeeId) and (re.Title LIKE "%Manager")
											""",conn)
#print(query_4)



"""
Query 5: Find the name and ID of the artists who do not have albums. 
"""
query_5 = pd.read_sql("""
											SELECT ar.Name, COUNT(al.AlbumId) AS total_albums
											FROM Artist ar LEFT JOIN Album al ON ar.ArtistId= al.ArtistId
											GROUP BY  ar.ArtistId
											HAVING total_albums = 0
											""",conn)
#print(query_5)



"""
Use a UNION to create a list of all the employee's and customer's first names and last names ordered by the last name in descending order.
"""
query_6 = pd.read_sql("""
											  SELECT LastName, FirstName
											  FROM Customer
											  UNION
											  SELECT LastName, FirstName
											  FROM Employee
											  ORDER BY LastName DESC
											  """,conn)
#print(query_6)



"""
Query 7: See if there are any customers who have a different city listed in
their billing city versus their customer city.
"""
query_7 = pd.read_sql("""
										  SELECT cus.LastName, cus.FirstName, cus.City, inv.BillingCity
										  FROM Customer cus INNER JOIN Invoice inv ON cus.CustomerId = inv.CustomerId
										  WHERE cus.City <> inv.BillingCity
										  """,conn)
#print(query_7)




