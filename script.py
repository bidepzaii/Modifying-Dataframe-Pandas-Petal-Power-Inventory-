import codecademylib3
import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory.iloc[0:11]
print(staten_island)

product_request = inventory['product_description']
print(product_request)

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

inventory['in_stock'] = inventory.quantity.apply(lambda quantity: True if quantity > 0 else False)

inventory['total_value'] = inventory['price'] * inventory['quantity']

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)




print(inventory.head(10))




