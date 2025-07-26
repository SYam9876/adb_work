# Working with ADB Commands Using My Smartphone

## Commands Used

1. `adb shell getprop ro.product.model`  
   → Get the device model.

2. `adb shell getprop ro.build.version.release`  
   → Get the Android version.

3. `adb logcat -d > C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\logcat.txt`  
   → Capture logcat output to a file.

4. `adb shell dmesg > "C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\dmesg.txt"`  
   → Capture dmesg output to a file.

5. `adb logcat *:E > "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\3.Error log using logcat\error_log.txt"`  
   → Capture only error-level logcat messages.

6. `adb pull /sdcard/cheat_sheet_adb.pdf "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\4.Pull from device to computer"`  
   → Pull a file from the device to your computer.

7. `adb push "C:\Users\NETCOM\Desktop\Cavli_Training\docker\Cavli_Docker_SDK_Setup_User_Guide.pdf" /sdcard/`  
   → Push a file from your computer to the device’s SD card.
