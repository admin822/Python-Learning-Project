from azure.iot.device import IoTHubDeviceClient
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures
import os
import json
import time

executor=ThreadPoolExecutor(10)
def concurrents(fn):
    def wrapper(*args,**kwargs):
        return executor.submit(fn,*args,**kwargs)
    return wrapper

class blob_send:
    def __init__(self):
        #self.executor=ThreadPoolExecutor(10)
        connection_string="HostName=BarrysHub.azure-devices.net;DeviceId=MyDotnetDevice;SharedAccessKey=X55MFOdZ6+Qi/kmNXO8YeN8UauSyNQcwXifppPXNcrY="
        self.client=IoTHubDeviceClient.create_from_connection_string(connection_string)
        self.threads=[]
        #pass

    def _store_blob(self,blob_info, file_name):
        try:
            sas_url = "https://{}/{}/{}{}".format(
                blob_info["hostName"],
                blob_info["containerName"],
                blob_info["blobName"],
                blob_info["sasToken"]
            )


            # Upload the specified file
            with BlobClient.from_blob_url(sas_url) as blob_client:
                with open(file_name, "rb") as f:
                    try:
                        result = blob_client.upload_blob(f, overwrite=True)
                    except Exception:
                        print("errors met")
                        blob_client.close()
                    blob_client.close()
                    return (True, result)

        except FileNotFoundError as ex:
            # catch file not found and add an HTTP status code to return in notification to IoT Hub
            ex.status_code = 404
            return (False, ex)

        except AzureError as ex:
            # catch Azure errors that might result from the upload operation
            return (False, ex)

    @concurrents
    def _send_csv_file(self,filename):
        print("start transmitting {}".format(filename))
        # connection_string="HostName=BarrysHub.azure-devices.net;DeviceId=MyDotnetDevice;SharedAccessKey=X55MFOdZ6+Qi/kmNXO8YeN8UauSyNQcwXifppPXNcrY="
        # client=IoTHubDeviceClient.create_from_connection_string(connection_string)
        blob_name=os.path.basename(filename)
        blob_info=self.client.get_storage_info_for_blob(blob_name)
        success,result=self._store_blob(blob_info,filename)
        if(success):
            print("{} has been sent".format(filename))
        else:
            print("transmission of {} has failed".format(filename))
        return result

    def send_csv_file(self,filename):
        self.threads.append(self._send_csv_file(filename))
    
    def wait_until_done(self,filename):
        self.threads.append(self.send_csv_file(filename))
        results=concurrent.futures.as_completed(self.threads)
        for r in results:
            print(r.result())

    
    def untreaded_send_csv_file(self,filename):
        print("start transmitting {}".format(filename))
        # connection_string="HostName=BarrysHub.azure-devices.net;DeviceId=MyDotnetDevice;SharedAccessKey=X55MFOdZ6+Qi/kmNXO8YeN8UauSyNQcwXifppPXNcrY="
        # client=IoTHubDeviceClient.create_from_connection_string(connection_string)
        blob_name=os.path.basename(filename)
        blob_info=self.client.get_storage_info_for_blob(blob_name)
        success,result=self._store_blob(blob_info,filename)
        if(success):
            print("{} has been sent".format(filename))
        else:
            print("transmission of {} has failed".format(filename))
        return result

    def destroty(self):
        self.client.disconnect()
    # def concurrent_send_to_blob(self,filename):
    #     t=self.executor.submit(self.send_csv_file,filename)
    #     result=t.result()
    #     return result


    def terminate(self):
        for t in self.threads:
            while(not t.done()):
                pass

counter=0
t1=blob_send()
while(True):
    try:
        if(counter==0):
            filenames=['ping.txt','ping.csv','secondping.txt']
            start_time=time.time()
            for filename in filenames:
                t1.send_csv_file(filename)
            print("this is threaded time:{}".format(time.time()-start_time))
            counter+=1
        else:
            pass
    except KeyboardInterrupt:
        break
print("all is finished")




# t1=blob_send()
# start_time=time.time()
# filenames=['ping.txt','ping.csv']

# start_time=time.time()
# for filename in filenames:
#     r=t1.untreaded_send_csv_file(filename)
#     print(r)
# print("this is untreaded time:{}".format(time.time()-start_time))

# start_time=time.time()
# for filename in filenames:
#     r=t1.wait_until_done(filename)
# print("this is threaded time:{}".format(time.time()-start_time))


# while(True):
#     try:
#         pass
#     except KeyboardInterrupt:
#         break




# def store_blob(blob_info, file_name):
#         try:
#             sas_url = "https://{}/{}/{}{}".format(
#                 blob_info["hostName"],
#                 blob_info["containerName"],
#                 blob_info["blobName"],
#                 blob_info["sasToken"]
#             )


#             # Upload the specified file
#             with BlobClient.from_blob_url(sas_url) as blob_client:
#                 with open(file_name, "rb") as f:
#                     result = blob_client.upload_blob(f, overwrite=True)
#                     blob_client.close()
#                     return (True, result)

#         except FileNotFoundError as ex:
#             # catch file not found and add an HTTP status code to return in notification to IoT Hub
#             ex.status_code = 404
#             return (False, ex)

#         except AzureError as ex:
#             # catch Azure errors that might result from the upload operation
#             return (False, ex)

# connection_string="HostName=BarrysHub.azure-devices.net;DeviceId=MyDotnetDevice;SharedAccessKey=X55MFOdZ6+Qi/kmNXO8YeN8UauSyNQcwXifppPXNcrY="
# client=IoTHubDeviceClient.create_from_connection_string(connection_string)
# filename='ping.csv'
# blob_info=client.get_storage_info_for_blob(os.path.basename(filename))
# store_blob(blob_info,filename)
