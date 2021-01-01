from flask import Flask, render_template
import time
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

app = Flask(__name__, static_folder='../build', static_url_path = '/', template_folder='../build')


@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/time')
def current_time():
	return {'time':time.time()}

@app.route('/api/tickle/<w>')
def tickle(w):
	r=requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&type=video&regionCode=US&videoCaption=closedCaption&key=AIzaSyAse2tC8PBhU3vS9Vidu6JxqQSP7GSvHNw')
	video_ids = [r['id']['videoId'] for r in r.json()['items']]
	print('hey')
	for step,vid in enumerate(video_ids):
		try:
			v_transcript = YouTubeTranscriptApi.get_transcript(vid)
		except (NoTranscriptFound, TranscriptsDisabled):
			continue
		for phrase in v_transcript:
			if w in phrase['text']:
				return {'link':vid,'phrase':phrase}