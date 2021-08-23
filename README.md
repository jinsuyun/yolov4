run  
./darknet detector test kodastest.data cfg/[yolov4-tiny-flip.cfg|yolov4-tiny-noflip.cfg] {weight path} {input image path} -out {path to save prediction image} -thresh 0.25 -txt {txt path} -dont_show

cfg path  
darknet/cfg/yolov4-tiny-flip.cfg(flip)

-txt  
Object detection information for the image is saved as a saved result.txt file.

-out  
path to save prediction image

-car
car only recall precision for new GT format