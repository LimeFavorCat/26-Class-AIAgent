# 폴더 내 모든 파일 읽어오기
from pathlib import Path

# 읽어올 폴더 지정
data_dir = Path('11-file/data')

txt_files = data_dir.glob('*.txt')

for file in txt_files:
    print()
    with open(file,'r',encoding='utf-8') as f:
        contents = f.read()
        print(contents)
    print('-' * 30)