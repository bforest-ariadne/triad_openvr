import triad_openvr
import time
import sys
from pythonosc import udp_client

client = udp_client.SimpleUDPClient('127.0.0.1', 8005)

v = triad_openvr.triad_openvr()
v.print_discovered_objects()

if len(sys.argv) == 1:
    interval = 1/250
elif len(sys.argv) == 2:
    interval = 1/float(sys.argv[1])
else:
    print("Invalid number of arguments")
    interval = False
    
if interval:
    while(True):
        start = time.time()
        txt = ""
        for idx, device_key in enumerate(v.devices):
            device = v.devices[device_key]
            pose_data = device.get_pose_quaternion()
            client.send_message(f"/pose_quat/{device_key}", pose_data)
            pose_euler_data = device.get_pose_euler()
            client.send_message(f"/pose_euler/{device_key}", pose_euler_data)
            pose_data_matrix = device.get_pose_matrix()
            pose_matrix_list = []
            for row in pose_data_matrix:
                for el in row:
                    pose_matrix_list.append(el)
            client.send_message(f"/pose_matrix/{device_key}", pose_matrix_list)
        pose_data = v.devices["tracking_reference_1"].get_pose_euler()
        # client.send_message("/tracker1", pose_data)
        # for each in pose_data:
        #     txt += "%.4f" % each
        #     txt += " "
        # print('matrix', pose_data_matrix)
        # print("\r" + pose_data_matrix, end="")
        sleep_time = interval-(time.time()-start)
        if sleep_time>0:
            time.sleep(sleep_time)