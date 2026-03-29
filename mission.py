class Mission:
    def __init__(self, mission_id, name, goal, status="planned"):
        self.mission_id = mission_id
        self.name = name
        self.goal = goal
        self.status = status
        self.spaceships = []

    def add_spaceship(self, spaceship):
        self.spaceships.append(spaceship)

    def to_dict(self):
        return {
            "id": self.mission_id,
            "name": self.name,
            "goal": self.goal,
            "status": self.status,
            "spaceships": [s.to_dict() for s in self.spaceships]
        }
