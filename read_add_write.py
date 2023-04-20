import yaml


def read_yaml_file(filename):
    with open(filename, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data


def add_resources_section(yaml_data, cpu_request, memory_request, cpu_limit,
                          memory_limit):
    containers = yaml_data["spec"]["template"]["spec"]["containers"]
    for container in containers:
        container["resources"] = {
            "requests": {
                "cpu": cpu_request,
                "memory": memory_request
            },
            "limits": {
                "cpu": cpu_limit,
                "memory": memory_limit
            }
        }
    return yaml_data


def write_yaml_file(filename, yaml_data):
    with open(filename, 'w') as file:
        yaml.safe_dump(yaml_data, file)


def main():
    source_file = './example-k8s-files/encoder_without_requests.yaml'
    destination_file = './example-k8s-files/encoder_with_requests_limits.yaml'
    cpu_request = '200m'
    memory_request = '512Mi'
    cpu_limit = '500m'
    memory_limit = '1Gi'

    yaml_data = read_yaml_file(source_file)
    modified_data = add_resources_section(yaml_data, cpu_request,
                                          memory_request, cpu_limit,
                                          memory_limit)
    write_yaml_file(destination_file, modified_data)


if __name__ == "__main__":
    main()
