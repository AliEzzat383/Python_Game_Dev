# # data = []
# # with open("2.1 weather_data.csv") as f:
# #     data = f.readlines()
# # print(data)
# # import csv
# # with open("2.1 weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
import pandas

data = pandas.read_csv("2.1 weather_data.csv")
# print(data)
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].tolist()

# print(len(temp_list))
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# get column
# print(data.condition) # = data["condition"]

# get row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday.temp = int(monday.temp)
# print(monday.temp)
# monday.temp = (9 / 5) * monday.temp + 32
# print(monday.temp)
# pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_csv.csv")
# ***********************************my code****************************
from squirrels import Squirrel, COLOR_LIST
import pandas
data = pandas.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_list = data["Primary Fur Color"].tolist()
rat = Squirrel()
for color in rat.list:
    for item in data_list:
        color.compare(item)
count_list = []
data_dict = {}
for color in rat.list:
    count_list.append(color.count)
    # print(f"{color.name}s = {color.count}")
data_dict["Fur color"] = COLOR_LIST
data_dict["count"] = count_list
# print(count_list)
# print(data_dict)
df = pandas.DataFrame(data_dict, columns=["Fur color", "count"])
df.to_csv("squirrel_count.csv")
# ********************************her code**********************************
# import pandas
#
# data = pandas.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# count_list = []
# color_list = ["Gray", "Cinnamon", "Black"]
# for color in color_list:
#     count_list.append(len(data[data["Primary Fur Color"] == color]))
#
# data_dict = {
#     "Fur Color": color_list,
#     "Count": count_list
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count_Angela.csv")
