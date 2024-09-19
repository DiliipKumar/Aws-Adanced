import boto3
from datetime import datetime

ec2_client = boto3.client('ec2')

instance_ids = [
    'i-035341e9e55d19aa4', 'i-06656ec45fbc5ace7', 'i-0edb25fb6537e42b3', 
    'i-08cfa297cb4be4142', 'i-0d0b6d11a82d8da31', 'i-00e6b5156a51be821', 
    'i-0f4f3144e948562fa', 'i-02a779dc7ccbae564', 'i-0aec119a2b2712965', 
    'i-079fccf733efe1d8e', 'i-007cf76b808be2b83', 'i-0496fca14fa3d8942', 
    'i-0912839b6780dce1b', 'i-07cd5c216e3186730'
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
