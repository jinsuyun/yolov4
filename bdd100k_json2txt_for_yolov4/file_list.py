import glob

path_dir ='/home/sanggyu/darknet/KODAS/bdd100k/images/100k/val' # image파일의 경로

file_list=glob.glob(path_dir+'/*.jpg')

with open(path_dir+'/val.txt', 'w') as f: #원하는 이름으로 txt파일 생성
   for line in file_list[:-1]:
       f.write(line+'\n')
