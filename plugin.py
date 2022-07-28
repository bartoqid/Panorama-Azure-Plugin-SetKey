from get_api_key import get_key
from secret_key import set_key
import getpass

# Enter firewall IP
firewall_ip = input("Please Enter firewall IP: ")
# Enter firewall admin
firewall_admin = input("Please Enter firewall username: ")
# Enter password for firewall
firewall_password = getpass.getpass("Please enter firewall password: ")
#Enter the service principal name
service_principal = input("Please enter service principal name: ")
#Enter the secret key
secret = input("Please enter the secret key: ")

api_key = get_key(firewall_ip, firewall_admin, firewall_password)

result = set_key(firewall_ip, api_key, service_principal, secret)

print(result.text)