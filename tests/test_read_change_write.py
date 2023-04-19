import pytest
import yaml
from read_change_write import modify_yaml_file


@pytest.fixture(scope='module')
def yaml_data():
    with open('./example-k8s-files/encoder.yaml', 'r') as f:
        data = yaml.safe_load(f)
    yield data


def test_modify_yaml_file(yaml_data):
    log_level = 2
    cpu_request = '750m'
    modify_yaml_file('./example-k8s-files/encoder.yaml',
                     './example-k8s-files/encoder_changed.yaml',
                     log_level, cpu_request)

    with open('./example-k8s-files/encoder_changed.yaml', 'r') as f:
        modified_yaml_data = yaml.safe_load(f)

    assert modified_yaml_data != yaml_data

    containers = modified_yaml_data['spec']['template']['spec']['containers']

    assert containers[0]['env'][0]['value'] == str(log_level)
    assert containers[0]['resources']['requests']['cpu'] == str(cpu_request)
