import json
from datetime import datetime
class BorrowReturnRecord:
    def __init__(self,recordId,memberId,borrowingList,borrowDate,returnDateEst,returnDate=None):
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
        
    def calculate_late_fee(self):
        borrow_date = datetime.strptime(self.getBorrowDate(), "%Y-%m-%d")
        return_date = datetime.strptime(self.getReturnDate(), "%Y-%m-%d")
        return_estDate = datetime.strptime(self.getReturnDateEst(), "%Y-%m-%d")
        if return_date > return_estDate:
            late_days = (return_date - borrow_date).days
            return max(0, late_days * 5000)
        return 0
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        clean_data = {key.replace("_BorrowReturnRecord__", ""): value for key, value in data.items()}
        return BorrowReturnRecord(**clean_data)