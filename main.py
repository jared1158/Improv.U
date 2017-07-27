import jinja2
import os
import webapp2
import sys
from random import randint

from os import path
sys.path.append('source/')

from blogpost import BlogPost
from blogpost import blog_list

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def constructBlogListHTML():
    html_string = "<ol>\n"
    for i in range(0, len(blog_list)):
        blog_post = blog_list[i]
        html_string +=  blog_post.listString(i) + "</li>"
    html_string += "</ol>"
    return html_string



class RecipesHandler(webapp2.RequestHandler):
    def get(self):
        recipes_list = ['templates/recipes/recipe1.html',
                        'templates/recipes/recipe2.html',
                        'templates/recipes/recipe3.html',
                        'templates/recipes/recipe4.html',
                        'templates/recipes/recipe5.html',
                        'templates/recipes/recipe6.html'

                       ]

        randnum = randint(0,(len(recipes_list)-1))
        recipe_file = open(recipes_list[randnum], 'r')
        #this is where you reference your HTML file
        template = jinja_environment.get_template('templates/index.html')
        my_vars = {'ListOfRecipes' : recipe_file.read(),"bloglist": constructBlogListHTML()}
        self.response.out.write(template.render(my_vars))



class PostHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        page_id = int(self.request.get('page_id'))
        self.sendResponse(page_id, None)

    def post(self):
        page_id = int(self.request.get('page_id'))
        self.sendResponse(page_id, self.request.get("comment"))

    def sendResponse(self, page_id, new_comment):
        template = jinja_environment.get_template('templates/blogpost.html')
        blog_post = blog_list[page_id]
        usersName = self.request.get("usersName_submission")
        commentHTML = blog_post.commentsAsHTML(page_id, new_comment,usersName)
        usersName = self.request.get("usersName_submission")
        template_variables = {"title": blog_post.title,
                              "content": blog_post.content,
                              "comments": commentHTML,
                               }
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([

    ('/', RecipesHandler),
    ('/post', PostHandler)
], debug=True)
