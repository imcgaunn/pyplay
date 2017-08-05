import json


def info(ev, ctx):
    import pprint
    pprint.pprint(ev)
    headers = ev['headers']
    body = ev['body']

    url = body['url']

    return {
        'responseCode': 200,
        'body': json.dumps({})
    }


# def init(sess_token, host=None):
#    """ all transactions need to pass around the session token
#    that was provided to init when client started.
#
#    when client first starts, it calls this method and supplies
#    its session token.
#
#    If a backend table exists for that session token, this method
#    returns a serialized version of the server's copy of the user's
#    state.
#
#    If not, create a new backend table for token and load a default
#    state.
#
#    """
#
#    pass


def update_state(sess_id, state):
    """ replaces backend state for session identified by
        :param sess_id with
        :param state

    called when user adds a podcast, and before
    window is closed.
    """
    pass
