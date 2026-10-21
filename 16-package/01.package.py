'''
* package : 관련있는 파이썬 파일(모듈)들을 기능별로 분류하여 모아놓은 디렉터리
            패키지 > 모듈 > 클래스 / 함수 / 변수

            패키지 안에는 __init__.py라는 파일이 있음

* __init__.py
        - 파이썬 패키지 (구조화된 모듈 모음)라고 하고 파이썬 시스템에 알려주는 역할
            > 파이썬 2에서는 이 파일이 없으면 패키지로 인식 못함
            > 파이썬 3부터는 이 파일이 없어도 패키지로 인식
            > 실무에서는 이 파일을 필수로 넣는 것을 권장
        - 기능
            1. 패키지를 불러올 때 가장 먼저 자동실행됨 (초기화) 딱 한번 실행
                > 패키지를 쓰기 전에 미리 설정해야 되는 것들
                    ex) 데이터베이스 연결, 로그 기록 설정, 환경변수 로드등의 초기화 작업시
            2. 패키지 가져오기(import) 경로 단축
            3. 패키지 내의 비밀파일등의 목록을 지정해 둘 수 있다.
                > 호출시 from package import *
                > __all__ 변수에 공개할 파일 목록만 지정 가능

'''
# 1번
import package01.image.io_file.imgRead
import package01.image.io_file.imgSave
package01.image.io_file.imgRead.jpgRead()
package01.image.io_file.imgSave.jpgSave()
print()

# 2번
import package01.image.io_file.imgRead as imr
import package01.image.io_file.imgSave as ims
imr.jpgRead()
ims.jpgSave()
print()

# 3번
from package01.image.io_file import imgRead, imgSave
imgRead.jpgRead()
imgSave.jpgSave()
print()

# 4번
from package01.image.io_file import imgRead as imr
from package01.image.io_file import imgSave as ims
imr.jpgRead()
ims.jpgSave()
print()

# 5번
from package01.image.io_file.imgRead import jpgRead, pngRead
pngRead()
jpgRead()

# 6번 
from package01.image.io_file.imgRead import jpgRead as jpr
from package01.image.io_file.imgSave import jpgSave as jps
jpr()
jps()