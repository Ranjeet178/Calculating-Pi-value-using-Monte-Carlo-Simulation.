import json
import math
import random
import time
   
def lambda_handler():
    start = time.time()
    # using d s q as input
    """print("Q: {},S: {},D: {} ".format(event["Q"],event["S"],event["D"],event["rid"]))
   D":2,
        "Q":1000,
        "S":100000
    number_shots = event["S"]
    r_r=event["Q"]
    
    rid=event["rid"]"""
    r_r=1000
    rid=0
    number_shots=100000
    print(type(number_shots))
    #number_shots=10000
    incircle_values = 0
    values=[]
    rr=[]
    inc=[]
    ns=[]
    for i in range(1, number_shots+1):
        random1 = random.uniform(-1.0, 1.0)
        random2 = random.uniform(-1.0, 1.0)
        if( ( random1*random1 + random2*random2 ) < 1 ):
            incircle_values += 1
        if i % r_r == 0:
            # value = 4.0 * incircle_values/i
            #values.append(value)
            print(incircle_values)
            values.append((incircle_values,i,rid))
           
   
    print(4.0 * incircle_values/number_shots)
    value = 4.0 * incircle_values/number_shots
    elapsed_time = time.time() - start
   
    # should return incircle and shot values
    return {
        'value': json.dumps(value),
        'values': json.dumps(values),
        "incircle_values": json.dumps(incircle_values),
        "number_shots": json.dumps(number_shots),
        "Resource_id": json.dumps(rid),
        "timeing": json.dumps(elapsed_time),
       
    }
    
lambda_handler()