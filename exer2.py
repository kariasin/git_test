def decorator1(tag):
    def outer_wrapper(function):
        def innter_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return innter_wrapper    
    return outer_wrapper
@decorator1('b')
def print_hello():
    return 'hello'
print(print_hello())
