def color_list_set():
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}

    difference_colors = color_list_1 - color_list_2
    return difference_colors


result = color_list_set()
print("Colors from color_list_1 not present in color_list_2:", result)
