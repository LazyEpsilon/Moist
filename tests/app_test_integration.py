import pytest
import sys

from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse, MethodRequest
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
from mockito import when, mock, verify, args, arg_that

import app as sdm

def test_initialisation_of_client_does_not_throw_with_valid_string(connectionstring):
    mock_adc = mock(ADC)
    mock_relay = mock(GroveRelay)

    when(CounterFitConnection).init('127.0.0.1', 5000)

    manager = sdm.SoilDeviceManager(mock_adc, mock_relay)

    manager.initialise_client(connectionstring)