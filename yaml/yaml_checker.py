import yaml

def main():
    with open('data2.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print(validate_values(data))
        
def validate_values(data):
    if type(data['app_name']) == str and type(data['database']['host']) == str and type(data['database']['port']) == int and type(data['database']['username']) == str and type(data['database']['password']) == str and type(data['database']['database_name']) == str:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()