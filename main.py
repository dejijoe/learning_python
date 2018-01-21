#currency converter




rates = [
    {
        'country':'USA',
        'currency':'USD',
        'rate': 360
    },
    {
        'country':'UK',
        'currency':'GBP',
        'rate': 500
    },

    {
        'country':[],
        'currency':'BTC',
        'rate': 4551124.12
    },

    {
        'country':'GHANA',
        'currency':'GHS',
        'rate': 78.50
    },

    {
        'country':['France', 'Spain', 'Germany', 'Italy'],
        'currency':'EUR',
        'rate': 440
    },

]

print('Welcome to our meetup python application')
print('We only currently support Naira(Nigerian currency)')
currency_or_country = input('Please a country or currency: ')
amount = input('please enter amount:')



result = None
kind = None
for record in rates:
   
    if currency_or_country.lower() == record['currency'].lower():
        result = record['rate']
        kind = 'currency'
        break

    similar_case_country = []
    for country in record['country']:
        similar_case_country.append(country.lower())
    if currency_or_country.lower() in similar_case_country:
        result = record['rate']
        kind = 'country'
        break

if result:
    print("The rate for {} which is a {} is {}".format(currency_or_country, kind, result))
    print("The equivalent amount is {}".format(int(amount) * result))
else:
    print('Sorry! we could not find your country/currency ')