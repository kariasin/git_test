class AndroidSmartPhone:
    def send(self, message):
        print("send a message via Android platform")

class WindowsSmartphone:
    def send(self,message):
        print("send a message via Window Mobile platform")

class iOSSmartphone:
    def send(self,message):
        print("send a message via iOS platform")

class SmartphoneFactory(object):
    def __init(self):
        pass
    
    def create_smartphone(self,devicetype):
        if devicetype == 'android':
            smartphone = AndroidSmartPhone() # <== 실제 객체를 팩토리 클래스 안에서 만든다.
        elif devicetype == 'window':
            smartphone = WindowsSmartphone() # <== 실제 객체를 팩토리 클래스 안에서 만든다.
        elif devicetype == 'ios':
            smartphone = iOSSmartphone() # <== 실제 객체를 팩토리 클래스 안에서 만든다.
        return smartphone

#팩토리 클래스로 실제 상세 객체 만들기

smartphone_factory = SmartphoneFactory()
message_sender1 = smartphone_factory.create_smartphone('android')
message_sender1.send('hi')

message_sender2 = smartphone_factory.create_smartphone('window')
message_sender2.send('good')

message_sender3 = smartphone_factory.create_smartphone('ios')
message_sender3.send('hahaha')

