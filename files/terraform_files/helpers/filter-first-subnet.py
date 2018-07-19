import sys
import json
import boto3
import yaml

query = yaml.load(sys.stdin)
vpc_id, default_cidr = sys.argv[-2:]

client = boto3.client('ec2', region_name=query['region'])
ret = "null"

filters = [
{
    "Name": "vpc-id",
    "Values": [vpc_id]
},
{
    "Name": "availabilityZone",
    "Values": [query['region'] + query['az']]
}
]

if query['subnet'] is not None:
    filters.append({
        "Name": "cidrBlock",
        "Values": [query['subnet']]
        })
else:
    filters.append({
        "Name": "cidrBlock",
        "Values": [default_cidr]
        })


for subnet in client.describe_subnets(Filters=filters)['Subnets']:
    if subnet['MapPublicIpOnLaunch'] == query['reachability'].startswith('public'):
        ret = subnet['SubnetId']
        break
print(ret)