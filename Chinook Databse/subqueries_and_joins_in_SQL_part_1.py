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
Query 1: How many albums does the artist Led Zeppelin have? 
"""
query_1 = pd.read_sql(
					"""
					SELECT COUNT(*)
					FROM Album
					WHERE ArtistId IN( SELECT ArtistId
														 FROM Artist
														 WHERE Name = "Led Zeppelin")
					""", conn)

#print(query_1)



"""
Query 2: Create a list of album titles and the unit prices for the artist
"Audioslave".
"""
query_2 = pd.read_sql("""
											SELECT *
											FROM	((Artist ar INNER JOIN Album al ON ar.ArtistId= al.ArtistId)
															INNER JOIN Track tr ON al.AlbumId=tr.AlbumId)
											WHERE ar.Name = "Audioslave"
											""", conn)
#print(query_2)



"""
Query 3: Find the first and last name of any customer who does not have an
invoice. Are there any customers returned from the query?  
"""

query_3 = pd.read_sql("""
											SELECT ct.CustomerId, ct.FirstName, ct.LastName, COUNT(InvoiceId) as total_invoices
											FROM	Customer ct LEFT JOIN Invoice inv ON ct.CustomerId = inv.CustomerId
											GROUP BY ct.CustomerId
											HAVING total_invoices = 0
											""", conn)
#print(query_3)


"""
Query 4: Find the total price for each album.
"""
query_4 = pd.read_sql("""
											SELECT al.Title, SUM(tr.UnitPrice) as total_price
											FROM Album al INNER JOIN Track tr ON al.AlbumId = tr.AlbumId
											GROUP BY al.AlbumId
											ORDER BY al.Title ASC
											""",conn)
#print(query_4)



"""
Query 5: How many records are created when you apply a Cartesian join to the
invoice and invoice items table?
"""
query_5 = pd.read_sql("""
											SELECT COUNT(*)
											FROM Invoice CROSS JOIN InvoiceLine
											""",conn)
#print(query_5)
