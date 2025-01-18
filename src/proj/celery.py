from celery import Celery

app = Celery(
    "prof",
    backend="redis://localhost:6379/0",
    broker="redis://localhost:6379/0",
    include=["proj.tasks"],
)


if __name__ == "__main__":
    app.start()
