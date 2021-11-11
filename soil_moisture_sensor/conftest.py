def pytest_addoption(parser):
    parser.addoption("--connectionstring", action="store", default="bad string")

def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.connectionstring
    if 'connectionstring' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("connectionstring", [option_value])