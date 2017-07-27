# A Blog Post class
# Also manages comments for the post
from google.appengine.ext import ndb

class CommentsData(ndb.Model):
    comment_page_id = ndb.IntegerProperty()
    comment_string = ndb.StringProperty(repeated=True)
    comment_userName = ndb.StringProperty()

class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def listString(self, page_id):
        return "<a href='post?page_id=" + str(page_id) + "'>" + self.title + "</a>"


    def commentsAsHTML(self, page_id, new_comment,usersName):
        comments_query = CommentsData.query(CommentsData.comment_page_id == page_id)
        comments_data = comments_query.get()
        if comments_data == None:
            if new_comment == None:
                return "<p> No Recipes Yet...</p>"
            else:
                comment_list = [ new_comment ]
                comments_data = CommentsData(comment_page_id = page_id,
                                             comment_string = comment_list,
                                             comment_userName= usersName)
                comments_data.put()
                return "<p>" + usersName + "</p>" + "<p>" + new_comment + "</p>"

        else:
            if new_comment != None:
                comments_data.comment_string.append(usersName+":")
                comments_data.comment_string.append(new_comment)
            html_string = ""
            for comment in comments_data.comment_string:

                html_string += "<p>" + comment + "</p>"
            if new_comment != None:
                comments_data.put()
            return html_string
blog_list = [
    BlogPost("Enter your Recipes",
             "Thanks for sharing, Keep It Up! "),
]
