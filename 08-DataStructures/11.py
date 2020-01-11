from GBP import GBP
   

print('{:<14}{:<7}\n{}'.format('Data', 'Kurs', '='*21))
for record in GBP['rates']:
    print('{:<14}{:<7}'.format(record['effectiveDate'], record['mid']))