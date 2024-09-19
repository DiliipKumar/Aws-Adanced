import boto3
from datetime import datetime

ec2_client = boto3.client('ec2')

instance_ids = [
    'i-035341a9e55d19aa4', 'i-06656ac45fbc5ace7', 'i-0edb25fb6537a42b3', 
    //Random instance-id
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
