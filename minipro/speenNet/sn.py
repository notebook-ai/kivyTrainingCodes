#pip install speedtest-cli
import speedtest

# speed_test = speedtest.Speedtest()

# def bytes_to_mb(bytes):
#     KB = 1024       #One Kilobyte is 1024 bytes 
#     MB = KB * 1024  #One MB ts 1024 KB 
#     return int(bytes/MB)
# download_speed = bytes_to_mb(speed_test.download()) 
# print("Your Download speed is ", download_speed, "MB")


def getSpeedInternet(res_with="KB"):
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download()
    if res_with == "MB":
        return int(download_speed/(1024*1024))
    return int(download_speed)
print(getSpeedInternet("MB"))