#Import all the modules and libraries
import boto3

#Open management console
aws_management_console = boto3.session.Session(profile_name="default")

#Open EC2 Console
ec2_console = aws_management_console.client('ec2')

#Stop instances of the selected instance ids
response = ec2_console.terminate_instances(
    InstanceIds=[
        'i-0a572a9944709ba25',
        'i-0d0afc4055f059c38',
        'i-08a387420586038d3',
        'i-0579f6d943437bc39'
    ]
)