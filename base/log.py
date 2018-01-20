import time


def log(content):
    print("log %s : %s" % (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), content))
    return