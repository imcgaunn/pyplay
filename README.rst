======
pyplay
======


An ASCII podcast player for the web. Nobody asked for it, but I could tell the
world wanted it. Add RSS feeds and browse podcasts in a boring way.

Its design is inspired by old terminals and jupyter notebooks.


Description
===========

Pyplay is a continuation of a podcast player I worked on in school
which suffered from a focus on fancy user-interface. Wanting something
very lightweight and cross-platform to stream my podcasts from, I decided
that I could write a serverless application to cache and index my podcasts
without too much effort, but potentially enormous benefit.

This application does not focus at all on fancy security features. When you
first start pyplay it generates a random token which gets saved into browser
local storage. This acts as your authentication token which you can use to
identify yourself should you need to use another browser (perhaps on another machine).

Your podcast subscriptions are stored in a dynamodb table named after the random
token generated at initialization time. The table stores a set of feed URLS
and some metadata about the feed:

 - up to date? (indicates whether all content has been cached for current state of feed)
 - cover photo url (or whatever the proper name is)

User Interface / Features
==============

- Text progress bar for audio
- Persist play state for session to dynamo
         (and subscriptions)

- added feeds should be text that looks like a hyperlink with cover image next to it
  this should all be aligned in a grid somehow.

- when you click hyperlink, replace cell with list of episodes that also look like hyperlinks
  with a '..' link at the top which transports you back to feed view.
- when you click an episode hyperlink, ask player to play it.
- There is a single player for the entire application which appears at the bottom.
  It has no controls, it only shows a progress percentage.
  You can stop and start audio once a file has been loaded using space.
