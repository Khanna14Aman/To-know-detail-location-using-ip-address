import pygeoip

print("enter ip address to know details")
a=input()
gip = pygeoip.GeoIP("GeoLiteCity.dat")#downloaded and save in project record
res = gip.record_by_addr(a)
for key,val in res.items():
    print("%s : %s" %(key,val))
