from flask import current_app
from api.app.models import Token
from api.app.main.utils import request_new_token
from api.app.main.utils import write_captions
from api.app.tasks.youtube_api_hub import get_video_bunch
from api.app.tasks.youtube_api_hub import build_captions_list
from api.app import create_app
from api.app import db
import datetime

app = create_app()
app.app_context().push()

def refresh_token(function):
    def wrapper():
        token = Token.query.first()
        if not token or datetime.date.today()>=token.expire:
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            token_string = request_new_token()
            token = Token(id = 0, token=token_string, expire=tomorrow)
            db.session.add(token)
            db.session.commit()
            # TODO check if it ok?

        return function()
    # Renaming the function name:
    wrapper.__name__ = function.__name__
    return wrapper


@refresh_token
def get_and_process_bunch_of_videos():
    video_ids = get_video_bunch()    
    captions_list = build_captions_list(video_ids)
    token = Token.query.first().token
    for captions in captions_list:
        response = write_captions(captions, token)
        print(response.text)