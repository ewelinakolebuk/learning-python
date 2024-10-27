import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]
gray_fur_amount = 0
cinnamon_fur_amount = 0
black_fur_amount = 0
for fur in fur_data:
    if fur == "Gray":
        gray_fur_amount+=1
    if fur == "Cinnamon":
        cinnamon_fur_amount+=1
    if fur == "Black":
        black_fur_amount+=1
print(gray_fur_amount)
print(cinnamon_fur_amount)
print(black_fur_amount)
fur_dict={
    "Fur Color":["gray", "cinnamon", "black"],
    "Count":[gray_fur_amount,cinnamon_fur_amount,black_fur_amount]
}
fur_color_data = pandas.DataFrame(fur_dict)
print(fur_color_data)
fur_color_data.to_csv("squirrel_count")

# Angela's solution
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")