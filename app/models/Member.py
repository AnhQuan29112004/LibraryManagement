class Member:
    def __init__(self):
        pass
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        member = Member(data['member_id'], data['name'], data['phone'], data['cccd'], data['address'])
        member.borrowed_books = data.get('borrowed_books', [])
        return member