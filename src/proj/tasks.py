import secrets

from celery import states
from celery.exceptions import Ignore, Reject
from celery.utils.log import get_task_logger

from .celery import app


logger = get_task_logger(__name__)


def random_str(size: int = 10) -> str:
    return secrets.token_hex(size)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task(
    bind=True,
    autoretry_for=(ZeroDivisionError,),
    retry_kwargs={"max_retries": 5},
)
def div(self, x, y):
    return x / y


@app.task(bind=True)
def get_tweets(self, user):
    timeline = random_str()
    if not self.request.called_directly:
        self.update_state(state=states.SUCCESS, meta=timeline)
    raise Ignore()


@app.task
def reject():
    raise Reject()


__all__ = ["add", "mul", "xsum"]
