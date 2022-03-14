import boto3

# Document
s3BucketName = "leogamboa06a"
documentName = "matriculas.jpg"

# Amazon Textract client
textract = boto3.client('textract', 'eu-west-1')

boto3.set_stream_logger('botocore', level='DEBUG')

# Call Amazon Textract
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })

print(response)

# Print detected text
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033[94m' +  item["Text"] + '\033[0m')


