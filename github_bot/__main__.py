from octomachinery.app.routing import process_event_actions
from octomachinery.app.routing.decorators import process_webhook_payload
from octomachinery.app.runtime.context import RUNTIME_CONTEXT
from octomachinery.app.server.runner import run as run_app


@process_event_actions('issues', {'opened'})
@process_webhook_payload
async def on_issue_opened(
        *,
        action, issue, repository, sender, installation,
        assignee=None, changes=None,
):
    """Whenever an issue is opened, greet the author and say thanks."""
    github_api = RUNTIME_CONTEXT.app_installation_client
    comments_api_url = issue["comments_url"]
    author = issue["user"]["login"]
    message = (
        f"Thanks for the report @{author}! "
        "I will look into it ASAP! (I'm a bot 🤖)."
    )
    await github_api.post(comments_api_url, data={"body": message})


@process_event_actions('issue_comment', {'created'})
@process_webhook_payload
async def on_comment_created(
        *,
        action, issue, comment, repository=None, sender=None,
        installation=None,
        assignee=None, changes=None,
):
    """Whenever an comment is posted, like it."""
    github_api = RUNTIME_CONTEXT.app_installation_client
    comment_reactions_api_url = f'{comment["url"]}/reactions'

    await github_api.post(
        comment_reactions_api_url,
        preview_api_version='squirrel-girl',
        data={"content": "+1"},
    )


if __name__ == "__main__":
    run_app(
        name='PyCon-Bot-by-webknjaz',
        version='1.0.0',
        url='https://github.com/apps/pyyyyyycoooon-booooot111',
    )
