import yaml


def modify_yaml_file(source_path, destination_path, log_level, cpu_request):
    with open(source_path, 'r') as input:
        yaml_data = yaml.safe_load(input)

    containers = yaml_data['spec']['template']['spec']['containers']

    # Modify the LOG_LEVEL
    containers[0]['env'][0]['value'] = str(log_level)
    # Modify the CPU request
    containers[0]['resources']['requests']['cpu'] = str(cpu_request)

    with open(destination_path, 'w') as output:
        yaml.safe_dump(yaml_data, output)


def main():
    source_path = './example-k8s-files/encoder.yaml'
    destination_path = './example-k8s-files/encoder_changed.yaml'

    log_level = 2
    cpu_request = '750m'
    modify_yaml_file(source_path, destination_path, log_level, cpu_request)


if __name__ == '__main__':
    main()
