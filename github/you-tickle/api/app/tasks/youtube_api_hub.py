from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import random
topic_ids = ["/m/04rlf","/m/05fw6t","/m/02mscn","/m/0ggq0m","/m/01lyv","/m/02lkt","/m/0glt670","/m/05rwpb","/m/03_d0","/m/028sqc","/m/0g293","/m/064t9","/m/06cqb","/m/06j6l","/m/06by7","/m/0gywn","/m/0bzvm2","/m/025zzc","/m/02ntfj","/m/0b1vjn","/m/02hygl","/m/04q1x3q","/m/01sjng","/m/0403l3g","/m/021bp2","/m/022dc6","/m/03hf_rm","/m/06ntj","/m/0jm_","/m/018jz","/m/018w8","/m/01cgz","/m/09xp_","/m/02vx4","/m/037hz","/m/03tmr","/m/01h7lh","/m/0410tth","/m/066wd","/m/07bs0","/m/07_53","/m/02jjt","/m/095bb","/m/09kqc","/m/02vxn","/m/05qjc","/m/019_rr","/m/032tl","/m/027x7n","/m/02wbm","/m/0kt51","/m/03glg","/m/068hy","/m/041xxh","/m/07c1v","/m/07bxq","/m/07yv9","/m/01k8wb","/m/098wr"]


def get_video_bunch():

    DEVELOPER_KEY = '***'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    ## TODO typeVidoe - short
    search_response = youtube.search().list(
    part='snippet',
    maxResults=25,
    videoCaption='closedCaption',
    type='video',
    regionCode='US',
    relevanceLanguage='en',
    topicId=random.choice(topic_ids)
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))

    return videos

def build_captions_list(video_ids):
    result = []
    for step,video_id in enumerate(video_ids):
        print(step,video_id, len(video_ids))
        try:
            captions = YouTubeTranscriptApi.get_transcript(video_id)
        except:
            continue
        result.append({'caption':captions, 'video_id':video_id})
        print(len(captions))
        print('---*---')
    return result


