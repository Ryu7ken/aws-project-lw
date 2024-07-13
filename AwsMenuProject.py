import awsec2
import awss3
import awslog

print("Welcome to AWS Menu Program!")
print("Select which task you want to perform from the below Menu.\n")
print("\t\t\t  -------MENU-------\n")
print("\t\t         Launch EC2 Instance")
print("\t\t         Upload to S3 Bucket")
print("\t\t   Check CloudWatch Log for Lambda")
print("\t\t    Setup RHEL GUI in EC2 Instance")
print("\t\t Audio to Text Serverless Architecture")
print("\t\t      Connect MongoDB with Lambda")
print("\t\t     Serverless Bulk Email with SES")

choice = input("Tell me and I will do it! ")

if ("launch" in choice or "ec2" in choice or "instance" in choice):
    
    print("You have chosen to Launch EC2 Instance")
    InstanceType = input("Enter the Instance type: ")
    ImageId = input("Enter the ImageId of the AMI: ")
    MaxCount = int(input("Enter the Max number of Instance: "))
    MinCount = int(input("Enter the Min number of Instance: "))

    awsec2.osLaunch(InstanceType, ImageId, MaxCount, MinCount)

elif ("upload" in choice or "s3" in choice or "bucket" in choice):

    print("You have chosen to Upload to S3 Bucket")
    bucket_name = input("Enter the name of the S3 bucket: ")
    file_name = input("Enter the name of the file to upload: ")

    awss3.s3upload(bucket_name, file_name)

elif ("cloudwatch" in choice or "log" in choice):

    print("You have chosen to Check CloudWatch Log for Lambda")

    awslog()

elif ("rhel" in choice or "gui" in choice):

    print("You have chosen to Setup RHEL GUI in EC2 Instance\n")
    print("Please visit this URL for the Guide: ")

elif ("audio" in choice or "text" in choice):

    print("You have chosen to convert Audio to Text using Serverless Architecture\n")
    print("Please visit this URL for the Guide: ")

elif ("mongodb" in choice or "mongo" in choice):

    print("You have chosen to Connect MongoDB with Lambda\n")
    print("Please visit this URL for the Guide: ")

elif ("mongodb" in choice or "mongo" in choice):

    print("You have chosen to make Serverless Architecture for Bulk Email with SES\n")
    print("Please visit this URL for the Guide: ")

else:
    print("Please check your choice, it should relate to the MENU. Try again !")