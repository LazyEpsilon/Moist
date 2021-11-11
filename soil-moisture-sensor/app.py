import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
import os
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
from counterfit_connection import CounterFitConnection

class SoilDeviceManager:
    def __init__(self, adc: ADC, relay: GroveRelay):
        self.adc = adc
        self.relay = relay
        self.device_client = None

    def initialise_client(self, connection_string: str):
        self.device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)
        print('Connecting')
        self.device_client.connect()
        print('Connected')
        self.device_client.on_method_request_received = self.handle_method_request
        CounterFitConnection.init('127.0.0.1', 5000)

    def handle_method_request(self, request):
        print("Direct method received - ", request.name)

        if request.name == "relay_on":
            self.relay.on()
        elif request.name == "relay_off":
            self.relay.off()

        method_response = MethodResponse.create_from_method_request(request, 200)
        self.device_client.send_method_response(method_response)

    def report_reading(self):
        soil_moisture = self.adc.read(0)
        print("Soil moisture:", soil_moisture)

        message = Message(json.dumps({'soil_moisture': soil_moisture}))
        self.device_client.send_message(message)

if __name__ == "__main__":

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\iot_config.json') as f: 
        conf = json.load(f)
        manager = SoilDeviceManager(ADC(), GroveRelay(5))
        manager.initialise_client(conf["iot_url"])

    while True:
        manager.report_reading()
        time.sleep(10)