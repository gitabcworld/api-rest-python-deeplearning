#Run a Rebug server
from app import app

if __name__ == "__main__":
    try:      
        app.run(debug=False)                                                                        
    except Exception:
        app.logger.exception('Failed')
