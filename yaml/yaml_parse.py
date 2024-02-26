import yaml

def main():
    employee_list = employee_names()
    for name in employee_list:
        print(name)

def employee_names():
    with open('data.yaml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        
        names = [] 
        
        for employee in data['employees']:
            names.append(employee['name']) 
        
        return names 

      
if __name__ == "__main__":
    main()

