class Spaceship:
    def __init__(self, spaceship_id, name, type_, status="available"):
        self.spaceship_id = spaceship_id
        self.name = name
        self.type_ = type_
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def to_dict(self):
        return {
            "id": self.spaceship_id,
            "name": self.name,
            "type": self.type_,
            "status": self.status
        }
