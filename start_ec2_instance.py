#Import all the modules and libraries
import boto3

#Open management console
aws_management_console = boto3.session.Session(profile_name="syed")

#Open EC2 Console
ec2_console = aws_management_console.client('ec2')

# Specify the instance ID you want to start/stop
# instance_id = 'your-instance-id'
instance_id = 'i-0d6ed5858237d9548'

# Start the instance
ec2_console.start_instances(InstanceIds=[instance_id])
print(f'Starting instance with ID {instance_id}')

# Wait for the instance to start
waiter = ec2_console.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])
print(f'Instance with ID {instance_id} is now running')

# Stop the instance
ec2_console.stop_instances(InstanceIds=[instance_id])
print(f'Stopping instance with ID {instance_id}')

# Wait for the instance to stop
waiter = ec2_console.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])
print(f'Instance with ID {instance_id} is now stopped')
