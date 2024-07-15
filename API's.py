#URL of the API & end point
url = "https://jsonplaceholder.typicode.com/posts"

#Making a GET request to  a server(retriving or collecting data)
response = requests.get(url)

#Checking if the request was successful
if response.status_code == 200:
    #parse the json response
    data = response.json()
    print("Data submitted",data)
else:
    print("Failed to retrive")



#How to deal with secure APIs

import requests 

url = "https://dihfahsih.com/api/reviews-list-secured/"
token = "a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload = {
    "Authorization" : f'Token {token}'
}
response = requests.get(url,headers=token_payload)

if response.status_code == 200:
    data = response.json()
    print(data[-1])
else:
    print("Failed to retrive")
    print("Status_cod :",response.status_code)   
    print("Response",response.text)     
    


#How to POST an API
import requests
#URL of the API & end point
url = "https://dihfahsih.com/api/review/"

#Data to be sent
data ={
    "first_name" : "John",
    "last_name"  : "Mosh",
    "status" : "Married",
    'loan _balance' : 10000000,
    'Applicant_Income' : 10000000,
    "credit_history" : 1.0
}

response = requests.post(url,json=data)
#Checking if the request was successful
if response.status_code==201:
       #parse the json response
    new_post=response.json()
    print("Data submited",new_post)
    
else:
    print("Failed to create a post")
    print("Status_cod :",response.status_code)   
    print("Response",response.text) 
    
    
print('success')
