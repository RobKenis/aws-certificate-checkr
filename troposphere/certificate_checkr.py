from troposphere import Template, Join, GetAtt, AWS_STACK_NAME, Ref, Parameter, constants
from troposphere.awslambda import Function, Code, Permission, Environment
from troposphere.events import Target, Rule
from troposphere.iam import Role, Policy
from troposphere.s3 import Bucket, LifecycleConfiguration, LifecycleRule

template = Template(Description='Lambda that described all certificates based on events')

# Parameters
event_cron = template.add_parameter(Parameter(
    "EventScheduleCron",
    Type=constants.STRING,
    Default="rate(1 day)",
))

# S3
bucket = template.add_resource(Bucket(
    "CheckResultsBucket",
    BucketName=Ref(AWS_STACK_NAME),
    LifecycleConfiguration=LifecycleConfiguration(
        Rules=[
            LifecycleRule(
                ExpirationInDays=7,
                Status='Enabled',
            ),
        ],
    ),
))

# Lambda
lambda_execution_role = template.add_resource(Role(
    "LambdaExecutionRole",
    Path="/",
    Policies=[Policy(
        PolicyName="root",
        PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [{
                "Action": ["logs:*"],
                "Resource": "arn:aws:logs:*:*:*",
                "Effect": "Allow",
            }, {
                "Effect": "Allow",
                "Action": ["acm:ListCertificates", "acm:DescribeCertificate"],
                "Resource": '*',
            }, {
                "Effect": "Allow",
                "Action": ["s3:PutObject"],
                "Resource": [
                    Join("", ["arn:aws:s3:::", Ref(bucket)]),
                    Join("", ["arn:aws:s3:::", Ref(bucket), "/results/*"]),
                ],
            }, {
                "Effect": "Allow",
                "Action": ["ec2:ListRegions"],
                "Resource": '*',
            }],
        })],
    AssumeRolePolicyDocument={"Version": "2012-10-17", "Statement": [
        {
            "Action": ["sts:AssumeRole"],
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com",
                ],
            },
        },
    ]},
))
with open("src/check_certificates.py", 'r') as input_file:
    check_function = template.add_resource(Function(
        "CheckFunction",
        Description="Describe certificates and store in S3.",
        Code=Code(
            ZipFile=input_file.read(),
        ),
        Handler="index.handler",
        Role=GetAtt(lambda_execution_role, "Arn"),
        Runtime='python3.6',
        Environment=Environment(
            Variables={
                "s3Bucket": Ref(bucket),
            },
        ),
    ))

# Cloudwatch
check_function_target = Target(
    "CheckFunctionTarget",
    Arn=GetAtt(check_function, 'Arn'),
    Id="CheckFunctionTarget"
)

trigger_rule = template.add_resource(Rule(
    "CheckTriggerLambdaRule",
    ScheduleExpression=Ref(event_cron),
    Description="Trigger lambda to describe ACM Certificates",
    State="ENABLED",
    Targets=[
        check_function_target
    ]
))

template.add_resource(Permission(
    "CheckFunctionTriggerLambdaPermission",
    Action="lambda:InvokeFunction",
    FunctionName=GetAtt(check_function, "Arn"),
    Principal="events.amazonaws.com",
    SourceArn=GetAtt(trigger_rule, "Arn")
))

f = open("output/certificate_checkr.json", "w")
f.write(template.to_json())
