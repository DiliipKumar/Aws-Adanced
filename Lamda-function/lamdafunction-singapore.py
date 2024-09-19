import boto3
from datetime import datetime

ec2_client = boto3.client('ec2')

instance_ids = [
    'i-0eb8f4f17ddf60a4a', 'i-061e867118ef75084', 'i-0ea6ed06281722a85', 
    'i-0d83751337570222e', 'i-05a06f17499e747da', 'i-08a97143ae67d6ba4', 
    'i-02ed488e1a2486b70', 'i-0267184932e353b23', 'i-04d230fe170f00ae1', 
    'i-049331319df6117e5', 'i-0908aa3d8f46fdc81', 'i-08020e7b9dfc5adcf', 
    'i-0d667335a9f531cab', 'i-06590e2acb3fbb5ee', 'i-080774fcf08d5d310', 
    'i-036657eb7db3261d1', 'i-08b8e6ec3cbdad14f', 'i-0a873247a4f4f91fb', 
    'i-0fdb981e9b7f959da', 'i-0bd55a6fabc59f0a7'
]

def lambda_handler(event, context):
    # Loop through each instance and create an AMI
    for instance_id in instance_ids:
        ami_name = f"ami-{instance_id}-{datetime.now().strftime('%Y-%m-%d')}"
        
        try:
            # Create the AMI
            response = ec2_client.create_image(
                InstanceId=instance_id,
                Name=ami_name,
                NoReboot=True
            )
            ami_id = response['ImageId']
            print(f"AMI created for instance: {instance_id}, AMI ID: {ami_id}")
        
        except Exception as e:
            print(f"Failed to create AMI for instance {instance_id}. Error: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': 'AMI creation process completed.'
    }
