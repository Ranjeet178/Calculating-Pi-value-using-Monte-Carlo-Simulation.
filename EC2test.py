# Lets create EC2 instances using Python BOTO3
import boto3
import botocore
import paramiko
# from boto.manage.cmdshell import sshclient_from_instance
 
user_data = '''#!/bin/bash
echo "import json
import math 
import random
import time
import flask
from flask import request, jsonify
 
app = flask.Flask(__name__)
 

@app.route('/', methods=['GET','POST'])
def api_all():
    start = time.time()
    estimate = []
    values=[]    
    shots = int(event[S])
    incircle = 0
    for i in range(1, shots+1):
        random1 = random.uniform(-1.0, 1.0)  
        random2 = random.uniform(-1.0, 1.0)  
        if( ( random1*random1 + random2*random2 ) < 1 ):
            incircle += 1
        if i % int(event[Q]) == 0:
            values.append([incircle,i])
    elapsed_time = time.time() - start
app.run(debug=True)" >> myfile.py && python myfile.py
'''

def create_ec2_instance():
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2",region_name='us-east-1',aws_access_key_id='AKIAZAYGC72ATPOYQTS4',
    aws_secret_access_key='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')
        resource_ec2.run_instances(
            ImageId="ami-0d5eff06f840b45e9",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            UserData=user_data,
            KeyName="coursework_1",
           # security_groups='coursework_1'
        )
    except Exception as e:
        print(e)

def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
            
"""
# rebooting the instance
def reboot_ec2_instance():
    try:
        print ("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

#stoping the instance
def stop_ec2_instance():
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)
"""

def terminate_ec2_instance():
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2",region_name='us-east-1',aws_access_key_id='AKIAZAYGC72ATPOYQTS4',
    aws_secret_access_key='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')
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


create_ec2_instance()


#instance_id=describe_ec2_instance()
#print(instance_id)
#public_ip=get_public_ip(instance_id)
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
terminate_ec2_instance()

"""def execute_commands_on_linux_instances(client, commands, instance_ids):
    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

ssm_client = boto3.client("ec2", region_name="us-east-1",aws_access_key_id='AKIAZAYGC72ATPOYQTS4',
    aws_secret_access_key='u0ivJPydJQ/arekvzyvkbvdWaGI90prQZMg9uQAX') # Need your credentials here
commands = ['echo "hello world"']
execute_commands_on_linux_instances(ssm_client, commands, instance_id)"""













"""

key = paramiko.RSAKey.from_private_key_file(path/to/mykey.pem)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command(cmd)
    print stdout.read()

    # close the client connection once the job is done
    client.close()
    break

except Exception, e:
    print e
    """