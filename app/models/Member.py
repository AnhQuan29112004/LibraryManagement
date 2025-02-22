import json
class Member:
    def __init__(self,memberId,fullName,phoneNumber,identificationNumber,address,borrowingBooks):
        self.__memberId=memberId
        self.__fullName=fullName
        self.__phoneNumber=phoneNumber
        self.__identificationNumber=identificationNumber
        self.__address=address
        self.__borrowingBooks=borrowingBooks
        
    # Getter và Setter cho memberId
    def getMemberId(self):
        return self.__memberId
    
    def setMemberId(self, memberId):
        self.__memberId = memberId

    # Getter và Setter cho fullName
    def getFullName(self):
        return self.__fullName
    
    def setFullName(self, fullName):
        self.__fullName = fullName

    # Getter và Setter cho phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber
    
    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    # Getter và Setter cho identificationNumber
    def getIdentificationNumber(self):
        return self.__identificationNumber
    
    def setIdentificationNumber(self, identificationNumber):
        self.__identificationNumber = identificationNumber

    # Getter và Setter cho address
    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address

    # Getter và Setter cho borrowingBooks
    def getBorrowingBooks(self):
        return self.__borrowingBooks
    
    def setBorrowingBooks(self, borrowingBooks):
        self.__borrowingBooks = borrowingBooks
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        member = Member(data['member_id'], data['name'], data['phone'], data['cccd'], data['address'])
        member.borrowed_books = data.get('borrowed_books', [])
        return member