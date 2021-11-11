import pytest
import sys

from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse, MethodRequest
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
from mockito import when, mock, verify, args, arg_that

import soil_moisture_sensor.app as sdm

def test_app():
    pass

def test_initialisation_of_client():
    mock_client = mock(IoTHubDeviceClient)
    mock_adc = mock(ADC)
    mock_relay = mock(GroveRelay)

    when(CounterFitConnection).init('127.0.0.1', 5000)

    when(mock_client).connect()
    when(IoTHubDeviceClient)\
        .create_from_connection_string("<connection string>")\
        .thenReturn(mock_client)

    manager = sdm.SoilDeviceManager(mock_adc, mock_relay)

    manager.initialise_client("<connection string>")

    verify(mock_client).connect()