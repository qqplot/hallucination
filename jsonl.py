import json

with open('data/truthfulqa/mc_task.json', 'r') as input_file, open('data/truthfulqa/mc_task.jsonl', 'w') as output_file:
    json_data = json.load(input_file)
    for item in json_data:
        json_line = json.dumps(item)
        output_file.write(json_line + '\n')
