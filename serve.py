#python3
"""
Script for running a simple test server, with the `output/` directory as root.
"""


import http.server
import socketserver
import os 
import sys

if __name__ == "__main__":
    port = 8000

    old_cwd = os.getcwd()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    web_dir = os.path.join(root_dir, "output")

    try:
        os.chdir(web_dir)
        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", port), Handler)

        print("serving at port", port)
        httpd.serve_forever()

    except KeyboardInterrupt as e:
        print("\nShutting down...")

    except Exception as e:
        raise(e)

    finally:
        os.chdir(old_cwd)