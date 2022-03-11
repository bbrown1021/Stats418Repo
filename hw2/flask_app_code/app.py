from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from utilities import match_query, rate_movie

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():
   title = request.form.get('title')

   if title:
       print('Request for result page received with title=%s' % title)
       xml_result = match_query(title)
       return render_template('results.html', title = title, xml_result = xml_result[0], poster = xml_result[1])
   else:
       print('Request for result page received with no title or blank title -- redirecting')
       return redirect(url_for('index'))

@app.route('/user_rating', methods=['POST'])
def user_rating():
  username = request.form.get('username')
  movie = request.form.get('movie')
  rating = request.form.get('rating')

  if username and movie and rating:
    print('Request for user rating page received with username=%s' % username)
    message = rate_movie(username, movie,rating)
    return render_template('user_rating.html', username = username, message = message)
  else:
    print('Request for user rating page received with no username, movie, or rating -- redirecting')
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()
