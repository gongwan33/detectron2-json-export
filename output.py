def json_output(predictions):
    print(predictions)
    instances = predictions['instances']
    keypoints = instances.pred_keypoints
    print(instances)
    print(keypoints)

def json_output_init(fname):
    return

def json_output_finish():
    return

