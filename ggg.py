print('hello')
print (' world')

def say_saomething(number: int, word: str)-> str:
    word =word.capitalize()
    return word*number

print(say_saomething(5,"fuck"))
