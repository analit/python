from lxml import html
import requests

amount = 2650
currency_from = "UAH"
currency_to = "USD"


response = requests.get("https://www.cbr.ru/currency_base/daily.aspx?date_req=26.10.2017")
tree = html.fromstring(response.content)

xpath_from = "//table[@class='data']/tbody/tr[td[contains(text(),'%s')]]" % currency_from
xpath_to = "//table[@class='data']/tbody/tr[td[contains(text(),'%s')]]" % currency_to
result_from = tree.xpath(xpath_from)
result_to = tree.xpath(xpath_to)

rate_from = float(result_from[0].xpath("td")[4].text.replace(",", ".")) / float(result_from[0].xpath("td")[2].text)
rate_to = float(result_to[0].xpath("td")[4].text.replace(",", ".")) / float(result_to[0].xpath("td")[2].text)

print(rate_from)
print(rate_to)

print(2650 * rate_from / rate_to)
