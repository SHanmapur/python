import csv, sys, operator


def process_csv_for_data(csv_2d_array):
    # method to process csv data to 2D array
    fruits_data = []
    size_data = []
    color_data = []
    shape_data = []
    days_data = []
    color_shape = []

    csv_2d_array.pop(0)
    # flattening 2d array to single array of each coulmn
    for data in csv_2d_array:
        fruits_data.append(data[0])
        size_data.append(int(data[1]))
        color_data.append(data[2])
        shape_data.append(data[3])
        color_shape.append(data[2] + ", " + data[3])
        days_data.append(data[4])

    return fruits_data, size_data, color_data, shape_data, days_data, color_shape


def total_number_of_fruits(size_array):
    return sum(size_array)


def unique_fruits(fruits_data):
    unique_fruits_list = set(fruits_data)
    return unique_fruits_list, len(unique_fruits_list)


def per_fruit_data(fruits_data, size_data, color_data, shape_data, days_data, color_shape, unique_fruits_list):
    # method to convert fruit data to dict and return dict value
    fruit_count = {}
    fruit_color = {}
    fruit_shape = {}
    fruit_days = {}
    fruit_char = {}

    for fruit in unique_fruits_list:

        total_fruit = 0
        color = []
        shape = []
        days = []
        characteristics = []
        for i in range(len(fruits_data)):

            if fruit == fruits_data[i]:
                total_fruit = total_fruit + size_data[i]
                color.append(color_data[i])
                shape.append(shape_data[i])
                days.append(days_data[i])
                characteristics.append(color_shape[i])

        fruit_count[fruit] = total_fruit
        fruit_color[fruit] = color
        fruit_shape[fruit] = shape
        fruit_days[fruit] = days
        fruit_char[fruit] = color_shape

    fruit_count = dict(sorted(fruit_count.items(), key=operator.itemgetter(1), reverse=True))

    return fruit_count, fruit_color, fruit_shape, fruit_days, fruit_char


def read_csv(file_name):
    csv_2d_array = []
    with open(file_name + ".csv", 'r') as file:
        reader = csv.reader(file)

        # converting csv data to 2D array
        for data in reader:
            csv_2d_array.append(data)

        return csv_2d_array


def get_fruit_characteristics(fruits_data, size_data, color_data, shape_data, color_shape, unique_fruits_list):
    fruit_char_array = []
    fruit_count_array = []
    fruit_char = {}
    for fruit in unique_fruits_list:
        for i in range(len(fruits_data)):
            if fruit == fruits_data[i] and color_shape[i] == color_data[i] + ", " + shape_data[i]:
                fruit_char_array.append(fruits_data[i] + ": " + color_shape[i])
                fruit_count_array.append(size_data[i])

    unique_fruit_character = set(fruit_char_array)

    for character in unique_fruit_character:
        total_fruits = 0
        for i in range(len(fruits_data)):

            if (character == fruit_char_array[i]):
                total_fruits = total_fruits + fruit_count_array[i]
        fruit_char[character] = total_fruits

    return fruit_char


def get_above_3_days_data(fruits_data, size_data, days_data, unique_fruits_list):

    fruit_above_3_days= {}
    for fruit in unique_fruits_list:
        total_fruits = 0

        for i in range(len(fruits_data)):

            if fruit == fruits_data[i] and int(days_data[i]) > 3:
                total_fruits = total_fruits + size_data[i]
        if total_fruits > 0:
            fruit_above_3_days[fruit] = total_fruits

    return fruit_above_3_days


def process_data(file_name):
    # method to read CSV file and process the data to print the results

    csv_data = read_csv(file_name)
    fruits_data, size_data, color_data, shape_data, days_data, color_shape = process_csv_for_data(csv_data)

    total_fruits = total_number_of_fruits(size_data)
    unique_fruits_list, types_of_fruits = unique_fruits(fruits_data)

    fruit_count, fruit_color, fruit_shape, fruit_days, fruit_char = per_fruit_data(fruits_data, size_data, color_data,
                                                                                   shape_data,
                                                                                   days_data, color_shape,
                                                                                   unique_fruits_list)

    fruits_features = get_fruit_characteristics(fruits_data, size_data, color_data, shape_data, color_shape,
                                                unique_fruits_list)
    fruits_older_than_3days = get_above_3_days_data(fruits_data, size_data, days_data, unique_fruits_list)
    return total_fruits, types_of_fruits, fruit_count, fruit_color, fruit_shape, fruit_days, fruits_features, fruits_older_than_3days


def print_fruits_descending_order(fruit_count):
    # Method to print fruits in descending order

    for fruit, count in fruit_count.items():
        print(fruit, ":", count)


def print_characteristics(fruit_features):
    # Method to print characteristics of fruit

    for feature, count in fruit_features.items():
        print(count, feature)


def print_older_fruits(fruits_older_than_3days):
    # Method to print fruits > 3 days old

    older_fruits =""
    for fruit, count in fruits_older_than_3days.items():

        older_fruits += str(count) + " " + fruit + ","
    older_fruits +=  "are over 3 days old"
    print(older_fruits)


if __name__ == "__main__":
    file_name = sys.argv[1]
    total_fruits, types_of_fruits, fruit_count, fruit_color, fruit_shape, fruit_days, fruit_features, fruits_older_than_3days = process_data(
        file_name)
    print("Total number of fruit:", total_fruits)
    print("Total types of fruit:", types_of_fruits)
    print("The number of each type of fruit in descending order")
    print_fruits_descending_order(fruit_count)
    print("The characteristics (size, color, shape, etc.) of each fruit by type")
    print_characteristics(fruit_features)
    print("Have any fruit been in the basket for over 3 days")
    print_older_fruits(fruits_older_than_3days)
