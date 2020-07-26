#!/bin/sh
echo 'strated..'

img_name=img.png
img_dir=/home/bumuthudilshanhhk/scripts/images
smplifyx_dir=/home/bumuthudilshanhhk/smplifyx
sudo rm $smplifyx_dir/data/images/*
sudo rm $smplifyx_dir/data/keypoints/*
cd ../openpose
sudo ./build/examples/openpose/openpose.bin --image_dir $img_dir/ --write_json output/ --display 0 --render_pose 0 --face --hand
sudo cp $img_dir/$img_name $smplifyx_dir/data/images/$img_name
sudo cp output/* $smplifyx_dir/data/keypoints
cd ../smplifyx
sudo python3.6 smplifyx/main.py --config cfg_files/fit_smplx.yaml --data_folder data --output_folder output --visualize="False" --model_folder models/models --vposer_ckpt models/vposer --part_segm_fn smplx_parts_segm.pkl
sudo cp -R output/ ../scripts/
echo 'finished!'
 
exit 0
