import glob
import os
[os.remove(f) for f in glob.glob("../KODAS/bdd100k/images/100k/train/*.txt")] #txt파일 삭제를 원하는 디렉토리 경로
