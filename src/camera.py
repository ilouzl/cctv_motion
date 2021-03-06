import cv2
from threading import Thread
from collections import deque
import time
import logging

class RtspCamera(object):
    def __init__(self, url, fps=10, frame_cb=None):
        self.cap = cv2.VideoCapture(url)
        self.fps = int(fps)
        self.frame_period = int(1000.0/self.fps) 
        self.frame_cb = frame_cb
        self.buffer_len = 20
        self.buffer = deque(maxlen=self.buffer_len)
        self.thread = Thread(target=self.run)
        self.thread.daemon=True
        self.thread.start()

    def close(self):
        logger.info("Closing camera")
        self.cap.release()

    def run(self):
        frame_cnt = 0
        t_fps = time.time()
        while True:
            t = time.time()
            ret, frame = self.cap.read()
            t_cap = time.time()
            if ret == False:
                break
            frame_cnt += 1
            if frame_cnt == self.fps:
                frame_cnt = 0
                logging.debug("Time to capture %d frames = %f"%(self.fps, t - t_fps))
                t_fps = t
            self.buffer.append((frame, t_cap))
            logging.debug(str(time.time() - t) + ", " + str(frame[0,0,0]))
     

    def prepare_frame(self, frame):
        gray = self.cv2.cvtColor(frame, self.cv2.COLOR_BGR2GRAY)
        gray = self.cv2.flip(gray, 0) 
        return gray

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    def tmr():
        while True:
            time.sleep(1)
            print(time.time())
            
    def test():
        cam = RtspCamera("rtsp://192.168.1.151/user=admin_password=tlJwpbo6_channel=1_stream=0.sdp") 
        while True:
            time.sleep(1)
            pass
        cam.thread.join()

    test()
