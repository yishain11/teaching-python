# sum list
def sum_list_iter(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum


def sum_list_recursive(num_list):
    if len(num_list) == 0:
        return 0
    num = num_list.pop()
    return num + sum_list_recursive(num_list)


# print(sum_list_iter([1, 2, 3]))
# print(sum_list_recursive([1, 2, 3]))


# graph iteration

family_tree = {
    "name": "Leah",
    "children": [
        {
            "name": "Alice",
            "children": [
                {
                    "name": "Nora",
                    "children": [
                        {
                            "name": "Dan",
                            "children": [
                                {"name": "Josh", "children": []},
                                {"name": "Bill", "children": []},
                            ],
                        },
                    ],
                },
                {"name": "Eli", "children": []},
            ],
        },
        {
            "name": "Bob",
            "children": [
                {"name": "Ivy", "children": []},
                {"name": "Max", "children": []},
            ],
        },
        {
            "name": "Carla",
            "children": [
                {"name": "Omar", "children": []},
            ],
        },
    ],
}


def search_name(root, target_name):
    if root["name"].lower() == target_name.lower():
        return True
    if len(root["children"]) == 0:
        return False
    for child in root["children"]:
        if search_name(child, target_name):
            return True
    return False


print(search_name(family_tree, "bill"))
