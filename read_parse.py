import yaml
import pprint


def load_and_print_yaml(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    pprint.pprint(data)


def load_and_print_image(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    print(f'image: {data["spec"]["containers"][0]["image"]}')


def main():
    example_file = "./example-k8s-files/nginx.yaml"
    load_and_print_yaml(example_file)
    load_and_print_image(example_file)


if __name__ == "__main__":
    main()
