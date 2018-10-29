gameState = GameState()

class GameState:
    world = World() 
    hero = Hero(0, 0)

    def getPlayerLocation():
        return world.getAt(hero.x, hero.y)


class Action:
    def __init__(self, action_type, times, action):
        self.action_type = action_type
        self.times = times
        self.action = action

    def trigger():
        times -= 1
        self.action()


class PlayerAction(Action):
    def __init__(self, times, key, description, action,):
        self.key = key
        self.description = description
        super(PlayerAction, self).__init__(f"player:{key}", action)


class Location:
    def __init__(self):
        self.short_desc_key = ""
        self.long_desc_keys = []
        self.custom_actions = {}

    def addAction(action):
        custom_actions[action.action_type] = action

    def triggerAction(action_type):
        action = self.custom_actions[action_type]
        action.trigger()
        if action.times == 0:
            del self.custom_actions[action_type]

    def triggerPlayerAction(key):
        self.triggerAction(f"player:{key}")
