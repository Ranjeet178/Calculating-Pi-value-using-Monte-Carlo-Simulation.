from flask import Flask, render_template,redirect,url_for,request,jsonify
import json,random
app=Flask(__name__)

import math
import random
import time
import json
import http.client
import statistics
import boto3
import botocore
import paramiko
from concurrent.futures import ThreadPoolExecutor# creates a list of values as long as the number of things we want# in parallel so we could associate an ID to each
results=[]
avg= None
values_estimates=[]
estimates_pi=[]
flat_list1=[]
# calling calculation functions

def ec2(matching,shots,rate,no_resource):
    # Lets create EC2 instances using Python BOTO3

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
def calculation(s):
    
    val=[]
    print("cal_reached",s)
    for i in s:
        if "errorMessage" in i:
            print("Error from AWS")
        else:
            val.append(i['values'])
        # resource_id.append(i['Resource_id'])
        # incircle_values.append(i['incircle_values'])
        # number_shots.append(i['number_shots'])
    #print(val)     
    #print(resource_id) 
    #print(incircle_values) 
    #print(number_shots)
    #val = map(float, val) 
    #avg=statistics.mean(val) 
    print("Value******",val)
    return val


    

def getpage(id,matching,shots,rate):
    try: 
        host = "07z3tk03ye.execute-api.us-east-1.amazonaws.com" 
        c = http.client.HTTPSConnection(host) 
        data = {
        "rid":id,
        "D":matching,
        "Q":rate,
        "S":shots
        } 
        c.request("POST", "/default/course_work", json.dumps(data)) 
        response = c.getresponse() 
        print("AWS response",response)
        data = json.loads(response.read().decode('utf-8'))
        #data.update({"Resource_id":id})
        print( data)
        return data 
    except IOError: 
        print( 'Failed to open ', host ) # Is the Lambda address correct? 
        print(data+" from "+str(id)) # May expose threads as completing in a different order 
        return "page "+str(id)
 
def getpages(matching,shots,rate,runs): 
    with ThreadPoolExecutor() as executor: 
        #results=executor.map(getpage, runs)
        
        
        for i in runs:
            data=getpage(i,int(matching),int(shots),int(rate))
            print("getpage_data",data)
            results.append(data)
    return results
def do_something(matching,shots,rate,no_resource):
    parallel = no_resource
    runs=[value for value in range(parallel)]
    print("there")
    getpages(matching,shots,rate,runs)
    
 
    #if __name__ == '__main__':
        # start = time.time() 
        # results = getpages() 
    
    for result in results: # uncomment to see results in ID order # 
        print(result)
 
    # print( "Elapsed Time: ", time.time() - start)
    return results
 

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        resource_type = request.form['Function']
        print(resource_type)
        no_resource= request.form['Services']
        print(no_resource)
        return redirect(url_for('ranjeet',resource_type=resource_type,no_resource=no_resource))
    else:
        return render_template('index.html') 
    
@app.route('/<resource_type>/<no_resource>',methods=['GET','POST'])
def ranjeet(resource_type,no_resource):
    print("here",resource_type,no_resource)
    if request.method == 'POST':
        matching = request.form['Matching']
        print(matching)
        shots= request.form['shots']
        shot=request.form['shots']
        print(shot)
        shots=int(shots)/int(no_resource)
        print(shots)
        rate= request.form['rate']
        print(rate)
        # start = time.time() 
        flat_list=[]
        s=do_something(matching,shots,rate,int(no_resource))
        
        print("Ranjeet_s",s)
        
        pi_values=calculation(s)
        
        print("pi average value",pi_values)
        for i in pi_values:
            values_estimates.append(json.loads(i))
        print("list of pi values",values_estimates)
        flat = [item for sublist in values_estimates for item in sublist]
        for i in flat:  
            flat_list1.append(i[0]/i[1]*4)
        no_shorts=[]
        circle=[]
        reso_id=[]
        
        for k in flat:
            no_shorts.append(k[1])
            circle.append(k[0])
            reso_id.append(k[2])
        print("%$$%^^^%^^",no_shorts)
        looobj = {
            "no_short" : no_shorts,
            "en_circle" : circle,
            "reso_id" : reso_id
                }
        
        print("SSSS*****SSS" , looobj)
        flat_list=[]
        for i in flat_list1:
            if i!=0.0:
                flat_list.append(i)
        print("flat_list******",flat_list)
        actual_pi=math.pi
        print('ap',actual_pi)
        sortlen1=len(no_shorts)
        print('sortleeee',sortlen1)    
        #return redirect(url_for('graph',resource_type=resource_type,no_resource=no_resource,matching=matching,shots=shots,rate=rate))
        return render_template('graph.html',no_resource=no_resource,shots=shots,rate=rate,s=s,actual_pi = actual_pi,matching=matching,flat_list=flat_list,no_shorts=no_shorts,circle=circle,reso_id=reso_id,looobj=looobj,sortlen1 = sortlen1,shot=shot)
    else:
        return render_template('ranjeet.html') 

@app.route('/graph')
def graph():
    return render_template('graph.html') 
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    
    #word = request.    gs.get('text1')
    combine = do_something(text1)
    
    #console.log(combine)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    print(result)
    return jsonify(result=result)

@app.route('/history')
def history():
    matching = request.form['Matching']
    print(matching)
    #print('matchings',matching)
    return render_template('history.html') 

if __name__ == '__main__':
    app.run(debug=True)


    
