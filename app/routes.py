from http.client import HTTPException
from flask import render_template, send_file,  request,session,jsonify
from app import app
from app.models import ModelVideo
from app.data import Video



@app.route("/search",methods=['POST'])
def search():  
    try:
        url = request.form["url"]
        session["url"]=url
        obj=Video(url) 
        mvideo=ModelVideo()
        mvideo=obj.getdetails()      
        return jsonify({'htmlresponse': render_template ('response.html',data={'stream': obj.getstream(),'title':mvideo.title,'thumbnail':mvideo.thumbnail,'duration':mvideo.duration})})
    
    except Exception as e: 
        session["url"]=""
        if type(e).__name__=="RegexMatchError" :
            raise Exception("The download link not found, Please paste valid video link.")  
        else:         
            raise e
            

@app.route("/")
def index():
    try:
        session["url"]=""
        return render_template("index.html")    
    except Exception as e:
        raise e

def mark_download_as_complete(itag):
    pass


@app.route("/download/<int:itag>/")
def download(itag):
    try:     
        obj=Video(session["url"])     
        data= obj.download(itag)         
        return send_file(data[0],as_attachment=True,download_name=data[1],mimetype=data[2])
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

