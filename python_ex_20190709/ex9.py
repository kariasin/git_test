def html_creator(tag):
    def text_wrapper(msg):
        print('<{0}>{1}<{0}>'.format(tag,msg))
    return text_wrapper

h1_html_creator = html_creator('h1')
print(h1_html_creator)
h1_html_creator('H1 태그는 타이틀을 표시하는 태그입니다.')

p_html_creator = html_creator('p')
p_html_creator('P 태그는 문단을 표시하는 태그입니다.')



def test(t):
    def test2(t2):
        print("{0},    {1}".format(t,t2))
    return test2
t = test("test")
print(t("test2"))



def list_creator(tag):
    def text_wrapper(msg):
        print('{0} {1}'.format(tag,msg))
    return text_wrapper

data_list_minus = list_creator('-')
data_list_minus('안녕')

data_list_mul = list_creator('*')
data_list_mul('안녕')




def index_creator2(tag):
    def text_wrapper2(msg):
        print('{0}   {1}'.format(tag,msg))
    return text_wrapper2
inPlus = index_creator2('+')
inPlus('good')


















