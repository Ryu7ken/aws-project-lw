##Connecting MongoDB Atlas using AWS Lambda##

###Below is the step by step guide to setup this architecture:###

***Step-1:*** Login to your MongoDB Atlas account. Under the "DEPLOYMENT" section click on "Database" and then click on the button "Build a Cluster".
![cluster](/assets/images/cluster.png)

***Step-2:*** Select the "MO" free tier and give your cluster a name. Then select your AWS region and click the button "Create Deployment".
![cluster2](/assets/images/cluster2.png)
![cluster3](/assets/images/cluster3.png)

***Step-3:*** Now you will be shown a screen where they will give you a pre-created Username and Password which you can change according to your preference.
![user](/assets/images/user.png)

***Step-4:*** Now you will be asked to Choose a connection method, choose the "Drivers" option.
![connect01](/assets/images/connect01.png)

***Step-5:*** Now choose the driver as Python and Install the driver by copying the command in the CMD and wait for the installation to complete.
![connect02](/assets/images/connect02.png)
![connect03](/assets/images/connect03.png)

***Step-6:*** Go to Lambda Console and create a function. Give a name and select Python as the Runtime.
![mongofunc](/assets/images/mongofunc.png)

***Step-7:*** Open your CMD and follow the steps from the image below to make a directory at your Desktop location and install the required dependencies.
![mongofunc](/assets/images/mongofunc.png)

***Step-8:*** Now open the directory that you created at your Desktop in Visual Studio Code.
![dir](/assets/images/dir.png)
![diropen](/assets/images/diropen.png)

***Step-9:*** Now create a new "lambda_function.py" python file and copy the below code into it. Then save the file.
![vspy](/assets/images/vspy.png)

```python
import os
from pymongo import MongoClient

client = MongoClient(host=os.environ.get("ATLAS_URI"))

def lambda_handler(event, context):
    # Name of database
    db = client.test 

    # Name of collection
    collection = db.test

    # Document to include
    document = {"first name": "Charles", "last name": "Delon"}

    # Insert Document
    result = collection.insert_one(document)

    if result.inserted_id:
        return "Inserted Successfully"
    else:
        return "Failed to Insert"
```

***Step-10:*** Open CMD and create a zip file of the dependencies directory with the lambda_function.py in it. Follow the below images for the commands.
![zipd](/assets/images/zipd.png)
![zipd2](/assets/images/zipd2.png)

***Step-11:*** Go to your Lambda function page and click on the button "Upload" and follow the steps below to upload the zip file that you created.
![uzip](/assets/images/uzip.png)
![uzip2](/assets/images/uzip2.png)

After Successful upload you will see this.
![uzip3](/assets/images/uzip3.png)

***Step-12:*** Now go to "Configuration" tab and then go to "Environment variables" and click on the button "Edit".
![var](/assets/images/var.png)

***Step-13:*** Then click on "Add environment variable".
![var2](/assets/images/var2.png)

***Step-14:*** Go back to MongoDB Atlas website and in your Cluster page click on button "Connect" and select "Drivers", then scroll down and copy the URL.
![var3](/assets/images/var3.png)
![var4](/assets/images/var4.png)
![var5](/assets/images/var5.png)

> [!IMPORTANT]
> Replace <password> with the password that you had provided in **Step-3** 

***Step-15:*** Paste the URL in the Lambda Environment variable. The key should be "ATLAS_URI" same as in the code of the Lambda function.
![var6](/assets/images/var6.png)

***Step-16:*** Now come back to Lambda code and click on "Test". Then give the Event name and click "Save".
![test](/assets/images/test.png)
![test2](/assets/images/test2.png)

***Step-17:*** Now click again on "Test" and you will screen as shown below.
![test3](/assets/images/test3.png)

> [!IMPORTANT]
> It might happen that the Lambda function might not run show a timeout error. In that case just go back to MongoDB Atlas website and follow the steps below to make your Database Cluster accessible from all IP Address.

![access](/assets/images/access.png)
![access2](/assets/images/access2.png)
![access3](/assets/images/access3.png)

###Now you can connect to any of your MongoDB Database with this Serverless Architecture.###