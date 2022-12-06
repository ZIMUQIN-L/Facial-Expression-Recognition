import cv2 as cv
import cv2
import subprocess as sp
import shlex
import queue
# q = queue.Queue()
import myQueue
# ffmpeg 推流


# class FfmpegRemp(object):
#
#     def __init__(self, rtmpfile, videoid):
#
#         self.rtmpUrl = "rtmp://47.93.55.157/" + rtmpfile
#         self.video_stream_path = videoid
#         self.WIDTH = 640
#         self.HEIGHT = 420
#         self.FPS = 30.0
#         self.stat = True
#
#     def open_opencv(self):
#         cap = cv2.VideoCapture(self.video_stream_path, cv2.CAP_DSHOW)
#         # 设置摄像头设备分辨率
#         # cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
#         # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
#         # 设置摄像头设备帧率,如不指定,默认600
#         cap.set(cv2.CAP_PROP_FPS, self.FPS)
#         # 解决延迟
#         cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
#         return cap
#
#     def open_ffmpeg(self):
#         cap = self.open_opencv()
#         fps = int(cap.get(cv2.CAP_PROP_FPS))
#         # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         # ffmpeg command
#         command = ['ffmpeg',
#                    '-y',
#                    '-f', 'rawvideo',
#                    '-vcodec', 'rawvideo',
#                    '-pix_fmt', 'bgr24',
#                    '-r', str(fps),
#                    '-i', '-',
#                    '-c:v', 'libx264',
#                    '-pix_fmt', 'yuv420p',
#                    '-preset', 'ultrafast',
#                    '-f', 'flv',
#                    self.rtmpUrl]
#
#         # print(command)
#         # 管道配置
#         # self.p = sp.Popen(command, stdin=sp.PIPE, shell=True)
#         p = subprocess.Popen(command, stdin=subprocess.PIPE)
#         # read webcamera
#         print(cap.isOpened())
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 print("Opening camera is failed")
#                 break
#             elif not self.stat:
#                 p.kill()
#                 print("停止推流")
#                 break
#             p.stdin.write(frame.tostring())
#
#     # 关闭直播
#
#     def close_ffmpeg(self):
#         self.stat = False
#         self.open_ffmpeg()


def push(rtmpURL, capId):
    """
    向ZLMediaKit进行推流
    :param rtmpURL: 推流的url
    :param capId: 摄像头id，一般为0
    :param q: 存放帧的队列
    """
    cap = cv.VideoCapture(capId)
    # cap.set(cv2.CAP_PROP_FPS, FPS)
    fps = int(cap.get(cv.CAP_PROP_FPS))

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    # ffmpeg command
    command = ['ffmpeg',
               '-y',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-s', "{}x{}".format(width, height),
               '-r', str(fps),
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-f', 'flv',
               rtmpURL]

    # 管道配置
    p = sp.Popen(command, stdin=sp.PIPE)

    # read webcamera
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Opening camera is failed")
            break
        myQueue.put(frame)
        # process frame
        # your code
        # process frame
        # q.put(frame)
        # write to pipe
        p.stdin.write(frame.tostring())


if __name__ == "__main__":
    # rtmpUrl = "rtmp://pengcheng.phi-ai.org:35690//live/test"
    rtmpUrl = "rtmp://bagua.phi-ai.org:46785//live/test"
    push(rtmpUrl, 0)
