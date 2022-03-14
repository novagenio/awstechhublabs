from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "j01"
job_uri = "https://leogamboa06a.s3-eu-west-1.amazonaws.com/test_transcribe.mp3"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='es-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
