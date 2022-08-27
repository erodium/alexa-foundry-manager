import aws_cdk.aws_lambda_python_alpha as pylambda

from aws_cdk import (
    CfnOutput,
    Duration,
    Stack,
    aws_iam as iam
)
from aws_cdk.aws_lambda import Runtime
from constructs import Construct


class FoundrySkillStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        lambda_function = pylambda.PythonFunction(
            self,
            "Function",
            entry="/home/liam/PycharmProjects/foundry-alexa/lambdas",
            runtime=Runtime.PYTHON_3_9,
            index="foundry_handler.py",
            timeout=Duration.seconds(7)
        )

        instance_policy = iam.PolicyStatement(
            actions=[
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            resources=[Stack.of(self).format_arn(
                partition='aws',
                service='ec2',
                resource="instance",
                resource_name="i-0b77ab0785378a0eb"
            )]
        )
        describe_instances_policy = iam.PolicyStatement(
            actions=[
                "ec2:DescribeInstanceStatus"
            ],
            resources=["*"]
        )
        lambda_function.add_to_role_policy(instance_policy)
        lambda_function.add_to_role_policy(describe_instances_policy)

        CfnOutput(self, "oLambdaArn", value=lambda_function.function_arn)
