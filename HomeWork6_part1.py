lst =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750 }]
result = {}
for item in lst:
    key = item['item']
    value = item['amount']
    if key in result:
        result[key] += value
    else: result[key] = value

print(result)
