import yaml

def main():
    with open('data3.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    
    update_file(data)

def update_file(data):
    if 'grades' not in data:
        data['grades'] = []
        
    history_entry = next((item for item in data['grades'] if item.get("subject") == "History"), None)
    if history_entry:
        history_entry['grade'] = 92
    else:
        data['grades'].append({'subject': 'History', 'grade': 92})

    with open('data3.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(data, file)

if __name__ == "__main__":
    main()