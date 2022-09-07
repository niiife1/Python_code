def start_spring(**example):
    result = ''
    example_order = {}
    first = []
    for k, v in example.items():
        example_order[v] = example_order.get(v, []) + [k]
        first_sort =  sorted(example_order.items(), key=lambda x: (-len(x[1]), x[0]))
    for key in example_order.keys():
        result += f"{key}:\n"
        for index in first_sort:
            first =  index[0]
            second = index[1]
            sorted_second = sorted(second)
            for ind in range(len(second)):
                result += f"-{ind} \n"
    return result.strip()
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))