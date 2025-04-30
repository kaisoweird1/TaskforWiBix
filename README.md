#  Task For Wibix

This repo includes:
- A CloudFormation template to create a read-only IAM role.
- A Python script to fetch AWS inventory (EC2 instances and S3 buckets for now ) using the Stack Name.
- A launch-ready CloudFormation stack URL.
- Steps used for the creation of all this

---

##  Files

- `RAT.yaml` – CloudFormation template (stored in S3)
- `fetchdeets.py` – Python script to fetch inventory using default AWS credentials
- `README.md` – This documentation

---

# Steps used for this Task
### Step 1: Creation of the yaml file
### Step 2: Upload the yaml file to a bucket and copy the object URL
  1. Open the AWS Console and go to the S3 Dashboard: https://s3.console.aws.amazon.com/s3/home
     
  2. Click `Create bucket`
     
  3. Go into the bucket and click Upload.
     
  4. Upload your .yaml file.
     
  5. After upload, click on the file and copy the `Object URL`
     
### Step 3: Deploy the CloudFormation Stack

1. Use this link to deploy the stack in AWS:
   
 https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/create/review?templateURL=https://bucketforrat.s3.us-west-1.amazonaws.com/RAT.yaml&stackName=TaskForWibix

2. Check the acknowledgment box and click **Create Stack**.

This will create an IAM Role named `TaskForWibix` with read-only access to EC2, S3, and other AWS services.

---

##  Run the Python Script

1. Save this python file on your device.
2. Install the requirements using the following command:
  ```bash 
   pip install -r requirements.txt
  ```

3. Run it inside a terminal of your choice by using the following command :

```bash
python3 fetchdeets.py
```


