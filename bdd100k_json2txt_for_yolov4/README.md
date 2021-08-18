 json2txt for yolov4
 ===

코드 설명
---
* **bdd100k_json2txt.py**  
  bdd100k 데이터셋에서 10개의 클래스에 대한 name과 bbox를 추출하고 json파일과 동일한 파일명으로 image파일이 있는 디렉토리에 txt파일을 생성합니다.     
  사용 시 json파일에 대한 디렉토리 위치와 image파일에 대한 디렉토리 위치를 수정하셔서 사용하시면 됩니다.

* **file_list.py**  
  학습 시 image파일의 경로를 명시하기 위해 image파일의 모든 위치를 txt파일에 저장합니다.    
  image파일의 경로를 수정해서 사용하시면 됩니다.

* **remove_txt.py**  
  `bdd100k_json2txt.py` 에서 txt 파일 생성 시 `'a'` 모드로 파일을 저장하므로 2회이상 실행 시 같은 데이터가 여러번 이어써집니다.      
  따라서 txt파일을 제거하고 다시 실행해야 하는 경우 해당 디렉토리의 txt 파일을 모두 삭제해줍니다.  
  삭제를 원하는 디렉토리에 대해 경로를 수정해서 사용하시면 됩니다.
  
사용 방법
---
- 각 파이썬 파일을 원하는 디렉토리 경로로 수정하여 `darknet`폴더에 업로드하거나
   `git clone`을 통해 다운받은 후 `vim`명령어를 통해 디렉토리 경로를 수정해야 합니다.
1. `bdd100k_json2txt.py`의 36번째 줄에서 `json_dir= 'json 파일 경로'`에 train dataset의 labels에 대한 json파일의 디렉토리 경로
   를 입력하고 `img_dir = 'image 파일 경로'` 에 train dataset의 jpg파일의 디텍토리 경로를 입력합니다. `bdd100k_json2txt.py`를 실행하고 validation data set에 대하여 반복합니다.
2. `file_list.py`의 3번째 줄에서 `path_dir ='image 파일 경로'` 에 image파일의 경로를 입력하고 7번째 줄에서 '원하는 파일명'을 저장할 파일명으로 수정합니다.  
  이후 `file_list.py`를 실행하고 validation dataset에 대해 반복합니다.
3. 2번에서 생성한 txt파일을 `.data` 파일의 train과 valid값에 입력하여 모델 학습을 진행합니다.