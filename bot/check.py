from bot.decorators import safe_handler_method

def wrapper(func):
    def wrap():
        try:
            return func()
        except Exception:
            print('Exception')
    return wrap


@wrapper
def func():
    print('hi')
    int('3d')


def main():
    func()
main()