# def greet(fx):
#  def mfx(*args, **kwargs):
#     print("Good morning")
#     fx(*args, **kwargs)
#     print("Good night")
#  return mfx

# @greet
# def hello():
#     print("Hello")

# hello()

def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello sir good morning")
        fx(*args, **kwargs)
        print("Good night")
    return mfx

@greet
def hello():
    print("how are you!!!!")


hello()