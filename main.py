import webapp2
import sys
import jinja2
import os
from random import randint
from os import path
sys.path.append('source/')

from webpost import BlogPost
from webpost import blog_list

from foodindex import FoodPost
from foodindex import food_list

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

class JokeHandler(webapp2.RequestHandler):
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
        template = jinja_environment.get_template('Laugh.html')
        my_vars = {'haha' : joke_list[randnum]}
        self.response.out.write(template.render(my_vars))

class PhiloHandler(webapp2.RequestHandler):
    def get(self):
         philo_list= [ 'No mans knowledge here can go beyond his experience - John Lock ' ,
          'The unexamined life is not worth living - Socrates ' ,
          'Even while they teach, men learn - Seneca the Younger' ,
          'I would never die for my beliefs because I might be wrong -Bertrand Russell' ,
          'Religion is the sign of the oppressed, it is the opium of the people- Karl Marx' ,
          'There are only two people who can tell you the truth about yourself- an enemy who has lost his temper and a friend who loves you dearly -Antisthenes ' ,
          'God is a comedian playing to an audience too afraid to laugh.- Voltaire' ,
          'When what you hear and what you see do not match, trust your eyes.- Dale Renton' ,
          'I make a great difference between people. I choose my friends for their good looks, my acquaintances for their good characters, and my enemies for their good intellects. A man cannot be too careful in the choice of his enemies. I have not got one who is a fool. They are all men of some intellectual power, and consequently they all appreciate me. Is that very vain of me? I think it is rather vain. - The Picture of Dorian Gray'
         ]
         randnum = randint(0,(len(philo_list)-1))
         template = jinja_environment.get_template('thinkingbeing.html')
         my_vars = {'philo' : philo_list[randnum]}
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



#Jinja stuff form food page

def constructFoodListHTML():
    html_string = "<ol>\n"
    for i in range(0, len(food_list)):
        food_post = blog_list[i]
        html_string +=  food_post.listString(i) + "</li>"
    html_string += "</ol>"
    return html_string
#Recipe method
class RecipesHandler(webapp2.RequestHandler):
    def get(self):
        recipes_list = ['template/recipes/recipe1.html',
                        'template/recipes/recipe2.html',
                        'template/recipes/recipe3.html',
                        'template/recipes/recipe4.html',
                        'template/recipes/recipe5.html',
                        'template/recipes/recipe6.html'
                        ]

        randnum = randint(0,(len(recipes_list)-1))
        recipe_file = open(recipes_list[randnum], 'r')
        #this is where you reference your HTML file
        template = jinja_environment.get_template('template/Foodieforlife.html')
        my_vars = {'ListOfRecipes' : recipe_file.read(),"foodlist": constructFoodListHTML()}
        self.response.out.write(template.render(my_vars))

#Food Handler
class FoodHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        page_id =(self.request.get('page_id'))
        self.sendResponse(page_id, None)

def food(self):
        page_id = int(self.request.get('page_id'))
        self.sendResponse(page_id, self.request.get("comment"))

def sendResponse(self, page_id, new_comment):
        template = jinja_environment.get_template('template/foodindex.html')
        food_post = recipes_list[page_id]
        usersName = self.request.get("usersName_submission")
        commentHTML = food_post.commentsAsHTML(page_id, new_comment,usersName)
        usersName = self.request.get("usersName_submission")
        template_variables = {"title": food_post.title,
                              "content": food_post.content,
                              "comments": commentHTML,
                               }
        self.response.out.write(template.render(template_variables))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/post',PostHandler),
    ('/posttree', JokeHandler) ,
    ('/philo' , PhiloHandler) ,
    ('/recipes' , RecipesHandler) ,
    ('/food' , FoodHandler)
], debug=True)
