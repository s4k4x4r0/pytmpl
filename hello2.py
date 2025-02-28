import boto3


def main():
    print("Hello from pytmpl!")


def sum(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    main()

    sts_client = boto3.client("sts")

    # AWSアカウントのIDを取得
    response = sts_client.get_caller_identity()
    print("AWSアカウントID:", response["UserId"])
    aaa = sum(1, "a")
