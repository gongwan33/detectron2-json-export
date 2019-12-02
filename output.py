import json
import numpy as np

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
        return

    def write(self, predictions, idx):
        instances = predictions
        keypoints = instances.pred_keypoints.numpy().astype("float").round(5)
        scores = instances.scores.numpy()
        anno_count = 0

        for i, points in enumerate(keypoints):
            key_annotation = {
                "image_id": idx,
                "category_id": 1,
                "keypoints": points.flatten().tolist(),
                "score": round(scores[i].astype("float"), 5)
            }
    
            if self.f is not None:
                if anno_count > 0:
                    self.f.write(",\n")
 
                json.dump(key_annotation, self.f)
                anno_count += 1
    
        return
    
    def release(self):
        if self.f is not None:
            self.f.write("]")
            self.f.close()
        return

