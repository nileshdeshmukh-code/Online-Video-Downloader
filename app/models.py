
class Modelstream:
    def __init__(self,itag,resolution,mime_type,type):
        self.itag=itag
        self.resolution=resolution
        self.mime_type=mime_type
        self.type=type
    
    

class ModelVideo:

    def __init__(self):
        self.title=""
        self.duration=""
        self.thumbnail=""

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,val):
        self.__title=val

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self,val):
        self.__duration=val
    
    @property
    def thumbnail(self):
        return self.__thumbnail
    @thumbnail.setter
    def thumbnail(self,val):
        self.__thumbnail=val
    





    
        



    
