# 큐 만들기(FIFO)
import queue
data_queue = queue.Queue()

# 데이터 넣기
data_queue.put("korea")
data_queue.put(1)

# 큐 사이즈 확인하기
print(data_queue.qsize())

# 데이터 꺼내기
print(data_queue.get())

# 데이터 꺼내면 큐사이즈 작아짐
print(data_queue.qsize())

# LifeQueue (나중에 입력된 데이터가 먼저 출력되는 구조(스택과 유사방식) LILO)
data_queue2 = queue.LifoQueue()

# 데이터 넣기
data_queue2.put("korea")
data_queue2.put(1)

# 데이터 꺼내기
print(data_queue2.get())

# PriorityQueue (데이터마다 우선순위를 넣어서, 높은 순으로 데이터 출력)
data_queue3 = queue.PriorityQueue()

# 데이터 넣기
data_queue3.put((10, "korea"))  # (우선순위, 데이터)형식의 튜플로 넣어야함
data_queue3.put((5,1))          # (우선순위, 데이터)형식의 튜플로 넣어야함
data_queue3.put((15,"china"))   # (우선순위, 데이터)형식의 튜플로 넣어야함

# 데이터 꺼내기
print(data_queue3.get())       # 우선수위값이 가장 낮은 데이터 순으로 출력













