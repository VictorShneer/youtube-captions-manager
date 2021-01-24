from app import db
from flask import current_app
import redis
import rq

class Task(db.Model):
    # look primary key is STRING not Integer            WTF!? :D
    # because this id is NOT SQLAlchemy id
    # but RQ job identificator
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(128))
    complete = db.Column(db.Boolean, default=False)

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100

    @classmethod
    def launch_task(cls, name, description):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name)
        print('\n---job_id!!')
        print(rq_job.get_id())
        task = cls(id=rq_job.get_id(), name=name, description=description)
        print(task)
        db.session.add(task)
        print('----')
        return task

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256))
    expire = db.Column(db.Date())

    def delete_myself(self):
        db.session.delete(self)
        db.session.commit()