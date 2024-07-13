''' This module can be used to Launch instances or Start the instances or Stop the instances or Terminate the instances. 
And also Check for all the instances and their currnet status.'''

import boto3

myec2 = boto3.resource("ec2")

def osLaunch(type, imageid, max, min):
    '''Takes 4 arguments, i.e., 
    type - The Instance type as string, 
    imageid - The ImageId of the AMI as string, 
    max - The Max number of instances to launch, 
    min - The Min number of instances to launch.
    '''
    myec2.create_instances( 
        InstanceType= type, 
        ImageId= imageid,
        MaxCount= max,
        MinCount= min,
    )

def osStart(id):
    ''' Takes the InstanceId of the instance as string. For more than one Id provide as comma seperated.'''
    myec2.instances.filter(
        InstanceIds=[id],
    ).start()

def osStop(id):
    ''' Takes the InstanceId of the instance as string. For more than one Id provide as comma seperated.'''
    myec2.instances.filter(
        InstanceIds=[id],
    ).stop()

def osTerminate(id):
    ''' Takes the InstanceId of the instance as string. For more than one Id provide as comma seperated.'''
    myec2.instances.filter(
        InstanceIds=[id],
    ).terminate()

def osCheck():
    '''Just call the funtion to get all the instances wiht details.'''
    for instance in myec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )