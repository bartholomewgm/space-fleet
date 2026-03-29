class CrewMember:
    def __init__(self, member_id, name, role):
        self.member_id = member_id
        self.name = name
        self.role = role

    def to_dict(self):
        return {
            "id": self.member_id,
            "name": self.name,
            "role": self.role
        }
