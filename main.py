import webapp2
import sys
import jinja2
import os

from os import path
sys.path.append('source/')

from webpost import BlogPost
from webpost import blog_list

#setting up the Environment for jinja
#that sets jinja's relative directory to match the directory's name
template_dir = path.join(path.dirname(__file__) , 'template')
jinja_environment  = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir))


def constructBlogListHTML():
    #blog_list = constructBlogList()
    html_string = "<ol>\n"
    for i in range(0 , len(blog_list)):
        blog_post = blog_list[i]
        html_string += "<li>" + str((blog_post.listString())) + "</li>"
    html_string += '</ol>'
    return html_string

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        #this is where you reference your html file
        template = jinja_environment.get_template('index.html')
        template_variables = {'bloglist':constructBlogListHTML()}
        self.response.out.write(template.render(template_variables))

class PostHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        page_id = self.request.get('page_id')
        if not page_id:
            page_id=0
        else:
            page_id= int(page_id)
        blog_post = blog_list[page_id]

        template = jinja_environment.get_template(blog_post.template)
        template_variables = {}
        self.response.out.write(template.render(template_variables))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post',PostHandler)
], debug=True)
