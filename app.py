from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    try:                                                                                                                                          
        raise TypeError()                                                                                                                         
    except TypeError as e:                                                                                                                        
        print(e)                                                                                                                                  
    except TypeError as e:                                                                                                                        
        print("Duplicado, ou seja, nunca vai entrar aqui.")    


if __name__ == '__main__':
    app.run()

def foo():
    try:
        raise FloatingPointError()
    except (ArithmeticError, RuntimeError) as e:
        print(e)
    except FloatingPointError as e: # Noncompliant. FloatingPointError is a subclass of ArithmeticError
        print("Never executed")
    except OverflowError as e: # Noncompliant. OverflowError is a subclass of ArithmeticError
        print("Never executed")

    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e: # Noncompliant. Duplicate Except.
        print("Never executed")

    try:
        raise ValueError()
    except BaseException as e:
        print(e)
    except: # Noncompliant. This is equivalent to "except BaseException" block
        print("Never executed")