import json

from pyplay.feed.parse import PodcastFeed, PodcastJSONEncoder


def test_PodcastEntry(feed_data):
    processed = PodcastFeed(feed_data)
    entries = processed.entries

    assert processed.summary
    assert processed.artwork_uri
    assert processed.entries
    assert processed.title
    assert processed.pub_detail
    assert processed.updated

    for e in entries:
        assert e.summary
        assert e.published
        assert e.audio_ref
        assert e.title
        assert e.id


def test_PodcastJSONEncoder(feed_data):
    feed = PodcastFeed(feed_data)
    res = json.dumps(feed, cls=PodcastJSONEncoder)
    assert res
