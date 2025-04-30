import boto3

# this function fetches the resources from the stack
def get_stack_resources(stack_name):
    cf = boto3.client('cloudformation')
    response = cf.describe_stack_resources(StackName=stack_name)
    return [res['ResourceType'] for res in response['StackResources']]

# this function extracts the names from the tags from EC2 instance tags
def get_instance_name(tags):
    if tags:
        for tag in tags:
            if tag['Key'] == 'Name':
                return tag['Value']
    return "No name specified"

# this function lists the ec2 instances and s3 buckets in the account
def list_inventory():
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    print("EC2 Instances:")
    reservations = ec2.describe_instances()['Reservations']
    if reservations:
        for res in reservations:
            for inst in res['Instances']:
                instance_id = inst['InstanceId']
                state = inst['State']['Name']
                name = get_instance_name(inst.get('Tags', []))
                print(f"Instance ID: {instance_id}, Name: {name}, State: {state}")
    else:
        print("No EC2 instances found.")

    print("S3 Buckets:")
    buckets = s3.list_buckets()['Buckets']
    if buckets:
        for bucket in buckets:
            print(f"Bucket Name: {bucket['Name']}")
    else:
        print("No S3 buckets found.")

def main():
    stack_name = "TaskForWixStack"  
    print(f"Fetching resources for stack: {stack_name}")

    try:
        resources = get_stack_resources(stack_name)
        print(f"Resources found in stack: {resources}")
        list_inventory()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
