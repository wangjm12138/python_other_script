

import dns.resolver


my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [192.168.140.5]
try:
    res=my_resolver.query("www.google.com")
except Exception as e:
    print('error')

for i  in res.response.answer:
    for j in i.items:
        print(j)
