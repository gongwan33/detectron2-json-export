import json
import numpy as np
from gpuinfo import GPUInfo
import _thread
import time

class JSONOutput:
    def __init__(self, fname):
        ofname = ''.join(fname.split(".")[:-1])

        if len(ofname) < 1:
            ofname = fname + '-res.json'
        else:
            ofname = ofname + '.json'

        print("Open %s to write json data"%ofname)
        self.f = open(ofname, 'w+')

        if self.f is not None:
            self.f.write("[")
        
        self.anno_count = 0
        self.gpu_percent = 0
        self.gpu_memory = 0
        self.gpu_thread = True
        self.thread_lock = _thread.allocate_lock()

        try:
            _thread.start_new_thread(self.get_gpu_info, ())
            print("GPUINFO Thread Started.")
        except Exception as e:
            print("Unable to start GPUINFO Thread")
            print(e)

        return

    def get_gpu_info(self):
        print("GPUINFO: Start loop")
        while self.gpu_thread:
            self.thread_lock.acquire()
            self.gpu_percent, self.gpu_memory = GPUInfo.gpu_usage()
            self.thread_lock.release()
            time.sleep(1)

        print("GPUINFO: End loop")
        return

    def write(self, predictions, idx):
        instances = predictions
        keypoints = instances.pred_keypoints.numpy().astype("float").round(5)
        scores = instances.scores.numpy()

        for i, points in enumerate(keypoints):
            self.thread_lock.acquire()
            key_annotation = {
                "image_id": idx,
                "category_id": 1,
                "keypoints": points.flatten().tolist(),
                "score": round(scores[i].astype("float"), 5),
                "instance_num": len(keypoints),
                "gpu_percentage": self.gpu_percent,
                "gpu_memory": self.gpu_memory
            }
            self.thread_lock.release()
    
            if self.f is not None:
                if self.anno_count > 0:
                    self.f.write(",\n")
 
                json.dump(key_annotation, self.f)
                self.anno_count += 1
    
        return
    
    def release(self):
        if self.f is not None:
            self.f.write("]")
            self.f.close()
            self.gpu_thread = False
        return

