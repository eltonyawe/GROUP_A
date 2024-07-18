import json
#Creating a function to read a json file
def read_json_file(filepath):
    with open(filepath,'r') as file:
        data = json.load(file)
        return data
    
#Creating a function to write to json file
def write_json_file(data,filepath):
    with open(filepath,'w') as file:
       data1= json.dump(data,file,indent=2)
       return data1
   
#Determining file location   
filepath = "Datasets/users.json"    
json_read_data=read_json_file(filepath)

#Creating new info thus adding to the json file
new_info ={
    "ID":10002,
    "Name" : "Kaka Elvis",
    "Age" : "50",
    'City' :"Kampala",
        
}

json_read_data.append(new_info) 
write_json_file(json_read_data,filepath)
print(read_json_file(filepath))

