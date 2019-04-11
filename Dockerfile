FROM python:3.7-slim

LABEL "maintainer"="Sviatoslav Sydorenko <wk+github-actions@sydorenko.org.ua>"
LABEL "repository"="https://github.com/webknjaz/comment-reactor-pyconsk-324"
LABEL "homepage"="https://github.com/webknjaz/comment-reactor-pyconsk-324"

LABEL "com.github.actions.name" "comment-reactor-pyconsk-324"
LABEL "com.github.actions.description" "Add Deploy buttons to Checks pages for each commit"
LABEL "com.github.actions.icon" "play"
LABEL "com.github.actions.color" "green"

ADD . /usr/src/comment-reactor-pyconsk-324
RUN pip install -r /usr/src/comment-reactor-pyconsk-324/requirements.txt

ENV PYTHONPATH /usr/src/comment-reactor-pyconsk-324

ENTRYPOINT ["python", "-m", "github_bot.action"]
