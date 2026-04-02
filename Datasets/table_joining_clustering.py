import pandas as pd
from sklearn.preprocessing import LabelEncoder

sales = pd.read_csv('sales.csv')
products = pd.read_csv('products.csv')


data = pd.merge(
    sales,
    products[['ProductID','Price','CategoryID','Class','Resistant','IsAllergic','VitalityDays']],
    on='ProductID',
    how='left'
)


data['TotalPrice'] = data['Quantity'] * data['Price'] * (1 - data['Discount'])

le_class = LabelEncoder()
le_resistant = LabelEncoder()
le_allergic = LabelEncoder()

data['Class_enc'] = le_class.fit_transform(data['Class'])
data['Resistant_enc'] = le_resistant.fit_transform(data['Resistant'])
data['IsAllergic_enc'] = le_allergic.fit_transform(data['IsAllergic'])


clustering_features = ['Quantity', 'Discount', 'Price', 'VitalityDays',
                        'Class_enc', 'Resistant_enc', 'IsAllergic_enc']

clustering_data = data[clustering_features]

clustering_data.to_csv('sales_clustering.csv', index=False)

print("Clustering dataset saved as 'sales_clustering.csv'")
print("Columns:", clustering_data.columns.tolist())