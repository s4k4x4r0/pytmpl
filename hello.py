import boto3


def main():
    print("Hello from pytmpl!")


if __name__ == "__main__":
    main()

    client = boto3.client("sts")

    # Retrieves all regions/endpoints that work with EC2
    response = client.get_caller_identity()
    print("Response:", response["UserId"])
