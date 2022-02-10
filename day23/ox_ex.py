# os 모듈 - 환경변수나 디렉터리, 파일 등의 os 자원을 제어하는 모듈
import os

os.chdir('c:\python\pyworks\day26')
dir = os.popen('dir')
print(dir.read())



