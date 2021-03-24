# DIMENSION TABLES DEFINITION


# Dim_Category
Dim_Category = """
CREATE TABLE IF NOT EXISTS 'Dim_Category' ( 
	'category'	INTEGER,
	'category_name'	TEXT,
	PRIMARY KEY('category')
);
	"""
# Dim_Store
Dim_Store = """
CREATE TABLE IF NOT EXISTS 'Dim_Store' (
	'store_number'	INTEGER,
	'store_name'	TEXT,
	'address'	TEXT,
	'city'	TEXT,
	'zip_code'	INTEGER,
	'store_location'	TEXT,
	'county_number'	INTEGER,
	'county'	TEXT,
	PRIMARY KEY('store_number')
);
"""
Dim_Vendor = """
-- Dim_Vendor
CREATE TABLE IF NOT EXISTS 'Dim_Vendor' (
	'vendor_number'	INTEGER,
	'vendor_name'	TEXT,
	PRIMARY KEY('vendor_number')
);
"""
Dim_Item = """
-- Dim_Item
CREATE TABLE IF NOT EXISTS 'Dim_Item' (
	'item_number'	INTEGER,
	'item_description'	TEXT,
	'bottle_volume_ml'	INTEGER,
	PRIMARY KEY('item_number')
);
"""

Fact_Sales = """
CREATE TABLE IF NOT EXISTS 'Fact_Sales' (
	'invoice_and_item_number'	TEXT,
	'store_number'	INTEGER,
	'category'	TEXT,
	'vendor_number'	INTEGER,
	'item_number'	INTEGER,
	'pack'	TEXT,
	'bottle_volume_ml'	INTEGER,
	'state_bottle_cost'	NUMERIC,
	'state_bottle_money'	NUMERIC,
	'bottles_sold'	INTEGER,
	'sale_dollards'	NUMERIC,
	'volume_sold_liters'	NUMERIC,
	'volume_sold_gallons'	NUMERIC,
    PRIMARY KEY('invoice_and_item_number'),
	FOREIGN KEY('vendor_number') REFERENCES Dim_Vendor(vendor_number),
	FOREIGN KEY('store_number') REFERENCES Dim_Store(store_number),
	FOREIGN KEY('item_number') REFERENCES Dim_Item(item_number),
	FOREIGN KEY('category') REFERENCES Dim_Category(category)
);
"""