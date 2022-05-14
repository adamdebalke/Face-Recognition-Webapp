from flask import render_template, request
from flask import redirect, url_for
import os

UPLOAD_FLODER = 'static/uploads'
def base():
    return render_template('base.html')







