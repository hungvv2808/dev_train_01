import json
import shopify
import csv
import requests

API_KEY = 'de7e8b82634adf7d6c58e12b55fe5ea2'
API_SECRET = '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'
PASSWORD = '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'
SHOP_NAME = 'k2-tech-store'

# 1 - using lib shopify
# shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
# shopify.ShopifyResource.set_site(shop_url)
#
# customer = shopify.Customer.find()
# jsonArr = []
# for c in customer:
#     jsonStr = json.dumps(c.attributes)
#     jsonArr.append(jsonStr)
#
# customerJson = '{"customers":[%s]}' % ', '.join(jsonArr)

# 2 - using request
customer_url = 'https://%s.myshopify.com/%s' % (SHOP_NAME, '/admin/api/2021-01/customers.json')
response = requests.get(url=customer_url, headers={'X-Shopify-Access-Token': PASSWORD})
customerJson = response.text

# write to file
x = json.loads(customerJson)
customerList = x['customers']
with open('K2_Customer.csv', 'w') as f:
    fieldnames = customerList[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for cus in customerList:
        writer.writerow(cus)
