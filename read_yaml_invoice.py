import yaml
from pprint import pprint

with open('DATA/invoice.yaml') as invoice_in:
    invoice_data = yaml.load(invoice_in, Loader=yaml.BaseLoader)

pprint(invoice_data)
print()

print(invoice_data['invoice'])
for product in invoice_data['product']:
    print(product['description'], product['price'])


airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

mydata = {
    'airports': airports,
#    'fruits': fruits,
}

with open('stuff.yaml', "w") as stuff_out:
    yaml.dump(mydata, stuff_out, Dumper=yaml.BaseDumper)
