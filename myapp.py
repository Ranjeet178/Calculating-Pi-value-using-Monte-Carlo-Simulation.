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
from operator import is_not
from functools import partial
import paramiko
from paramiko import SSHClient
from boto.manage.cmdshell import sshclient_from_instance

from concurrent.futures import ThreadPoolExecutor
results=[]
avg= None
values_estimates=[]
estimates_pi=[]
flat_list1=[]
# calling calculation functions

# EC2 Code
user_data = '''#!/bin/bash
sudo apt-get update &&
sudo apt-get install python3 &&
cd /home/ubuntu/ &&
git clone https://github.com/Ranjeet178/ec2 &&
cd ec2'''

def cost_cal(s):
    cost=[]
    
    print("sdhjsdhfks",s)
    
    for i in s:
        if "errorMessage" in i:
            print("Error from AWS")
        else:
            str1 = ''.join(i)
            json_acceptable_string = str1.replace("'", "\"")
            d = json.loads(json_acceptable_string)
            cost.append(d['elapsed_time'])
    return cost

def calculation_ec2(s):
    val=[]
   
    print("sdhjsdhfks",s)
    
    for i in s:
        if "errorMessage" in i:
            print("Error from AWS")
        else:
            str1 = ''.join(i)
            json_acceptable_string = str1.replace("'", "\"")
            d = json.loads(json_acceptable_string)
            val.append(d['values'])
    return val
def pi_values_from_ec2(host,shots,rate):
    shot=int(shots)
    rt=int(rate)
    
    print(host)
    user="ubuntu"
    key=paramiko.RSAKey.from_private_key_file("./Cloud_project.pem")
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(host, username=user,pkey=key)
    
    stdin, stdout, stderr = client.exec_command(f'cd /home/ubuntu/ec2/ && python3 pi_estimator.py {shot} {rt}')
    vals = stdout.readlines()[4]
    print ("output: ", vals)

    return vals
def create_ec2_instance():
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2",region_name='us-east-1',aws_access_key_id="AKIA26RDFRLR2HTXT3P5",
            aws_secret_access_key="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",)
        resource_ec2.run_instances(
            ImageId="ami-09e67e426f25ce0d7",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            UserData=user_data, 
            KeyName="Cloud_project",
            
        )
        print("end of request")
    except Exception as e:
        print(e)
def describe_ec2_instance():
    instance_ids = []
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        for i in resource_ec2.describe_instances()["Reservations"]:

            print(i["Instances"][0]["InstanceId"])
            instance_ids.append(i["Instances"][0]["InstanceId"])
        
        print("DONE")

        
        return instance_ids
    except Exception as e:
        print(e)

def stop_ec2_instance(instance_id):
    try:
        print ("Stopping EC2 instance")
        
        resource_ec2 = boto3.client("ec2")
        resource_ec2.stop_instances(InstanceIds=[instance_id])
        print(f"{instance_id} STOPPED")
    except Exception as e:
        print(e)

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))
            if instance.get("PublicIpAddress") == None:
                continue
            else:    
                return instance.get("PublicIpAddress")

def do_something_EC2(matching,shots,rate,no_resource):
    for i in range(no_resource):
       create_ec2_instance()
    time.sleep(80)
    instance_ids = describe_ec2_instance()
    print(instance_ids)

    instance_address = []

    for instance in instance_ids:
        
        address = get_public_ip(instance)
        instance_address.append(address)
    list=[]
    for i in instance_address:
        if i is not None:
            my_values = pi_values_from_ec2(i,shots,rate)
            print(my_values)
            list.append(my_values)
    '''ip_list=[]
    for i in instance_address:
        if i is not  None:
            ip_list.append(i)
    print("new Ip",ip_list)
    for i in range(len(ip_list)):
        my_values = pi_values_from_ec2(ip_list[i],shots,rate,i)
        print(my_values)'''
    
        
 


    for i in instance_ids:
        stop_ec2_instance(i)
    return list


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
    
 
 
    for result in results: 
        print("the resulstnd sdkj",result)
 
    
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
    if resource_type == 'EC2':
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
            actual_pi=math.pi
            # start = time.time() 
            flat_list=[]
            s=do_something_EC2(matching,shots,rate,int(no_resource))
            print("sssssssss",s)
            pi_values=calculation_ec2(s)
            print("actual piisis",pi_values)
            cost=cost_cal(s)
            #print("ECCC@^SGS",pi_values)
            flat = [item for sublist in pi_values for item in sublist]
            print("Faaaat",flat)
            for i in flat:  
                flat_list.append(i[0]/i[1]*4)
            print("EC@FLATLIST",flat_list)
            no_shorts=[]
            circle=[]
            for k in flat:
                no_shorts.append(k[1])
                circle.append(k[0])
            estimated=flat_list[-1]
            print("jcsydjskv",estimated)
            print("sdhksnddsfsdf",cost) 
            cost_val = cost[-1]
            #print("asjsadas",cost_val)
            print("sdhkhskdf",no_shorts)
            print("asdajsdjad",circle)
            no_shorts_1=no_shorts[-1]
 
            
            return render_template('ec2.html',no_resource=no_resource,shots=shots,rate=rate,s=s,actual_pi = actual_pi,matching=matching,flat_list=flat_list,no_shorts=no_shorts,no_shorts_1=no_shorts_1,circle=circle,estimated=estimated,cost_val=cost_val)
        else:
            return render_template('ranjeet.html') 
    else:
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
            print("flat_list******",type(flat_list))
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
    print("the results",result)
    return jsonify(result=result)

@app.route('/history')
def history():
    matching = request.form['Matching']
    print(matching)
    #print('matchings',matching)
    return render_template('history.html') 

if __name__ == '__main__':
    app.run(debug=True)


    
