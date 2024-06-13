# 기준 경로
def start():
    print("나는 pacakageC에 있는 main 파일이에요.")

start()

# 동일 경로
from moduleC import same

same()

# 하위 경로
from subpackageC.submoduleC import sub

sub()

# 상위 경로
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from moduleA import upper

upper()

# 다른 경로
sys.path.append('C:/Users/mcw/python-practice/module-import-test/packageB/moduleB.py')
from packageB.moduleB import other

other()

print(sys.path)