import urllib.request

def connect(host="https://www.nic.ir/"):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

# test
print( "connected" if connect() else "no internet!" )