import anlory


cmd = "adb shell dumpsys window > " + "debug/dumpsys_window_"+anlory.get_time().strip()+".txt"
# os.system();
print(cmd)
anlory.exec_cmd(cmd);

anlory.short_pause()