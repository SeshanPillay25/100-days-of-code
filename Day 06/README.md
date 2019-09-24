### API documentation - http://ip-api.com/docs/
###  you can see you external ip using this Bash script :
#### read COUNTRY IP <<< $(wget -qO- http://ip-api.com/line/?fields=countryCode,query); echo $IP $COUNTRY

# IP tracing tool:

Execute by navigating to directory and starting the program 

using the following command:
perl iplocator.pl

Thereafter:
perl iplocator.pl + your target ip address

# Json API Response :
#### A successful request will return, by default, the following:
#### {
####   "status": "success",
####    "country": "COUNTRY",
####    "countryCode": "COUNTRY CODE",
####    "region": "REGION CODE",
####    "regionName": "REGION NAME",
####    "city": "CITY",
####    "zip": "ZIP CODE",
####   "lat": LATITUDE,
####    "lon": LONGITUDE,
####    "timezone": "TIME ZONE",
####    "isp": "ISP NAME",
####    "org": "ORGANIZATION NAME",
####    "as": "AS NUMBER / NAME",
####   "query": "IP ADDRESS USED FOR QUERY"
#### }