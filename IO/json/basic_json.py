# read
import json

file_path = "data.json"
# with open(file_path, "r") as f:
#     file_contents = json.load(f)


with open(file_path, "r+") as f:
    file_contents = json.load(f)
    file_contents["kids"].append({"name": "ori"})
    file_contents["age"] += 1
    f.seek(0)
    json.dump(file_contents, f)
