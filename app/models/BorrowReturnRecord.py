class BorrowReturnRecord:
    def __init__(self):
        pass
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return BorrowReturnRecord(**data)