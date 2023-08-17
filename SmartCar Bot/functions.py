import requests
class functions:  
    def getting_function(value):
        if value == "Engine_On()":
            functions.Engine_On()
        elif value == "Rollup_Windows()":
            functions.Rollup_Windows()
        elif value == "Get_Charge()":
            functions.Get_Charge()
        elif value == "Get_System_Status()":
            functions.Get_System_Status()
        elif value == "Unknown()":
            functions.Unknown()
        elif value == "Check_Doors()":
            functions.Check_Doors()
        elif value == "Get_Range()":
            functions.Get_Range()
        elif value == "Unlock_Doors()":
            functions.Unlock_Doors()
        elif value == "Check_Windows()":
            functions.Check_Windows()
        elif value == "Lock_Doors()":
            functions.Lock_Doors()
        elif value == "Rolldown_Windows()":
            functions.Rolldown_Windows()
        elif value == "Check_Engine()":
            functions.Check_Engine()
        elif value == "Engine_Off()":
            functions.Engine_Off()
        else:
            print("Not part of the mapping")

    def Engine_On():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['engine_status'] = 'On'
        response = requests.post(url, json=data)
        print(response.text)

    def Rollup_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['windows_status'] = 'Closed'
        response = requests.post(url, json=data)
        print(response.text)

    def Get_Charge():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['Charge'] 
        print(status)

    def Get_System_Status():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['system_status'] 
        print(status)

    def Unknown():
        print("Unknow Command")

    def Check_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['doors_locked'] 
        print(status)

    def Get_Range():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['range_value'] 
        print(status)

    def Unlock_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['doors_locked'] = 'Unlock'
        response = requests.post(url, json=data)
        print(response.text)

    def Check_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['windows_status'] 
        print(status)

    def Lock_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['doors_locked'] = 'Locked'
        response = requests.post(url, json=data)
        print(response.text)

    def Rolldown_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['windows_status'] = 'Closed'
        response = requests.post(url, json=data)
        print(response.text)

    def Check_Engine():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['engine_status'] 
        print(status)
        
    def Engine_Off():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['engine_status'] = 'Off'
        response = requests.post(url, json=data)
        print(response.text)









    