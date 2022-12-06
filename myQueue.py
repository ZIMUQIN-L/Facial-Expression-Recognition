import cv2 as cv
import cv2
import subprocess as sp
import shlex
import queue

q = queue.Queue()


def get():
    return q.get()


def put(frame):
    q.put(frame)
