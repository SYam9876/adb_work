Working with adb commands using my smartphone

Commands Used

adb shell getprop ro.product.model      # Device Model
adb shell getprop ro.build.version.release  # Android Version

adb logcat -d > C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\logcat.txt      #Capture logcat to a file
adb shell dmesg > "C:\Users\NETCOM\Desktop\Cavli_Training\abd_work\2.logcat & dmesg logs\dmesg.txt"   # Capture dmesg to a file

adb logcat *:E > "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\3.Error log using logcat\error_log.txt" 

adb pull /sdcard/cheat_sheet_adb.pdf "C:\Users\NETCOM\Desktop\Cavli_Training\adb_work\4.Pull from device to computer"

adb push "C:\Users\NETCOM\Desktop\Cavli_Training\docker\Cavli_Docker_SDK_Setup_User_Guide.pdf" /sdcard/
