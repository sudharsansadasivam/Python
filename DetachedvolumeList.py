#Script is to display all the detatched volumes in AWS 

import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
volumes = ec2.volumes.all() # If you want to list out all volumes
volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}]) # if you want to list out only attached volumes

for volume in volumes:
    print (volume.id)
