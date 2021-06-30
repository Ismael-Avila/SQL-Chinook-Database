# Chinook Database

Chinook is a sample database available for SQL Server, Oracle, MySQL, etc. It can be created by running a single SQL script.

# Data Model

The Chinook data model represents a digital media store, including tables for artists, albums, media tracks, invoices and customers. You can see the Chinook data model below.

![DbSchema](https://user-images.githubusercontent.com/72403273/123901397-76d10700-d930-11eb-8984-fd5061594993.png)

# Explanation
This repository contains a folder that has many files that interact with the Chinook database. Each file contains a set of queries written in python 3 that receives a SQL query. At the beginning of each query is added a simple description of the query does follow by the code and finally a print function to see the result of the query.

```
"""
Description of the query
"""

query =  pd.read_sql("""
                     SELECT *
                     FROM ---
                     WHERE ---
                     """, conn)
print(query)
```

# Prerequesites
Python 3

# Running

To execute each one of the files contained in the folder only use the next sintaxis in your linux or windows terminal.
```
python3 file_name
```
# Note
All the ***print(query)*** are commented, if you want to see a specific query only uncomment it.
