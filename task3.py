# banker.ua
# http://www.platesh.ru/annuitetnie-plateshi/

data = {"amount": 12000, "term": 12, "percent": 20}
monthPercent = data['percent'] / 12 / 100;
monthPay = data['amount'] * (monthPercent + (monthPercent / (pow(monthPercent + 1, data["term"]) - 1)))


def get_amount(body):
    data["amount"] = data["amount"] - body
    return data["amount"]


result = {month + 1: {"debt": monthPay, "percent_amount": data["amount"] * monthPercent,
                      "debt_rest": get_amount(monthPay - (data["amount"] * monthPercent))}
          for month in range(data["term"])}

print("| %+8s | %+14s | %+14s | %+14s |" % ('month', 'percent amount', 'debt', "debt rest"))
for month, month_data in result.items():
    print("| % 8d | % 14.2f | % 14.2f | % 14.2f |" % (

        month, month_data['percent_amount'], month_data['debt'], month_data['debt_rest']))
