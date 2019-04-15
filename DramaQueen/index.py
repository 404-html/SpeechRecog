from __future__ import print_function
import cgi, cgitb

def index(req):
    postData = req.form
    json = str(postData['fileName'])
    print(json)
