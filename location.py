class Action:
    def __init__(self, action_type, max_times, action):
        self.action_type = action_type
        self.times = 0
        self.times = max_times
        self.action = action

    def trigger():
        times += 1
        self.action()


class PlayerAction(Action):
    def __init__(self, times, key, description, action,):
        self.key = key
        self.description = description
        super(PlayerAction, self).__init__(f"player:{key}", action)


class Location:
    def __init__(self, short_desc, long_desc = [], same_room_short_desc = ""):
        self.short_desc_key = short_desc
        self.long_desc_keys = long_desc
        self.same_room_short_desc_key = same_room_short_desc
        self.custom_actions = {}

    def addAction(action):
        custom_actions[action.action_type] = action

    def triggerAction(action_type):
        action = self.custom_actions[action_type]
        action.trigger()
        if action.times >= action.max_times:
            del self.custom_actions[action_type]

    def triggerPlayerAction(key):
        self.triggerAction(f"player:{key}")

