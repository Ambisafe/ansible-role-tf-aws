import sys
import json
import boto3
import yaml
query = yaml.load(sys.stdin)
client = boto3.client('ec2', region_name=query['region'])
filters = [{
    "Name": "isDefault",
    "Values": [str(query['default']).lower()]
}]
if not query['default']:
    filters.append({
        "Name": "cidr",
        "Values": [query['cidr']]
        })
for vpc in client.describe_vpcs(Filters=filters)['Vpcs']:
    print( vpc['VpcId'])
    sys.exit(0)
print('null')