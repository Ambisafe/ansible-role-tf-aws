import sys
import json
import hashlib
import ipaddress
import itertools
import operator
from functools import reduce
import yaml
query = yaml.load(sys.stdin)
global_cidr = sys.argv[-1]
json_output = sys.argv[-2] == "json"
network = ipaddress.ip_network(global_cidr)

hashes = [ h for h in hashlib.blake2b((query['region'] + query['az'] + query['reachability']).encode(),
                    digest_size=query['digest_size'],
                    person=query['personalization'].encode()[-16:]).digest()]
available_subnet = itertools.cycle(network.subnets(new_prefix=query['subnet_size']))
for i in range(reduce(operator.mul, hashes[1:], hashes[0])):
    subnet = next(available_subnet)
if not json_output:
    print(subnet)
else:
    json.dumps({'value':subnet})