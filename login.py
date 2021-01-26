#!/usr/bin/env python3
import os
import sys
import json
import secret 



	# print('Content-Type: text/html')
	# 	# seperate header and content
	# print()
	# print("""<!DOCTYPE html>	
	# <html>
	# <body>

	# """)
	# posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
	# if posted_bytes:
	#     posted = sys.stdin.read(int(posted_bytes))
	#     print(f"<p> POSTED: <pre>")
	#     for line in posted.splitlines():
	#         print(line)
	#     print("</pre></p>")

	# print("""
	# </body>
	# </html>
	# """)
	
	

def main():


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
	if ((tuple_array[0][1] == secret.username) and (tuple_array[1][1]  == secret.password) ):
		login_flag = True

	else :
		login_flag = False

	if (login_flag) :
		login_status = "Successful login"
		session_id = os.environ.get("GNOME_DESKTOP_SESSION_ID", 0)
		print("set-cookie: session_id = ",  session_id)
	else:
		login_status = "Unsuccessful login"


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
if __name__ == '__main__':

	main()
