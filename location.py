from val_defs import *


class Action:
    def __init__(self, action_type, max_times, action):
        self.action_type = action_type.lower()
        self.times = 0
        self.max_times = max_times
        self.action = action

    def trigger(self):
        self.times += 1
        self.action()


class PlayerAction(Action):
    @staticmethod
    def getTypeString(key):
        return f"player:{key.lower()}"

    def __init__(self, max_times, key, description, action):
        self.key = key
        self.description = description
        super(PlayerAction, self).__init__(PlayerAction.getTypeString(key), max_times, action)


class Location:
    def __init__(self, short_desc, long_desc = [], same_room_short_desc = ""):
        self.short_desc_key = short_desc
        self.long_desc_keys = long_desc
        self.same_room_short_desc_key = same_room_short_desc
        self.custom_actions = {}

    def addAction(self, action):
        self.custom_actions[action.action_type] = action

    def triggerAction(self, action_type):
        action = self.custom_actions.get(action_type, None)
        if action == None:
            return
        if action.times + 1 >= action.max_times:
            # Delete action before it's triggered because action may add
            # another action of the same type
            del self.custom_actions[action_type]
        action.trigger()

    def triggerPlayerAction(self, key):
        self.triggerAction(PlayerAction.getTypeString(key))

    def getLongDescription(self):
        global long_descriptions
        full_desc = ""
        for desc_key in self.long_desc_keys:
            full_desc += long_descriptions[desc_key] + "\n"
        return full_desc

    def getShortDescription(self):
        global short_descriptions
        return short_descriptions[self.short_desc_key]

    def getSameRoomDescription(self):
        global short_descriptions
        return short_descriptions[self.same_room_short_desc_key]

    def getPlayerActionsDescription(self):
        desc = ""
        for act_type in self.custom_actions:
            if act_type.startswith("player"):
                act = self.custom_actions[act_type]
                desc += f"[{act.key}] {act.description}\n"
        return desc

