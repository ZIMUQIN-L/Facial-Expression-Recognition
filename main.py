from push_stream import push
from pull_result import draw_result, get_result, getin
import threading
from multiprocessing import Process

if __name__ == '__main__':
    rtmpUrl = "rtmp://bagua.phi-ai.org:46785//live/test"
    # push(rtmpUrl, 0)
    t1 = Process(target=push, args=(rtmpUrl, 0))
    t1.start()
    t2 = Process(target=getin)
    t2.start()
    # while True:
    #     get_result("live", "test")
