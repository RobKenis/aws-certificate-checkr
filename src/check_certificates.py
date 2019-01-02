import json
import os
from datetime import datetime

import boto3

regions = boto3.client('ec2').describe_regions()
s3 = boto3.client('s3')

bucket = os.environ['s3Bucket']


def handler(event, context):
    for region in regions['Regions']:
        check_certificates(region['RegionName'])


def check_certificates(region):
    client = boto3.client('acm', region_name=region)
    certificates = list(map(lambda described: {'CertificateArn': described['Certificate']['CertificateArn'],
                                               'DomainName': described['Certificate']['DomainName'],
                                               'InUseBy': described['Certificate']['InUseBy'],
                                               'InUse': len(described['Certificate']['InUseBy']) > 0, },
                            list(map(lambda cert: client.describe_certificate(CertificateArn=cert['CertificateArn']),
                                     client.list_certificates()['CertificateSummaryList']))))
    upload_to_s3(region, certificates, _result_key(region), 'bucket-owner-full-control')
    upload_to_s3(region, certificates, "results/latest/{region}.json".format(region=region), 'public-read')


def upload_to_s3(region, certificates, key, access_control):
    s3.put_object(
        ACL=access_control,
        Body=(bytes(json.dumps(certificates, indent=2).encode('UTF-8'))),
        Bucket=bucket,
        Key=key,
        StorageClass='ONEZONE_IA',
    )
    print("Results for {region} stored in {bucket} at {path}".format(region=region, bucket=bucket, path=key))


def _result_key(region):
    return "results/{year}/{month}/{day}/{region}.json".format(
        year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, region=region)
