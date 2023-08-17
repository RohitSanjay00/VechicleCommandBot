import requests
class functions:  
    def getting_function(value):
        if value == "Engine_On()":
            r = functions.Engine_On()
            return r
        elif value == "Rollup_Windows()":
            r = functions.Rollup_Windows()
            return r
        elif value == "Get_Charge()":
            r = functions.Get_Charge()
            return r
        elif value == "Get_System_Status()":
            r = functions.Get_System_Status()
            return r
        elif value == "Unknown()":
            r = functions.Unknown()
            return r
        elif value == "Check_Doors()":
            r = functions.Check_Doors()
            return r
        elif value == "Get_Range()":
            r = functions.Get_Range()
            return r
        elif value == "Unlock_Doors()":
            r = functions.Unlock_Doors()
            return r
        elif value == "Check_Windows()":
            r = functions.Check_Windows()
            return r
        elif value == "Lock_Doors()":
            r = functions.Lock_Doors()
            return r
        elif value == "Rolldown_Windows()":
            r = functions.Rolldown_Windows()
            return r
        elif value == "Check_Engine()":
            r = functions.Check_Engine()
            return r
        elif value == "Engine_Off()":
            r = functions.Engine_Off()
            return r
        else:
            r = "Not part of the mapping"
            return r

    def Engine_On():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['engine_status'] = 'On'
        requests.post(url, json=data)
        #print(response.text)
        response = "The engine is on"
        return response

    def Rollup_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['windows_status'] = 'Closed'
        requests.post(url, json=data)
        #print(response.text)
        response = "The windows are rolled up"
        return response

    def Get_Charge():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['Charge'] 
        response = f'the current charge is {status}'
        return response

    def Get_System_Status():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['system_status'] 
        response = f'the current system status is {status}'
        return response

    def Unknown():
        response = "Sorry I can't do that"
        return response

    def Check_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['doors_locked'] 
        response = f'the doors are {status}'
        return response
        

    def Get_Range():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['range_value'] 
        response = f'the range left is {status}'
        return response

    def Unlock_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['doors_locked'] = 'Unlock'
        requests.post(url, json=data)
        #print(response.text)
        response = "The doors are unlocked"
        return response

    def Check_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['windows_status'] 
        response = f'the windows are {status}'
        return response

    def Lock_Doors():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['doors_locked'] = 'Locked'
        requests.post(url, json=data)
        #print(response.text)
        response = "The doors are locked"
        return response

    def Rolldown_Windows():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['windows_status'] = 'Open'
        response = requests.post(url, json=data)
        #print(response.text)
        response = "The windows are rolled down"
        return response

    def Check_Engine():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        status = data['engine_status'] 
        response = f'the engine is {status}'
        return response
        
    def Engine_Off():
        url = 'http://127.0.0.1:5000/'
        response = requests.get(url, headers={'Content-Type': 'application/json'})
        data = response.json()
        data['engine_status'] = 'Off'
        response = requests.post(url, json=data)
        #print(response.text)
        response = "The engine is off"
        return response









    