import time
from datetime import datetime as dt
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
#in this program the websites will be blocked for certain working hours
#those websites will be accessible again when working hours are over
# websites That you want to block
website_list = ["www.facebook.com", "www.gmail.com", "www.outlook.com",  "geeksforgeeks.org", "github.com", "coep.org.in"]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 8)
    < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 11)):
        #print(dt.now())
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                #writes all lines in the file which are not there in website_list
                if not any(website in line for website in website_list):
                    file.write(line)
            # removing hostnmes from host file
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
