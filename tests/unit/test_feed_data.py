from pyplay.feed.parse import parse_feed


def test_PodcastEntry(feed_data):
    processed = parse_feed(feed_data)
    entries = processed.entries

    assert processed.summary
    assert processed.artwork_uri
    assert processed.entries
    assert processed.title
    assert processed.pub_detail

    for e in entries:
        assert e.summary
        assert e.published
        assert e.audioRef
        assert e.title
        assert e.id
