# Import required libraries
import sqlite3
import pandas as pd
import pyodbc

data = pd.read_csv(r'C:\Users\aqml\PycharmProjects\ITMO2022.Python\Practice02\FinalTask\Export.csv')
df = pd.DataFrame(data)

print(df)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=(localdb)\Local;'
                      'Database=FarmersMarket;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#
# # Connect to SQLite database
# conn = sqlite3.connect(r'C:\Users\aqml\FarmersMarket.mdf')
#
#
# # Load CSV data into Pandas DataFrame
# farm_market_data = pd.read_csv('Export.csv')
# # Write the data to a sqlite table
# farm_market_data.to_sql('student', conn, if_exists='replace', index=False)
#
# # Create a cursor object
# cur = conn.cursor()
# # Fetch and display result
# for row in cur.execute('SELECT * FROM student'):
#     print(row)
# # Close connection to SQLite database
# conn.close()
