import boto3
from datetime import datetime

# Specify the region
ec2_client = boto3.client('ec2', region_name='ap-southeast-1')

instance_ids = [
    "i-08a97143ae67d6ba9"
]



def get_instance_name(instance_id):
    """Retrieve the Name tag of the instance."""
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_info = response['Reservations'][0]['Instances'][0]
    
    # Get the Name tag if it exists
    tags = instance_info.get('Tags', [])
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    
    # Return a default name if no Name tag is found
    return f"instance-{instance_id}"

def create_amis():
    # Loop through each instance and create an AMI
    for instance_id in instance_ids:
        instance_name = get_instance_name(instance_id)  # Get the instance name
        ami_name = f"{instance_name}-ami-{datetime.now().strftime('%Y-%m-%d')}"
        
        try:
            # Create the AMI
            response = ec2_client.create_image(
                InstanceId=instance_id,
                Name=ami_name,
                NoReboot=True
            )
            ami_id = response['ImageId']
            print(f"AMI created for instance: {instance_id} ({instance_name}), AMI ID: {ami_id}")
        
        except Exception as e:
            print(f"Failed to create AMI for instance {instance_id}. Error: {str(e)}")
    
    print('AMI creation process completed.')

if __name__ == "__main__":
    create_amis()
