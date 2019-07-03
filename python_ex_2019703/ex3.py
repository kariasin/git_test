# 과제
# 1. 계좌 관리 class 작성하기
# - attribute: 계좌 초기 금액을 속성으로 하나 설정
# - 생성자에서 초기 금액은 0으로 설정
# - 속성은 private 으로 설정
# - method: 인출, 저축, 잔액 확인 세 가지 method 구현, 각각 현재 계좌 금액 리턴
# - 각 method 도 private 으로 설정

# 2. 학생 성적 관리 class 작성하기
# - attribute: 국어, 영어, 수학, 학생 이름 네 개의 속성
# - 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정
# - 각 속성은 private 으로 설정
# - method: 전체 과목 점수 평균, 전체 과목 총점 두 가지 method 구현
# - 각 method 는 private 으로 설정

# 3. 피자 가게 관리 class 작성하기
# - attribute: 피자 종류(리스트 데이터 타입), 피자 가게 이름 속성
# - 생성자에서 각 속성을 객체 생성시 전달된 인자값으로 설정, 피자 종류는 ['슈퍼슈프림', '콤비네이션', '불고기']로 제공
# - 각 속성은 private 으로 설정
# - method: 원하는 피자를 제공하는지를 알려주는 기능, YES 또는 NO 문자열을 리턴

class account:
    def __init__(self):
        self.__total = 0
    def __set_account(self,total):
        self.__total = total    
    def __set_i(self,total):
        if self.__total >= total:    
            self.__total = self.__total - total
    def __set_s(self,total):
        self.__total = self.__total + total    
    def __get_b(self):
        return self.__total
a = account()

a.__set_account(500)
print(a.__get_b())
a.__set_i(300)
print(a.__get_b())