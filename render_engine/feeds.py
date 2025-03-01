"""
The Feeds Logic That Makes Up RSS and ATOM FeedTypes.
This is the base files and should only contain the params identified by the
standards defined.
RSS: http://www.rssboard.org/rss-specification
JSON: https://jsonfeed.org/version/1
"""

from collections import namedtuple
from datetime import datetime

import jinja2
from jinja2 import PackageLoader, Template, select_autoescape

from .page import Page


def to_pub_date(value: datetime):
    """
    Parse information from the given class object.
    """
    return value.to_rfc2822_string()


rss_feed_engine = jinja2.Environment(
    loader=PackageLoader("render_engine", "templates"),
    autoescape=select_autoescape(enabled_extensions=("rss")),
    trim_blocks=True,
)
rss_feed_engine.filters["to_pub_date"] = to_pub_date
feed_template = rss_feed_engine.get_template("rss2.0.xml")


class RSSFeed(Page):
    """The RSS Feed Component of an Archive Object"""

    template: Template = feed_template
    extension: str = "rss"
