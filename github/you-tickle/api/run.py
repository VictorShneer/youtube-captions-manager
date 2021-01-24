from app import create_app
from app import db
from app.models import Task

app = create_app()

@app.cli.command()
def drop_bunch_of_random_video_captions():
    task = Task.launch_task('regular_upload.get_and_process_bunch_of_videos', 'youtube request')
    db.session.commit()
    print('CLI command run!')
