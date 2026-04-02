import pandas as pd

sales = pd.read_csv('sales.csv')
products = pd.read_csv('products.csv')

data = pd.merge(sales, products[['ProductID','Price','Class',
                                'Resistant','IsAllergic','VitalityDays']],
                                on='ProductID', how='left')

data['TotalPrice'] = data['Quantity'] * data['Price'] * (1 - data['Discount'])

data_final = data[['Quantity','Discount','Price','Class',
                    'Resistant','IsAllergic','VitalityDays','TotalPrice']]
data_final.to_csv('sales_final.csv', index=False)