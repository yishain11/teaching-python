def function_factory(phrase):
    def inner_fn():
        print(phrase)

    return inner_fn


my_fn = function_factory("hi!")
my_fn()
