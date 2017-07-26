import webapp2
import sys
import jinja2
import os
from random import randint

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
       joke_list = ['The only time incorrectly isn\'t spelled incorrectly is when it\'s spelled incorrectly.'
        , 'Escalators don\'t break down... they just turn into stairs' ,
        'I intend to live forever... or die trying' ,
        'A blind man walks into a bar....And a table, and a chair' ,
        'We never knew he was a drunk... until he showed up to work sober' ,
        'A clear conscience is usually the sign of a bad memory' ,
         'I used to be in a band, we were called \'lost dog\'. You probably saw our posters' ,
         'I childproofed the house... but they still get in!' ,
         'Want to hear a pizza joke? nah, it\'s too cheesy. What about a construction joke? Oh never mind, I\'m still working on that one. Did you hear the one about the rope? Skip it. Have you heard the one about the guy in the wheelchair? Never mind, it\'s too lame.'
         , 'I used to think the brain was the most important organ. Then I thought, look what\'s telling me that.' ,
          'Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.'
            ]
        randnum = randint(0,(len(joke_list)-1))
        #this is where you reference your HTML file
        template = jinja_environment.get_template('templates/dummy.html')
        my_vars = {'haha' : joke_list[randnum]}
        self.response.out.write(template.render(my_vars))

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
