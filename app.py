import os
from sqlalchemy import create_engine
from sql_tables_creation_dim_and_facts import Dim_Category, Dim_Vendor, Dim_Item, Fact_Sales, Dim_Store
from sql_insert_into_star_schema import Dim_Store_Insert_Data, Delete_Store_Data, Delete_Vendor_Data, Dim_Vendor_Insert_Data, Delete_Item_Data, Dim_Item_Insert_Data, Delete_FactSales_Data, Fact_Sales_Insert_Data, Delete_Category_Data, Dim_Category_Insert_Data 



import pandas as pd

dbpath = os.path.join('database','mydatabase.db')
# connect to sqlite database
engine = create_engine(f"sqlite:///{dbpath}")
print(Dim_Category, Dim_Vendor, Dim_Item, Fact_Sales)
create_tables_list = [Dim_Category, Dim_Vendor, Dim_Item, Fact_Sales, Dim_Store]
table_names = ["Dim_Category", "Dim_Vendor", "Dim_Item", "Fact_Sales", "Dim_Store"]
counter = 0
# creating our star schema with python 
for item in create_tables_list:
    print(f"creating table {table_names[counter]}")
    create_query = engine.execute(item) 
    print(f"table {table_names[counter]} was created")
    counter = counter + 1

    
    
# read denormalized data from csv, put it into a pandas dataframe, and send to the sqlite database
datapath = os.path.join('inputdata','liquorsalesdenormalized.csv')
mycsvdata = pd.read_csv(datapath) 
print("sending our data from the pandas dataframe (csv) to our sqlitedb")
# send data to sqlite from the mycsvdata dataframe
mycsvdata.to_sql('liquorsalesdenormalized', if_exists = 'replace', con = engine)
print("data was correctly sent to our new table")




# Inserting data into our Dimension and Fact Tables
list_inserts = [Dim_Store_Insert_Data, Dim_Vendor_Insert_Data, Dim_Item_Insert_Data, Fact_Sales_Insert_Data, Dim_Category_Insert_Data]
list_deletes = [Delete_Store_Data, Delete_Vendor_Data, Delete_Item_Data, Delete_FactSales_Data, Delete_Category_Data]
new_counter = 0
for insert in list_inserts:
    print(f"inserting data into table {new_counter + 1}")
    delete_from_dim_store = engine.execute(list_deletes[new_counter])
    insert_into_dim_store = engine.execute(insert)
    print(f"data was inserted into table {new_counter + 1}")
    new_counter = new_counter + 1

print("Done, our data is now in the star schema table in the sqlite!")
# Done
