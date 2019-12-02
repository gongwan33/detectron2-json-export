#!/bin/bash
DIR="/root/gong/testdata"

for entry in "$DIR"/*
do 
    echo $entry
    FileName=`basename $entry`
    FileNameWithoutExt=${FileName%.*}
    echo $FileNameWithoutExt
    python demo/demo.py --config configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml --video-input $entry --output "/root/detectron2/resvideos/$FileNameWithoutExt.mp4" --opts MODEL.WEIGHTS /root/gong/PD601/detectron2/weights/model_R50_FPN_3x.pkl 
    #python demo/demo.py --config configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml --video-input /root/gong/PD601/short.mp4 --output "/root/detectron2/resvideos/short.mp4" --opts MODEL.WEIGHTS /root/detectron2/weights/model_R50_FPN_3x.pkl 
done

