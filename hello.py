#!/usr/bin/env python3
import os
import json
import sys
from templates import secret_page
import secret 
# from cgi import escape
# This CGI script

# design for  return posted data, according to saved login status,  
# where login matched, it is should return, inputted valued
def status_check():
	posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
	tuple_array = []
	# checking login status
	login_flag = False
	if posted_bytes:
		posted = sys.stdin.read(int(posted_bytes))
		for line in posted.splitlines():
			# print("The line is :",line)
			# print()
			for parameter in line.split('&'):
				(name, value) = parameter.split('=')
				tuple_array.append((name,value))
	
	# after saved, 
	if (tuple_array != [] ):
		if ((tuple_array[0][1] == secret.username) and (tuple_array[1][1]  == secret.password) ):

			login_flag = True
		else :
			login_flag = False

	return tuple_array, login_flag

def set_cookie(login_flag):
	if (login_flag) :
		login_status = "login, "
		session_id = os.environ.get("GNOME_DESKTOP_SESSION_ID", 0)
		print("Set-Cookie: session_id = ",  session_id, "; Max-Age=30")
		print("Set-Cookie: username = ",  secret.username, "; Max-Age=30")
		print("Set-Cookie: password = ",  secret.password, "; Max-Age=30")
		print("Set-Cookie: log_in = True; Max-Age=30")
	else:
		login_status = "login failed"
	return login_status
	


#design for after login action, i.e. post request/submit  sent from Client
def submit_action(login_status, tuple_array):


	print('Content-Type: text/html')
	# seperate header and content
	print()
	print("""<!DOCTYPE html>    
	<html>
	<body>

	""")
	print(f"<h1> {login_status} posting data</h1>")


	print(f"<p> POSTED: <pre>")
	for i in range(len(tuple_array)):
		print(f"<li><em>{tuple_array[i][0] } </em> = {tuple_array[i][1] } </li>")
	print("</pre></p>")


	print("""
	</body>
	</html>
	""")
	pass

def login_page():
	"""
	Returns the HTML for the login page.
	"""
	return _wrapper(r"""
	<!DOCTYPE html> 
	<html>
	<body>
	<h1> Welcome! </h1>

	<form method="POST" >
		<label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
		<label> <span>Password:</span> <input type="password" name="password"></label>

		<button type="submit"> Login! </button>
	</form>
	</body>
	</html>
	""")

def _wrapper(page):
	"""
	Wraps some text in common HTML.
	"""
	return ("""
	<!DOCTYPE HTML>
	<html>
	<head>
		<meta charset="utf-8">
		<style>
			body {
				font-family: -apple-system, BlinkMacSystemFont, sans-serif;
				max-width: 24em;
				margin: auto;
				color: #333;
				background-color: #fdfdfd
			}

			.spoilers {
				color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
			}
			.spoilers:hover {
				transition: color 250ms;
				color: rgba(36, 36, 36, 1)
			}

			label {
				display: flex;
				flex-direction: row;
			}

			label > span {
				flex: 0;
			}

			label> input {
				flex: 1;
			}

			button {
				font-size: larger;
				float: right;
				margin-top: 6px;
			}
		</style>
	</head>
	<body>
	""" + page + """
	</body>
	</html>
	""")




def main():
	client_request = os.environ.get("REQUEST_METHOD",0) # always exist, this is better optimizion, can be added later on
	client_cookie  = os.environ.get("HTTP_COOKIE", 0) # either ""
	client_query = os.environ.get("QUERY_STRING", 0)  # might not exist
	client_agent = os.environ.get("HTTP_USER_AGENT",0) # for q3
	tuple_array = []

	# deisgn for cookie selection and check secret status
	cookie_tuple_array = []
	secrete_flag =False
	# login_status = False
	
	if (client_cookie != "") :

		for parameter in client_cookie.split(';'):
			(name, value) = parameter.strip().split('=')
			cookie_tuple_array.append((name,value))
		# if (cookie_tuple_array[0][0] == os.environ.get("GNOME_DESKTOP_SESSION_ID", 0) ):
		for t in cookie_tuple_array:
			if (t[0] == "log_in"):
				secrete_flag = True
			else:
				secrete_flag = False
	else :
		# print(login_page())
		secrete_flag = False
	# if (client_request != " "):
	# 	pass
	tuple_array, login_flag = status_check();
	login_status = set_cookie(login_flag);
	# #q1
	# print('Content-Type: application/json')
	# # seperate header and content, q1
	# print()
	# # check in web, we use json 
	# print(json.dumps(dict(os.environ), indent=2))
	#####Q2
	# localhost:8080/hello.py?boo=yogi
	print('Content-Type: text/html')
	# seperate header and content
	print()
	print("""<!DOCTYPE html>
	<html>
	<body>
	<h1>HELLO</h1>
	""")
	print("<ul>")



	if ( not client_query) :
		# query not exist
		print(f"<p> no query: </p>")
	else:
		print(f"<p> QUERY_STRING:{client_query} </p >")
		for parameter in client_query.split('&'):
		    (name, value) = parameter.split('=')
		    print(f"<li><em>{name} </em> = {value} </li>")

	if(not client_agent):
		print(f"<p> no agent exist: </p>")
	else:
		print(f"<p> user browser:{client_agent} </p >")
	print("cookie_tuple_array", cookie_tuple_array)
	print("secret_flag: ",secrete_flag)

	if (secrete_flag ) :
		print(secret_page(secret.username, secret.password))
	else:
		
		submit_action(login_status, tuple_array);
		print(login_page())

	print("""
	</ul>
	</body>
	</html>
	# """)

		

if __name__ == '__main__':

	main()
