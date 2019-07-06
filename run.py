# under normal circumstances, this script would not be necessary. the
# sample_application would have its own setup.py and be properly installed;
# however since it is not bundled in the sdist package, we need some hacks
# to make it work

import os
import sys

from flask import Flask
from app import create_app


# create an app instance
app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
