class ServerState(object):
    def __init__(self, sess_id):
        self.session_id = sess_id
        self.dbh = None

    @property
    def subscriptions(self):
        return None

    @property
    def player_states(self):
        return None
