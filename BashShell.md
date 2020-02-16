This beginner’s tutorial shows you **how to install bash on Windows**._ **Linux on Windows** is a reality, thanks to the partnership between 
- [Canonical](https://www.canonical.com/) (parent company of Ubuntu) and 
- [Microsoft](https://www.microsoft.com). 

This way you can run Linux commands inside Windows without the needing to install a virtual machine.This is a good option if your main aim is to learn Linux/Unix commands.

## Method 1: Install Linux Bash Shell on Windows 10 Newer Versions

- Good thing is that [Fall Creator’s Update](https://blogs.msdn.microsoft.com/commandline/2017/10/11/whats-new-in-wsl-in-windows-10-fall-creators-update/) makes it easier to install Bash on Windows 10. 
- You can get it in one click from Windows Store. 
- There are still a few things to do however. 
- Install the Ubuntu using Windows 10 Linux subsytem (You can also use SUSE Linux), the procedure is same for both distributions.

### Step 1: Enable “Windows Subsystem for Linux” feature 

- The first thing you need to do is to enable Windows Subsyetm for Linux feature from [PowerShell](https://itsfoss.com/microsoft-open-sources-powershell/). 
- Go to the Start menu and search for PowerShell. 
- Run it as administrator:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/Powershell-Ubuntu-install_02_16_20.jpg" width="500">

- Once you have the PowerShell running, use the command below to enable Bash in Windows 10. - 


```sh
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

- You’ll be asked to confirm your choice. Type Y or press enter:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/Powershell-Ubuntu-install-2_02_16_20.jpg" width="600">


- Now you should be asked to reboot. Even if you are not asked to, you must restart your system.  

### Step 2: Download a Linux system from the Windows store 

- Once your system has rebooted, go to the Windows Store and search for “Linux.”

<img src="">
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/install-ubuntu-windows-10-linux-subsystem-3-1.jpeg" width="500">

- You’ll see the option to install Ubuntu or SUSE. I have installed Ubuntu for Bash on Windows here.

<img src="">
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/ubuntu_suse_choice_02_16_20.png" width="500">


- What’s the difference between using Ubuntu or openSUSE or SUSE Linux Enterprise? And which one should you use? 
- Use UBUNTU! If you get to a point where Suse is peaking your interest, then you have learned enough to know what you want.

- Once you choose the distribution of your choice, you’ll see the option to install it. Do note that it will download files of around 1Gb in size. So you should have a good internet connection here.

<img src="">
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/install_ubuntu_win10_02_16_20.jpg" width="500">


### Step 3: Run Linux inside Windows 10

- You are almost there. Once you have installed Linux, it’s time to see how to access Bash in Windows 10. 
- Just search for the Linux distribution you installed in the previous step. 
- In should be **Ubuntu**. 
- You’ll see that it runs like a normal Windows application. 
- It will take some time installing and then you’ll have to set up the username and password.


<img src="">
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/ubuntu_on_windows_confirm_02_16_20.jpg" width="500">

- Don’t worry, it’s just for the first run. 
- Bash shell will be available for use directly from the next time onwards. 
- Enjoy Linux inside Windows 10. 

### Troubleshooting 1: 

- **The WSL optional component is not enabled. Please enable it and try again. **
- You may see an error like this when you try to run Linux inside Windows 10:

```sh
The WSL optional component is not enabled. Please enable it and try again. 
See https://aka.ms/wslinstall for details. 
Error: 0x8007007e 
Press any key to continue...
```

- And when you press any key, the application closes immediately. 
- The reason here is that the Windows Subsystem for **Linux is not enabled** in your case. 
- You should enable it as explained in** step 1 **of this guide. You can do that even after you have installed Linux from Windows Store. 


### Troubleshoot 2: Installation failed with error 0x80070003

- This is because Windows Subsystem for Linux only runs on the system drive i.e. the C drive. 
- You should make sure that when you download Linux from the Windows Store, it is stored and installed in the C Drive. 

```
Go to Settings -> Storage -> More Storage Settings: Change where new content is saved and select C Drive here.
```

 ## Method 2: Install Linux Bash Shell on older Windows 10
 
- [Older Windows 10 Tutorial](BashShellOld10.md)