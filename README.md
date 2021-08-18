run: ./darknet detector test kodastest.data cfg/yolov4-tiny-flip.cfg {weight path} {input image path} -thresh 0.25 -txt {txt path} -dont_show

cfg path : darknet/cfg/yolov4-tiny-flip.cfg(flip) 
           darknet/cfg/yolov4-tiny-noflip.cfg(no flip)

-txt : Object detection information for the image is saved as a saved result.txt file.

-out : save prediction image