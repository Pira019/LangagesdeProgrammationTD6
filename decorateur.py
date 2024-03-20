def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
               # result = func(*args, **kwargs)
                print(*kwargs)
                func(*kwargs)
            return 25
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet(a='name')

"""
def ma_fonction(*args, **kwargs):
    print("Arguments positionnels (args) :", args)
    print("Arguments de mots-clés (kwargs) :", args)"""

# Appel de la fonction avec différents arguments
#ma_fonction(1, 2, 3, a='a', b='b', c='c')
