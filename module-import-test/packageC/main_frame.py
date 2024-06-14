import config

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
from moduleA import upper

upper()

# 다른 경로
from packageB.moduleB import other

other()