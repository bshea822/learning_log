"""Helper functions that can be used to improve readability in views.py"""

from django.http import Http404

def check_topic_owner(topic_owner, current_user):
    """Checks if the current user matches to the owner of the content."""

    if topic_owner != current_user:
        raise Http404
