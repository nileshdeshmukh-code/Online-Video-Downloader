from http.client import HTTPException, InvalidURL, responses
import json
from app import app
from flask import render_template,request,jsonify


@app.errorhandler(Exception)
def handle_http_exception(e):   
    status_code = 500
    success = False
    response = {
        'success': success,
        'status_code':status_code,
        'error': {
            'type': type(e).__name__,
            'message': str(e)
        }
    }
    return jsonify({'htmlresponse': render_template ('error.html',data= response)})


    



 