import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


def set_key(firewall_ip, api_key, sp_name, sp_key):
    xpathvalue = '/config/devices/entry[@name="localhost.localdomain"]/plugins/azure/service-principal/entry[@name="%s"]' % sp_name
    elementvalue = '<client-secret>%s</client-secret>' % sp_key

    values = {'type': 'config', 'action': 'set', 'key': api_key, 'xpath': xpathvalue, 'element': elementvalue}

    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    return response