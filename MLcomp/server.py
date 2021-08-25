from waitress import serve
    
from MLcomp.wsgi import application
    
if __name__ == '__main__':
    try:
        serve(application, port='8000')
    except Exception as e:
        print(e)