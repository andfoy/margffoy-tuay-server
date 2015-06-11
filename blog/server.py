#!/usr/bin/env python
import os
import sys


from swampdragon.swampdragon_server import run_server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

host_port = sys.argv[1] if len(sys.argv) > 1 else None

host_port = '0.0.0.0:9999'
run_server(host_port=host_port)
