from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

# HTML form template
html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Form</title>
</head>
<body>
    <h2>Submit Your Information</h2>
    <form action="/submit" method="post">
        <label for="firstname">First Name:</label>
        <input type="text" id="firstname" name="firstname" required><br><br>

        <label for="lastname">Last Name:</label>
        <input type="text" id="lastname" name="lastname" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" cols="30" required></textarea><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the form
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_form.encode())
        else:
            super().do_GET()  # Default handling for other GET requests

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # Parse the form data
            post_data = urllib.parse.parse_qs(post_data.decode())

            # Get the data from the form fields
            firstname = post_data.get('firstname', [''])[0]
            lastname = post_data.get('lastname', [''])[0]
            message = post_data.get('message', [''])[0]

            # Format the data and save it to the file
            data = f"First Name: {firstname}\nLast Name: {lastname}\nMessage: {message}\n\n"
            with open('submissions.txt', 'a') as file:
                file.write(data)

            # Respond with a success message
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Data saved successfully!")

        else:
            self.send_response(404)
            self.end_headers()

# Set up and run the HTTP server
def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8080)  # Listen on port 8080
    httpd = server_class(server_address, handler_class)
    print("Starting server at http://localhost:8080")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
