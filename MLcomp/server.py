from waitress import serve
import os
    
from MLcomp.wsgi import application
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    try:
        serve(application, port=port)
    except Exception as e:
        print(e)