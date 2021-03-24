# DIMENSION TABLES DEFINITION


# Dim_Category
Delete_Category_Data = "delete from Dim_Category where category>=0"
Dim_Category_Insert_Data = """
INSERT INTO Dim_Category (category, category_name) 
select distinct cast(category as INT), max(category_name) as category_name from liquorsalesdenormalized
where category is not null and category_name is not null
group by cast(category as INT);
	"""
# Dim_Store
Delete_Store_Data = "delete from Dim_Store where store_number>=0"
Dim_Store_Insert_Data = """
insert into Dim_Store (store_number, store_name, address, city, zip_code, store_location, county_number, county)
select distinct 
cast(store_number as INT) as store_number,
max(store_name) as store_name,
max(address) as address,
max(city) as city,
00000 as zip_code,
max(store_location) as store_location,
00000 as county_number,
max(county) as county
from liquorsalesdenormalized
group by cast(store_number as INT);
"""

Delete_Vendor_Data = "delete from Dim_Vendor where vendor_number>=0"
Dim_Vendor_Insert_Data = """
	insert into Dim_Vendor (vendor_number, vendor_name) 
	select distinct cast(vendor_number as INT),
	max(vendor_name) from liquorsalesdenormalized
	where cast(vendor_number as INT) is not null
	group by cast(vendor_number as INT);
"""

Delete_Item_Data = "delete from Dim_Item where item_number>=0;"
Dim_Item_Insert_Data = """
INSERT INTO Dim_Item (item_number, item_description, bottle_volume_ml)
select distinct cast(item_number as INT),
max(item_description) as item_description, 
max(bottle_volume_ml) as bottle_volume_ml 
from liquorsalesdenormalized
group by cast(item_number as INT);
"""

Delete_FactSales_Data = "delete from Fact_Sales where invoice_and_item_number is not null"
Fact_Sales_Insert_Data = """
INSERT INTO Fact_Sales (invoice_and_item_number, store_number, category, vendor_number, item_number, pack, 
bottle_volume_ml, state_bottle_cost, state_bottle_money, bottles_sold, volume_sold_liters, volume_sold_gallons) 
SELECT distinct
cast (invoice_and_item_number as TEXT), 
cast(store_number as INT), cast(category as INT), cast(vendor_number as INT), cast(item_number as INT) as item_number,
pack, bottle_volume_ml ,state_bottle_cost, state_bottle_retail as state_bottle_money, bottles_sold,volume_sold_liters,volume_sold_gallons 
from liquorsalesdenormalized
"""