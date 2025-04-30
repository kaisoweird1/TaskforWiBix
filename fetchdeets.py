import boto3
from botocore.exceptions import BotoCoreError, ClientError


STACK_NAME = "TaskForWibix"


def get_stack_resource_types(stack_name):

##   Retrieves all resource types from the specified CloudFormation stack
    cf = boto3.client('cloudformation')
    response = cf.describe_stack_resources(StackName=stack_name)
    return [res['ResourceType'] for res in response['StackResources']]


def extract_instance_name(tags):

   ## Extracts the Name tag from EC2 instance tags
    if tags:
        for tag in tags:
            if tag['Key'].lower() == 'name':
                return tag['Value']
    return "Unnamed"

def list_ec2_instances():
 
    ##Lists all EC2 instances with their ID, name, and state

    ec2 = boto3.client('ec2')
    print("\nEC2 Instances:")
    try:
        reservations = ec2.describe_instances()['Reservations']
        if not reservations:
            print("No EC2 instances found.")
            return

        for reservation in reservations:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                name = extract_instance_name(instance.get('Tags', []))
                print(f"- ID: {instance_id}, Name: {name}, State: {state}")
    except (BotoCoreError, ClientError) as e:
        print(f"Error fetching EC2 instances: {e}")


def list_s3_buckets():

    ##Lists all S3 buckets in the account

    s3 = boto3.client('s3')
    print("\nS3 Buckets:")
    try:
        buckets = s3.list_buckets().get('Buckets', [])
        if not buckets:
            print("No S3 buckets found.")
            return

        for bucket in buckets:
            print(f"- {bucket['Name']}")
    except (BotoCoreError, ClientError) as e:
        print(f"Error fetching S3 buckets: {e}")


def main():
    print(f"Fetching resources in stack: {STACK_NAME}")

    try:
        resource_types = get_stack_resource_types(STACK_NAME)
        print(f"Stack contains resources: {resource_types}")

        list_ec2_instances()
        list_s3_buckets()
    except (BotoCoreError, ClientError) as e:
        print(f"Error accessing CloudFormation stack: {e}")

if __name__ == "__main__":
    main()
