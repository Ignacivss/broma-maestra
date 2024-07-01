import subprocess
import datetime
import time

phone_number = "phone number"
start_time = datetime.time(21, 30, 0)
call_duration = 15
total_runtime = 600

current_time = datetime.datetime.now().time()

if current_time < start_time:
    time_until_call = datetime.datetime.combine(datetime.date.today(), start_time) - datetime.datetime.now()
else:
    tomorrow = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), start_time)
    time_until_call = tomorrow - datetime.datetime.now()

time.sleep(time_until_call.total_seconds())

start_timestamp = time.time()
while (time.time() - start_timestamp) < total_runtime:
    adb_command = f"adb shell am start -a android.intent.action.CALL -d tel:{phone_number}"

    try:
        subprocess.run(adb_command, shell=True, check=True)
        print(f"calling {phone_number} now...")

        time.sleep(call_duration)

        end_call_command = "adb shell input keyevent KEYCODE_ENDCALL"
        subprocess.run(end_call_command, shell=True, check=True)
        print(f"call ended {call_duration} seconds.")

    except subprocess.CalledProcessError as e:
        print(f"error in adb shell: {e}")

    time.sleep(5)

exit()
