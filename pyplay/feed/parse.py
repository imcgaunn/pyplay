# functions for parsing RSS feed data
import json

import feedparser


class PodcastJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, PodcastEntry):
            return {'title': o.title,
                    'links': o.audio_ref,
                    'summary': o.summary,
                    'id': o.id}
        elif isinstance(o, PodcastFeed):
            return {'title': o.title,
                    'artwork': o.artwork_uri,
                    'entries': o.entries,
                    'summary': o.summary,
                    'date': o.updated,
                    'publisher': o.pub_detail}


class PodcastEntry(object):
    def __init__(self, parser_entry):
        self._raw = parser_entry

    @property
    def title(self):
        return self._raw['title']

    @property
    def audio_ref(self):
        links = self._raw['links']
        audio = [l for l in links
                 if 'audio' in l['type']]
        return audio

    @property
    def published(self):
        return self._raw['published']

    @property
    def summary(self):
        return self._raw['summary']

    @property
    def id(self):
        return self._raw['id']


class PodcastFeed(object):
    def __init__(self, raw):
        self._raw = raw
        self._parsed = feedparser.parse(self._raw)
        self._parsed_feed = self._parsed['feed']
        self._parsed_entries = self._parsed['entries']

    @property
    def title(self):
        return self._parsed_feed['title']

    @property
    def artwork_uri(self):
        return self._parsed_feed['image']['href']

    @property
    def summary(self):
        return self._parsed_feed['summary']

    @property
    def updated(self):
        return self._parsed_feed['date']

    @property
    def pub_detail(self):
        return self._parsed_feed['publisher_detail']

    @property
    def entries(self):
        return [PodcastEntry(e)
                for e in self._parsed_entries]

