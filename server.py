import json
from http.server import BaseHTTPRequestHandler, HTTPServer


# Функция для загрузки модели данных из JSON
def load_data():
    with open('model.json') as json_file:
        return json.load(json_file)


# Функция для загрузки и рендеринга HTML-шаблона
def render_template(template_path, context):
    with open(template_path, 'r') as file:
        template = file.read()
        for key, value in context.items():
            placeholder = '{{ ' + key + ' }}'
            template = template.replace(placeholder, value)
        return template


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            data = load_data()
            content = render_template('template.html', data)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    run() #http://localhost:8000
