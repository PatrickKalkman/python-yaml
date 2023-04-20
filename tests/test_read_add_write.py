import os
import yaml
from read_add_write import read_yaml_file, add_resources_section
from read_add_write import write_yaml_file
import pytest


@pytest.fixture(scope='module')
def test_add_resources_section(tmpdir):
    source_file = './example-k8s-files/encoder_without_requests.yaml'
    destination_file = os.path.join(tmpdir,
                                    './example-k8s-files/result.yaml')
    cpu_request = '200m'
    memory_request = '512Mi'
    cpu_limit = '500m'
    memory_limit = '1Gi'

    yaml_data = read_yaml_file(source_file)
    modified_data = add_resources_section(yaml_data, cpu_request,
                                          memory_request, cpu_limit,
                                          memory_limit)
    write_yaml_file(destination_file, modified_data)

    with open(destination_file, 'r') as file:
        result = yaml.safe_load(file)

    containers = result["spec"]["template"]["spec"]["containers"]

    resources = containers[0]["resources"]

    assert resources["requests"]["cpu"] == cpu_request
    assert resources["requests"]["memory"] == memory_request
    assert resources["limits"]["cpu"] == cpu_limit
    assert resources["limits"]["memory"] == memory_limit
