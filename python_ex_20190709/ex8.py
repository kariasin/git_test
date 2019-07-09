def logger(msg):
    message = msg
    def msg_creator():  # <== 함수 안에 함수를 만들 수도 있음
        print('[HIGH LEVEL]: ', message)

    return msg_creator
log1 = logger('Dave Log-in')
log1()

del logger
log1()