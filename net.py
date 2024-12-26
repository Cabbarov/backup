from netmiko import ConnectHandler
from hosts import hosts
import os


import schedule
import time

def my_script():
    print("Running script...")
    # Add your script logic here
    username = 'fuad'
    password = 'C@bb@r0v7361'
    port = 22
    device_type = 'juniper'

    from datetime import datetime

    # Get the current time
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d-%m-%Y")



    for host in hosts:
        virtual_srx = {
            'device_type': device_type,
            'host': host,
            'username': username,
            'password': password,
            'port': port,
        }

        net_connect = ConnectHandler(**virtual_srx)
        print(f'{host}')
        output = net_connect.send_command('show configuration | display set')


        # Define folder and file paths
        folder_name = formatted_time
        file_name = host
        file_content = output

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Create and write content to the text file
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            file.write(file_content)

        print(f"Folder '{folder_name}' and file '{file_name}' created successfully.")

        net_connect.disconnect()

# Schedule the function to run dayly on a specific time  
schedule.every().day.at("10:00").do(my_script) # Adjust day and time

print("Scheduler running... Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)




   
