from controllers.modules import *


class AudioStreamHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    @coroutine
    def get(self):
        self.write(json.dumps({
            "status": status,
            "message": message,
        }))

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        json_data = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(json_data))

    def options(self):
        self.set_status(204)
        self.finish()
