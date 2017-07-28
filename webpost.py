
class BlogPost:
    def __init__(self , template,iden):
        self.template = template
        self.id=iden
        #self.img=img
    def listString(self):
     return "<a href=\"/post?page_id=" + str(self.id) + "\"></a>"

    def toDict(self):
        return {

        }



blog_list = [

 BlogPost(
 "stressfreeme.html" ,
 0 ,
 ) ,
 BlogPost(
 "thinkingbeing.html" ,
 1
 ) ,
 BlogPost(
 "Foodieforlife.html" ,
 2
 ) ,
 BlogPost(
 "Laugh.html" ,
 3
 ) ,
 BlogPost(
 "fitness_home.html" ,
 4
 )

]
