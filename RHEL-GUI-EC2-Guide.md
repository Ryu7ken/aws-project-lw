<h2>Launching a RHEL9 GUI on Amazon EC2 Instance</h2>

<h3>Below is the step by step guide to configure a EC2 instance for RHEL9 GUI:</h3>

***Step-1:*** Go to EC2 Console and click on "Launch Instance".

***Step-2:*** Give a name to your instance and select Red Hat AMI.

![Launch](/assets/images/Launch.png)

***Step-3:*** Select "t2.medium" as Instance type for optimal performance of the GUI.

![Instance](/assets/images/Instance.png)

***Step-4:*** In Key pair, click on "Create new key pair". Give a name to your key pair.

![KeyPair](/assets/images/KeyPair.png)

***Step-5:*** Then click on "Launch instance".

![LaunchInstance](/assets/images/LaunchInstance.png)

***Step-6:*** Select the instance and click on the "Security" tab, then click on the "Security groups".

![Security](/assets/images/Security.png)

***Step-7:*** Click on "Edit inbound rules", then click on "Add rule". Then select type as "RDP" and Source as "Anywhere-IPv4". Then click on "Save rules".

![Security](/assets/images/Security2.png)

![Security](/assets/images/Security3.png)

***Step-8:*** Select the Instance and click on "Connect".

![Connect](/assets/images/Connect.png)

***Step-9:*** Then click on "SSH client" and click on the copy button as shown in the image below.

![Connect](/assets/images/Connect2.png)

***Step-10:*** Open CMD in your local system and go to the folder where you had downloaded the "Key pair". And paste the command to SSH into the EC2 instance.

![Connect](/assets/images/Connect3.png)

***Step-11:*** Then press Enter and it will ask if you want to connect, so write "yes" and you will be connected to the EC2 instance.

![Connect](/assets/images/Connect4.png)

***Step-12:*** Now here is a list of commands that you have to run in the instance one after another to setup your GUI in the instance.

> [!IMPORTANT]
> First switch to root user and then start executing the commands one by one.

Switch to root user
```shell
sudo su - root
```

Set the password of root user
```shell
passwd root
```

Update your system packages
```shell
yum update
```

Install packages for GUI
```shell
yum groupinstall "Server with GUI" -y
```

Install TigerVNC server
```shell
yum install tigervnc-server -y
```

Add epel (Extra Packages for Enterprise Linux)
```shell
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm -y
```

Install xrdp
```shell
yum install xrdp -y
```

Start and enable the xrdp service
```shell
sudo systemctl start xrdp
sudo systemctl enable xrdp
```

> [!NOTE]
> Some commands execution will take time so please wait patiently and let the installations complete.

***Step-13:*** Open "Remote Desktop Connection" on your local system.

![Remote](/assets/images/Remote.png)

***Step-14:*** Copy the Public IP of the instance and paste it as shown in the image below and give the User name as "root".

![Remote](/assets/images/Remote2.png)

***Step-15:*** It will ask if you to connect, so click on "yes".

***Step-16:*** Enter you root user password and you will be connected.

![Remote](/assets/images/Remote3.png)

<h3>Now you can use the GUI version of RHEL9 on your EC2 instance.</h3>