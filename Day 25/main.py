# with open("weather_data.csv") as file:
#     data = file.readlines()
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures= []
#     for row in data:
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
temperatures = data["temp"]

average_temp = sum(temperatures)/len(temperatures)
print(average_temp)
print(data["temp"].mean())
print(temperatures.max())

# Get data in columns - obie formy zwracają to samo
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day =="Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
print(monday_temp)
print(f"Monday temperature is {monday_temp*9/5 + 32} F")

# Create a datafreme from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
dataa = pandas.DataFrame(data_dict)
# print(dataa)
dataa.to_csv("new_data.csv")