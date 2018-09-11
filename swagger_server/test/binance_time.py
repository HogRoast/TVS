import time
import requests

def get_server_time():
    r = requests.get('https://api.binance.com/api/v1/time', timeout=5)
    if r.status_code == requests.codes.ok:
        return r.json()
    return {'serverTime' : 0} 

def printBinance_Local_TimeDifference(): 
    for i in range(1, 10): 
        local_time1 = int(time.time() * 1000) 
        server_time = get_server_time() 
        diff1 = server_time['serverTime'] - local_time1 
        local_time2 = int(time.time() * 1000) 
        diff2 = local_time2 - server_time['serverTime'] 
        print("local1: %s server:%s local2: %s diff1:%s diff2:%s" % (local_time1, server_time['serverTime'], local_time2, diff1, diff2)) 
        time.sleep(2)

printBinance_Local_TimeDifference()
