# Working with ADB Commands Using My Smartphone

## Commands Used

1. `adb shell getprop ro.product.model`  
   → Get the device model.  

   `adb shell getprop ro.build.version.release`  
   → Get the Android version.  

2. `adb logcat -d > C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\logcat.txt`  
   → Capture logcat output to a file.  

   `adb shell dmesg > "C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\dmesg.txt"`  
   → Capture dmesg output to a file.  

3. `adb logcat *:E > "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\3.Error log using logcat\error_log.txt"`  
   → Capture only error-level logcat messages.  

4. `adb pull /sdcard/cheat_sheet_adb.pdf "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\4.Pull from device to computer"`  
   → Pull a file from the device to your computer.  

5. `adb push "C:\Users\NETCOM\Desktop\Cavli_Training\docker\Cavli_Docker_SDK_Setup_User_Guide.pdf" /sdcard/`  
   → Push a file from your computer to the device’s SD card.  

6. `adb shell screencap -p /sdcard/screen.png`  
   → Take a screenshot using ADB.

7. `adb shell pm list packages > "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\7.List installed packages\installed_packages.txt"`  
   → Listing installed packages on device.

8. `adb shell monkey -p com.canva.editor 1`  
   → Launches an app by its package name.

   `adb shell am force-stop com.canva.editor`  
   → Immediately stops an app and removes it from memory.

9. `adb logcat | findstr com.Slack > "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\9.Realtime log\app_log.txt"`  
   → Monitor realtime logs for slack.

10. `adb shell input keyevent <keycode>`  
   → Simulate hardware keypress based on keycode.

11. `adb shell ps -A`  
   → Viewing all running Processes.

    `adb shell top`  
   → Monitor CPU/Memory usage.

12. `adb install "C:\Users\NETCOM\Downloads\Mini Militia Classic _ DA2 MMC_0.14.4_APKPure"`  
   → Installing app using adb.

13. `adb uninstall com.appsomniacs.mmc`  
   → Uninstalling app using abd.
