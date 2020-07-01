from azure.iot.device import IoTHubDeviceClient,Message
import json
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures

executor=ThreadPoolExecutor(10)
def threaded(fn):
    def wrapper(*args,**kwargs):
        return concurrent.futures.as_completed(executor.submit(fn,*args,**kwargs))
    return wrapper

dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
msg1=json.dumps(dict1)
msg2=json.dumps(dict2)

class test_send_msg:
    def __init__(self):
        connection_string="HostName=BarrysHub.azure-devices.net;DeviceId=MyDotnetDevice;SharedAccessKey=X55MFOdZ6+Qi/kmNXO8YeN8UauSyNQcwXifppPXNcrY="
        self.client=IoTHubDeviceClient.create_from_connection_string(connection_string)
        self.executor=ThreadPoolExecutor(10)

    def send_message(self,msg):
        print("start transmitting {}".format(msg))
        message=Message(msg)
        self.client.send_message(message)
        t=self.executor.submit(self.client.send_message,message)
        print("{} has been sent to iothub".format(msg))
        return t.result()
        
    @threaded
    def threaded_send_message(self,msg):
        print("start transmitting {}".format(msg))
        message=Message(msg)
        self.client.send_message(message)
        print("{} has been sent to iothub".format(msg))



t1=test_send_msg()

# t1.send_message(msg1)
# t1.send_message(msg2)

result1=t1.threaded_send_message(msg1)
result2=t1.threaded_send_message(msg2)
for result in result1:
    print(result)
for result in result2:
    print(result)
    