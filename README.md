run(new  GT)  
./darknet detector test {data path kodastest.data} {cfg path yolov4-tiny-flip.cfg} {weight path .weight} {input image path} -gt {path for gt directory} -out {path to save prediction image} -thresh 0.25 -txt {txt path} -dont_show -car

(gt for CAM_FL, CAM_FR, etc..)  
./darknet detector test {data path kodastest.data} {cfg path yolov4-tiny-flip.cfg} {weight path .weight} {input image path} -gt {path for gt directory} -out {path to save prediction image} -thresh 0.25 -txt {txt path} -dont_show

cfg path  
darknet/cfg/yolov4-tiny-flip.cfg(flip)

-txt  
Object detection information for the image is saved as a saved result.txt file.

-gt
path for gt directory

-out  
path to save prediction image

-car
car only recall precision for new GT format

-dont_show
no show detection image