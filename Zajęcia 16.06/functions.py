"""
Example
"""
print('Top level instruction')
def foo(arg1, arg2):
    """
    Example docs
    :return:
    """
    a = 2
    def bar(x, y):
        """
        
        :param x: 
        :param y: 
        :return: 
        """
        return x ** y

    print('foo')
    return arg1 + arg2 + a + bar(2, 3)
if __name__ == '__main__':
    print('instruction in ')
    foo_result = foo(1, 2)
    print(foo_result)
