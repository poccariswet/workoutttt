from boto3 import Session
s3client = Session().client('s3')

def exists(bucket: str, key: str) -> bool:
    contents = s3client.list_objects(Prefix=key, Bucket=bucket).get("Contents")
    if contents:
        for content in contents:
            if content.get("Key") == key:
                return True
    return False

print(exists('jisseki-nichiji', 'jisseki_nichiji.csv'))
