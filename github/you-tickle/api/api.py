from flask import Flask
import time
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

app = Flask(__name__)

@app.route('/api/time')
def current_time():
	return {'time':time.time()}

@app.route('/api/tickle/<w>')
def tickle(w):
	r=requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&type=video&regionCode=US&videoCaption=closedCaption&key=AIzaSyAse2tC8PBhU3vS9Vidu6JxqQSP7GSvHNw')
	video_ids = [r['id']['videoId'] for r in r.json()['items']]

	for step,vid in enumerate(video_ids):
		try:
			v_transcript = YouTubeTranscriptApi.get_transcript(vid)
		except (NoTranscriptFound, TranscriptsDisabled):
			continue
		for phrase in v_transcript:
			if w in phrase['text']:
				return {'link':vid,'phrase':phrase}