#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

#class Signup(webapp2.RequestHandler):
form = """
    <form action = "/" method = "post">
    <h1 style="color:red;font-size:48px">Signup</h1>
    <br>
    <br>
        <label>
            username<input type = "text" name="username" value="%(username)s"/>%(user_error)s
        </label>
        <br>
        <br>
        <label>
            password<input type="password" name="password">%(password_error)s
        </label>
        <br>
        <br>
        <label>
            verify password<input type="password" name="verify">%(verify_error)s
        </label>
        <br>
        <br>
        <label>
                email(optional)<input type="text" name="email"%(email)s"/>%(email_error)s
        </label>
        <br>
        <br>
        <input type="submit">
    </form>
    """
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
 return USER_RE.match(username)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
   return username and USER_RE.match(username)

PASS_Re = re.compile(r"^.{3,20}$")
def valid_password(password):
   return password and PASS_Re.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
   return not email or EMAIL_RE.match(email)


class MainHandler(webapp2.RequestHandler):
   def error_message(self, user_error="",username="",password_error="",
   verify_error="",email_error="",email=""):
      self.response.write(form %{'user_error':user_error,
                                   "username":username,
                                   'password_error':password_error,
                                   'verify_error':verify_error,
                                   'email_error':email_error,
                                   'email':email
                                   })

   def get(self):
       self.error_message()

   def post(self):
       have_error = False
       username = self.request.get('username')
       password = self.request.get('password')
       verify = self.request.get('verify')
       email = self.request.get('email')
       user_error, password_error, verify_error, email_error = "","","", "",

#        pars = dict(user_name=user_name,email=email)
       if not valid_username(username):
           user_error="Invalid username."
           have_error = True

       if not valid_password(password):
           password_error="Invalid password."
           have_error = True
       elif password != verify:
           verify_error ="Incorrect password."
           have_error = True

       if not valid_email(email):
           email_error = "Invalid email."
           have_error = True

       if not have_error:
           self.redirect('/Welcome?username={}'.format(username))

       #self.render(form%pars)
       self.error_message(user_error=user_error,password_error=password_error,verify_error=verify_error,email_error=email_error)



class Welcome(webapp2.RequestHandler):
   def get(self):
       username = self.request.get("username")
       self.response.write(" Welcome "+ username +" you did it! ")



#class MainHandler(webapp2.RequestHandler):
   #def get(self):
       #self.response.write('Hello World')


    #def get(self):
app = webapp2.WSGIApplication([
   ('/', MainHandler),
   ('/Welcome',Welcome)
], debug=True)        #self.response.write(self.form)

#app = webapp2.WSGIApplication([
    #('/', MainHandler)
#], debug=True)
