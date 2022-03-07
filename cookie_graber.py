#!/usr/bin/env python
import requests
import sys
import bgp
# Making a get request
session = requests.Session()
response = session.get('http://google.com')

with open('cookies.txt', 'w') as f:
    print((session.cookies.get_dict()), file=f)
[
    {'name': c.name, 'value': c.value, 'domain': c.domain, 'path': c.path}
    for c in session.cookies
]
{'PREF': 'ID=5514c728c9215a9a:FF=0:TM=1406958091:LM=1406958091:S=KfAG0U9jYhrB0XNf', 'NID': '67=TVMYiq2wLMNvJi5SiaONeIQVNqxSc2RAwVrCnuYgTQYAHIZAGESHHPL0xsyM9EMpluLDQgaj3db_V37NjvshV-eoQdA8u43M8UwHMqZdL-S2gjho8j0-Fe1XuH5wYr9v'}

# printing request cookies
exit()