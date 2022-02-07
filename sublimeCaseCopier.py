import sublime
import sublime_plugin
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import _thread
import threading
import os
import platform


def MakeHandlerClassFromFilename(filename):
    class HandleRequests(BaseHTTPRequestHandler):
        def do_POST(self):
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                tests = json.loads(body.decode('utf8'))
                tests = tests["tests"]
                ntests = []
                sttt=""
                for test in tests:
                    sttt += test['input'].strip()
                k = os.path.split(filename)[0] +'/inputf.in'
                nfilename = k
                with open(nfilename, "w") as f:
                    f.write(sttt)
            except Exception as e:
                print("Error handling POST - " + str(e))
            threading.Thread(target=self.server.shutdown, daemon=True).start()
    return HandleRequests


class CompetitiveCompanionServer:
    def startServer(filename):
        host = 'localhost'
        port = 12345
        HandlerClass = MakeHandlerClassFromFilename(filename)
        httpd = HTTPServer((host, port), HandlerClass)
        httpd.serve_forever()
        print("Server has been shutdown")


class FastOlympicCodingHookCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            _thread.start_new_thread(CompetitiveCompanionServer.startServer,
                                     (self.view.file_name(),))
        except Exception as e:
            print("Error: unable to start thread - " + str(e))

