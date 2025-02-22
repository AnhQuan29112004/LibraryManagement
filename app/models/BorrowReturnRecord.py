import json
class BorrowReturnRecord:
    def __init__(self,recordId,memberId,borrowingList,borrowDate,returnDateEst,returnDate):
        self.__recordId=recordId
        self.__memberId=memberId
        self.__borrowingList=borrowingList
        self.__borrowDate=borrowDate
        self.__returnDateEst=returnDateEst
        self.__returnDate=returnDate
        
    # Getter và Setter cho recordId
    def getRecordId(self):
        return self.__recordId

    def setRecordId(self, recordId):
        self.__recordId = recordId

    # Getter và Setter cho memberId
    def getMemberId(self):
        return self.__memberId

    def setMemberId(self, memberId):
        self.__memberId = memberId

    # Getter và Setter cho borrowingList
    def getBorrowingList(self):
        return self.__borrowingList

    def setBorrowingList(self, borrowingList):
        self.__borrowingList = borrowingList

    # Getter và Setter cho borrowDate
    def getBorrowDate(self):
        return self.__borrowDate

    def setBorrowDate(self, borrowDate):
        self.__borrowDate = borrowDate

    # Getter và Setter cho returnDateEst (Ngày trả dự kiến)
    def getReturnDateEst(self):
        return self.__returnDateEst

    def setReturnDateEst(self, returnDateEst):
        self.__returnDateEst = returnDateEst

    # Getter và Setter cho returnDate (Ngày trả thực tế)
    def getReturnDate(self):
        return self.__returnDate

    def setReturnDate(self, returnDate):
        self.__returnDate = returnDate
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return BorrowReturnRecord(**data)