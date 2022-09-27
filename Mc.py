import canopen
import paho.mqtt.client as mqtt
from Lift import Lift


obj = Lift(1.5, 1, 2)
obj.Display()

network = canopen.Network()
network.connect(channel='10.150.1.240', bustype='socketcan')

"""
canopen.Network.send_message(self=, can_id=, ):
    if not self.bus:
                raise RuntimeError("Not connected to CAN bus")
            msg = can.Message(is_extended_id=can_id > 0x7FF,
                              arbitration_id=can_id,
                              data=data,
                              is_remote_frame=remote)
            with self.send_lock:
                self.bus.send(msg)
            self.check()
"""
str


#print(canopen.network.MessageListener(network='10.150.1.240'))


"""
#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('testtopic/#')

# Message receiving callback
def on_message(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.connect('broker.emqx.io', 1883, 60)
# Publish a message
client.publish('emqtt',payload='Hello World',qos=0)

#for x in range(10):
#    print(client)

client.loop_forever()


def send_one():

    with can.interface.Bus() as bus:
        msg = can.Message(
            arbitration_id=0x001303, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True
        )

        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")
"""
