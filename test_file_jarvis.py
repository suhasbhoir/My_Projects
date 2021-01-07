import requests as rq
import json
url1 = 'http://www.showmyisp.com/'
# url = 'https://ipinfo.io/'
isp_req = rq.get(url1)
isp_data = isp_req.json()
# for k, v in isp_data.items():
#     print(f"{k} : - {v}")
print(isp_data)

# ip_is = isp_data['ip']
# tz = ['timezone']
# an = ['asn']
# isp_name = ['name']
# dm = ['domain']
# rout = ['route']
# isp_type = ['type']


# print(f"your ip address is {ip_is}")
# for k, v in isp_data.items():
#     print(f"{k} : - {v}")
