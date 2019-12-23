from routes import routes
from controllers.modules import *
from controllers.utility import *


class ApplicationHandler(Application):
    def __init__(self):
        handlers = routes.routes
        settings = dict(
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    parse_command_line()
    server = HTTPServer(ApplicationHandler())
    server.listen(os.environ.get("PORT", 9000))
    out = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    if stderr is not None:
        print("some error while reading ip address of machine")
        sys.exit()
    print(stdout)
    get_ip_token(stdout.decode("utf-8").split()[0])
    IOLoop.instance().start()