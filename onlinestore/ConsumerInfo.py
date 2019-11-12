class Books:

    def __init__(self, bid, bname, bauth, bprice, bqty, bpub, brev):
        self.id = bid
        self.name = bname
        self.author = bauth
        self.price = bprice
        self.qty = bqty
        self.publication = bpub
        self.reviews = brev

    def __str__(self):
        return f'''\n
        Id : {self.id},
        Name : {self.name},
        Auther : {self.author},
        Price: {self.price},
        Quantity : {self.qty},
        Publication : {self.publication},
        Review : {self.reviews}
        '''

    def __repr__(self):
        return str(self)
# lib=Books(bid=1,bname='national geo',bauth='geology',bprice=1000,bqty=1,bpub='history',brev='informatics')
