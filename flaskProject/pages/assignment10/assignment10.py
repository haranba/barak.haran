from flask import Flask, render_template, request, Blueprint, redirect
import mysql.connector

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')



