import json
import shopify
import csv

API_KEY = 'de7e8b82634adf7d6c58e12b55fe5ea2'
API_SECRET = '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'
PASSWORD = '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'
SHOP_NAME = 'k2-tech-store'

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)

customer = shopify.Customer.find()
jsonArr = []
for c in customer:
    jsonStr = json.dumps(c.attributes)
    jsonArr.append(jsonStr)

print(jsonArr)

# for i in range(len(jsonArr)):
#     data = jsonArr[i]
#     with open('K2_Customer.csv', 'w') as outf:
#         dw = csv.DictWriter(outf, data[0].keys())
#         dw.writeheader()
#         for row in data:
#             dw.writerow(row)
