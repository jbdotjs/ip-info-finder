import requests

# API: https://rapidapi.com/jkosgei/api/free-ip-geolocation

querystring = {"api-key":"test"} # take your free api key from ipdata.co if you pass your testing limit

headers = {
    'x-rapidapi-host': "jkosgei-free-ip-geolocation-v1.p.rapidapi.com",
    'x-rapidapi-key': "ENTER YOUR RAPIDAPI KEY"
    }


def ip_details(ip):
	url = f"https://jkosgei-free-ip-geolocation-v1.p.rapidapi.com/{ip}"
	response = requests.request("GET", url, headers=headers, params=querystring)
	details=response.json()
	
	if response.status_code==200:
		try:
			print('IP: ', details['ip'])
			print('Country: ', details['country_name'])
			print('Region: ', details['region'])
			print('City: ', details['city'])
			print('Coordinates: lat=', details['latitude'],'long=',details['longitude'])
			print('ASN info:')
			print('ASN: ', details['asn']['asn'])
			print('Name: ', details['asn']['name'])
			print('domain: ', details['asn']['domain'])
			
		except KeyError:
			print('Try again, with "public" ip address')
	else:
		print(response.status_code)


ip=input('Enter public ip address: ')
ip_details(ip)
