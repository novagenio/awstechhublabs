import boto3


# Instantiate Boto3 SDK:
client = boto3.client('comprehend', region_name='eu-west-1')

# Create a document classifier
create_response = client.create_document_classifier(
    InputDataConfig={
        'S3Uri': 'https://leogamboa06a.s3-eu-west-1.amazonaws.com/docclass/prueba.txt'
    },
    DataAccessRoleArn='arn:aws:iam::522218044253:user/leogamboa03',
    DocumentClassifierName='SampleCodeClassifier1',
    LanguageCode='es'
)
print("Create response: %s\n", create_response)

# Check the status of the classifier
describe_response = client.describe_document_classifier(
    DocumentClassifierArn=create_response['DocumentClassifierArn'])
print("Describe response: %s\n", describe_response)

# List all classifiers in account
list_response = client.list_document_classifiers()
print("List response: %s\n", list_response)

