import json 

def make_class_list(classesJson):
    class_file = open(classesJson)
    data = json.load(class_file)
    class_list = []

    for key in data:
        sections = []
        for section in data[key]["Sections"]:
            sections.append(section["Section Number"])
        class_list.append((key, sections))
    return class_list


def search_classes(prefix, class_list):
    results = []
    for curr in class_list:
        class_name = curr[0]
        if not class_name.startswith(prefix):
            continue
        results.append(curr)
    return results


class_list = make_class_list("pushin-pp/website/json/classes.json")
# print(class_list)
res = search_classes("CS 2", class_list)
print(res)
