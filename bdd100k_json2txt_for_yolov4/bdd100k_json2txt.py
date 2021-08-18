import json
import glob

label_category=["car","bus","person","bike","truck","motor","train","rider","traffic sign","traffic light"]
#lavel mapping : 10 classes
label_map = {
    "car": 0,
    "bus": 1,
    "person": 2,
    "bike": 3,
    "truck" : 4,
    "motor" : 5,
    "train" : 6,
    "rider" : 7,
    "traffic sign" : 8,
    "traffic light" : 9
}
#image size
IMG_WIDTH = 1280
IMG_HEIGHT = 720

#yolo에 사용할 수 있도록 class, 중심좌표(x,y), 크기(w,h) 를 전체이미지에 대해 비율로 포맷변경 (0~1)
def box2d_to_yolo(box2d):
    x1 = box2d["x1"] / IMG_WIDTH
    x2 = box2d["x2"] / IMG_WIDTH
    y1 = box2d["y1"] / IMG_HEIGHT
    y2 = box2d["y2"] / IMG_HEIGHT

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    w = abs(x2 - x1)
    h = abs(y2 - y1)

    return x, y, w, h

json_dir='../KODAS/bdd100k/labels/100k/val' # json파일의 디렉토리 경로
img_dir='../KODAS/bdd100k/images/100k/val' # image파일의 디렉토리 경로
json_list=glob.glob(json_dir+'/*.json') #디렉토리 내 json파일 리스트

for i in json_list:
    with open(i,'r') as json_files:
        json_obj=json.load(json_files) #json 파일 로드
        json_name=json_obj["name"] #name 추출
        k=0 #k개의 클래스 정보 추출을 위해 초기화

        '''
        반복문 내 카테고리 정보를 추출하고 10개 class에 포함하지 않는 카테고리가 나올 때까지 반복
        카테고리와 바운딩박스에 대한 데이터 추출
        yolo의 바운딩박스 포맷으로 변환
        클래스 매핑하여 문자열에서 정수형으로 변환
        yolo에 적합한 txt 형식으로 to_txt 문자열 생성 class x y w h 형태
        txt파일을 json파일 위치에 같은 이름으로 생성
        '''

        while(json_obj["frames"][0]["objects"][k]["category"] in label_category):
            json_class=json_obj["frames"][0]["objects"][k]["category"]
            json_bbox=json_obj["frames"][0]["objects"][k]["box2d"]
            x, y, w, h = box2d_to_yolo(json_bbox)
            lbl = label_map[json_class]
            to_txt_list=[lbl,x,y,w,h]
            to_txt_str=str(to_txt_list).replace(",","")
            to_txt_li=to_txt_str.replace("[","")
            to_txt = to_txt_li.replace("]", "")
            print(to_txt)
            json2txt=img_dir+"/"+json_name
            print(json2txt)
            with open(json2txt+'.txt', 'a') as f:
                    f.write(to_txt+"\n")
            k=k+1
            '''
            10개 클래스 이외 데이터가 없어 최대 인덱스보다 반복문이 더 반복되서 오류가 발생하는 경우
            k+1에서 objects 내에 box2d가 있는지 확인하고 없을 경우 반복문을 빠져나옴
            key error가 발생하는 경우를 예외처리하여 반복문을 빠져나옴
            '''
            try :
                if not json_obj["frames"][0]["objects"][k]["box2d"]  : break
            except :
                break
