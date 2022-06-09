from array import array
import sys
import requests
from time import sleep
# url = input("Scan Site Here : ")
url = "%s" % (sys.argv[1])
# print("hello dirgh how are you")
headers = requests.get(url).headers
if 'X-Frame-Options' in headers:
    print("1. Site is  Not Vulnerable To X-Frame-Options")
else:
    print("1. Site is Vulnerable To X-Frame-Options")
 
if 'Strict-Transport-Security' in headers:
    print("2. Site is  Not Vulnerable To Strict-Transport-Security")
else:
    print("2. Site is Vulnerable To Strict-Transport-Security")
 
if 'Content-Security-Policy' in headers:
    print("3. Site is  Not Vulnerable To Content-Security-Policy")
else:
    print("3. Site is Vulnerable To Content-Security-Policy")
 
if 'X-Content-Type-Options' in headers:
    print("4. Site is  Not Vulnerable To X-Content-Type-Options")
else:
    print("4. Site is Vulnerable To X-Content-Type-Options")
 
if 'Referrer-Policy' in headers:
    print("5. Site is  Not Vulnerable To Referrer-Policy")
else:
    print("5. Site is Vulnerable To Referrer-Policy")
 
if 'Permissions-Policy' in headers:
    print("6. Site is  Not Vulnerable To Permissions-Policy")
else:
    print("6. Site is Vulnerable To Permissions-Policy")
 
    
print("Your Scan Has Been Completed!!")
