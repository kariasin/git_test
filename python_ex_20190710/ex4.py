def mark_bold(function):
    "%%html"
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args,**kwargs) + '</b>'
    return wrapper

def mark_italic(function):
    def wrapper(*args, **kwargs):
        return '<i>' + function(*args,**kwargs) + '</i>'
    return wrapper


# @mark_bold
# def contetns(string):
#     return string
# print(contetns('test'))

# @mark_italic
# def contetns(string):
#     return string
# print(contetns('test'))

@mark_bold
@mark_italic
def contetns(string):
    return string
print(contetns('test'))


