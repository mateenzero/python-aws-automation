#Import all the modules and libraries
import boto3

# Specify the instance type
instance_type = 't2.micro'

# Specify the AMI ID for the instance
ami_id = 'ami-0449c34f967dbf18a'

#Open management console
aws_management_console = boto3.session.Session(profile_name="syed")

#Open EC2 Console
ec2_console = aws_management_console.client('ec2')

#Start an instance with the selected image id and instance type
response = ec2_console.run_instances(
    ImageId=ami_id ,
    InstanceType=instance_type ,
    MaxCount=1,
    MinCount=1
)

# Get the instance ID of the newly created instance
instance_id = response['Instances'][0]['InstanceId']
print(f'Instance with ID {instance_id} created successfully.')