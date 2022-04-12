# import copy
# import csv
#
# players = [
#     {
#         "first_name": "John",
#         "last_name": "Doe",
#         "rank": 3
#     },
#     {
#         "first_name": "Kevin",
#         "last_name": "McDonald",
#         "rank": 4
#     },
#     {
#         "first_name": "Brad",
#         "last_name": "Kelvin",
#         "rank": 2
#     },
#     {
#         "first_name": "Mihai",
#         "last_name": "Vladimir",
#         "rank": 1
#     }
# ]
#
# print(players)
# sorted_players = sorted(players, key=lambda player: player["rank"])
# print(sorted_players)
# sorted_players_rev = sorted(players, key=lambda player: player["rank"], reverse=True)
# print(sorted_players_rev)
#
#
# def check_top_3_player(player):
#     updated_player = copy.deepcopy(player)
#     updated_player["is_top_3"] = True if updated_player["rank"] <= 3 else False
#     return updated_player
#
#
# players_with_top_3_value = map(check_top_3_player, players)
# print(list(players_with_top_3_value))
#
# first_list = [x for x in range(10)]
# second_list = [x for x in range(10, 100, 10)]
# third_list = [x for x in range(100, 1000, 100)]
# print(first_list)
# print(second_list)
# print(third_list)
#
# for zip_item in zip(first_list, second_list, third_list):
#     first_element, second_element, third_element = zip_item
#     print(first_element, second_element, third_element)
#
# first_list = [x for x in range(10)]
# even_squared_numbers = [x ** 2 for x in first_list if x % 2 == 0]
# print(even_squared_numbers)
#
# even_squared_numbers_v2 = [x ** 2 for x in first_list[2:] if x % 2 == 0]
# print(even_squared_numbers_v2)
#
#
# with open("hello.txt", "w") as file:
#     file.write("Hello World!")
#
# new_cars = [['Dacia', 'Logan', 2005, 75], ['Renault', 'Clio', 2005, 75]]
#
# with open('data.csv', 'a', newline='', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for new_car in new_cars:
#         csv_writer.writerow(new_car)
#
# with open('data.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     for row in rows:
#         print(row)
