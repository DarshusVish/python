import csv

stock_price = []
with open("stock.csv","r") as f:
    # csv_reader = csv.reader(csv_file,delimiter=",")
    for line in f:
        day,price = line.split(",")
        price = float(price)
        stock_price.append([day,price])

print(stock_price)

stock_dict={}
with open("stock.csv","r") as f1:
    for line in f1:
        day, price = line.split(",")
        price = float(price)
        stock_dict[day] = price

print(stock_dict)

print(stock_dict["23-Nov"])