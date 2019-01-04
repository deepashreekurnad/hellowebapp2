import webapp2
import os
from google.appengine.ext.webapp import template
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'static/index.html') 
        self.response.out.write(template.render(path, {})) 


def main():
    app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ], debug=True)
if __name__ == '__main__':
    main()
