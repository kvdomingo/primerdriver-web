import os

from django.templatetags.static import static
from django.urls import reverse
from django.conf import settings
from primerdriver.version import __version__
from jinja2 import Environment
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

_SHORT_SHA = os.environ.get("SHORT_SHA")


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "now": datetime.now(),
            "program_version": __version__,
            "settings": settings,
            "static": static,
            "url": reverse,
            "web_version": _SHORT_SHA if _SHORT_SHA else __version__,
        }
    )
    return env
