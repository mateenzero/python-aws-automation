# Import all the modules and Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="syed")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Get a list of all running instances
response = ec2_console.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")