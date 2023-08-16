from  app.custom_packages.pytube import YouTube
from io import BytesIO
from app.models import Modelstream,ModelVideo

class Video:
    def __init__ (self,url):
        self.url=url        
    def getstream(self): 
        try:
            result=[]           
            obj=YouTube(self.url)         
            #data=obj.streams.filter(progressive=True, file_extension='mp4').all()      
            data=obj.streams
            video=data.filter(progressive=True, file_extension='mp4').all()
            audio=data.filter(type='audio', progressive=False, abr='160kbps').all()         
            for i in video:
                obj=Modelstream(i.itag,i.resolution,i.mime_type,i.type)            
                result.append(obj)
            for i in audio:
                print(i)
                obj=Modelstream(i.itag,i.resolution,i.mime_type,i.type)            
                result.append(obj)
            return result 
        except Exception as e:
            raise e
    def getdetails(self):
        try:
            obj=YouTube(self.url) 
            data=ModelVideo()
            data.thumbnail=obj.thumbnail_url
            data.title=obj.title
            data.duration=obj.length
            return data
        except Exception as e:
            raise e

         
    def download(self,itag):
        try:
            buffer = BytesIO()  
            obj=YouTube(self.url)        
            video = obj.streams.get_by_itag(itag)
            video.stream_to_buffer(buffer)            
            buffer.seek(0)     
            return buffer,video.default_filename,video.mime_type
        except Exception as e:
            raise e