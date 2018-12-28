import boto3

regions = boto3.client('ec2').describe_regions()


def handler(event, context):
    for region in regions['Regions']:
        check_certificates(region['RegionName'])


def check_certificates(region):
    client = boto3.client('acm')
    certificates = list(map(lambda described: {'CertificateArn': described['Certificate']['CertificateArn'],
                                               'DomainName': described['Certificate']['DomainName'],
                                               'InUseBy': described['Certificate']['InUseBy'],
                                               'InUse': len(described['Certificate']['InUseBy']) > 0, },
                            list(map(lambda cert: client.describe_certificate(CertificateArn=cert['CertificateArn']),
                                     client.list_certificates()['CertificateSummaryList']))))
    upload_to_s3(region, certificates)


def upload_to_s3(region, certificates):
    print('----------------------------------------------------')
    print(region)
    print(certificates)


handler(None, None)
