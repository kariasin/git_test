class SalesWorker:
    def __init__(self,name):
        self.name = name
    def work(self):
        print(self.name, 'sells something')
class DevWorker:
    def __init__(self,name):
        self.name = name
    def work(self):
        print(self.name, 'develops somthing')
worker1 = SalesWorker('Dave')
worker2 = SalesWorker('David')
worker3 = SalesWorker('Andy')
worker4 = DevWorker('Aiden')
worker5 = DevWorker('Tina')
worker6 = DevWorker('Anthony')


workers = [worker1,worker2,worker3,worker4,worker5,worker6]

for worker in workers:
    worker.work()


# * 요정(Elf), 파이터(Fighter) 클래스 만들기
# - 이름을 입력받음 - Elf의 attack 메서드: 출력 "마법으로 공격합니다."
# - Fighter의 attack 메서드: 출력 "주먹으로 공격합니다."
# - 다음과 같이 객체 생성 후 반복문으로 공격
class Elf:
    def __init__(self,name):
        self.name = name
    def attack(self):
        print("마법으로 공격")
class Fighter:
    def __init__(self,name):
        self.name = name
    def attack(self):
        print("주먹으로 공격")

elf1 = Elf('Dave')
fighter1 = Fighter('Anthony')
ourteam = [elf1, fighter1]
for attacker in ourteam:
    attacker.attack() 