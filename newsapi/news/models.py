from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 120)
    body = models.TextField()
    location =models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updeted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}{}".format(self.author, self.title)

class TourPack(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()
    tour_img = models.ImageField(blank=True, null=True)
    from_where = models.CharField(max_length=120)
    to = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
    (ACTIVE, "Active"),
    (FULL, "Full"),
    (EXPIRED, "Expired"),
    (NEW, "New"),
    )
    status = models.CharField(max_length=9,
                  choices=STATUS_CHOICES,
                  default=ACTIVE)

    def __str__(self):
        return "Tur:{}- DESC:{}- PRICE: ${}- Start_date:{}- end_date:{} -Quantity:{}".format(
                                                                                            self.name, 
                                                                                            self.description,
                                                                                            int(self.price),
                                                                                            self.start_date,
                                                                                            self.end_date,
                                                                                            self.quantity)

class Client(models.Model):
    username = models.CharField(max_length=16)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    password_id =  models.IntegerField()
    password_img =  models.ImageField(null=True, blank=True, upload_to='images/')
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {} ".format(self.username, int(self.phone_number), self.email)

class ClientTour(models.Model):
    tourpack_id = models.ForeignKey(TourPack, null=True, related_name="tourpack_id", on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, null=True, related_name="client_id", on_delete=models.CASCADE)
    adult_count = models.PositiveIntegerField(default=1)
    child_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.tourpack_id, self.client_id)

class ClientTourParticipant(models.Model):
    clienttour_id = models.ForeignKey(ClientTour, null=True, related_name="clienttour_id", on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, null=True, related_name="client_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.clienttour_id, self.client_id)

class Order(models.Model):
    clienttour_id = models.ForeignKey(ClientTour, null=True, related_name="clienttour_id", on_delete=models.CASCADE)
    STATUS_CHOICES = (
    (ACTIVE, "Active"),
    (FULL, "Full"),
    (EXPIRED, "Expired"),
    (NEW, "New")
    )
    status = models.CharField(max_length=9,
                  choices=STATUS_CHOICES,
                  default=ACTIVE)
    PAYMENT_STATUS = (
    (PAID, "Paid"),
    (NOT_PAID, "Not Paid")
    )
    payment_status = models.CharField(max_length=9,
                  choices=PAYMENT_STATUS,
                  default=PAID)
    PAYMENT_METHODS = (
    (VISA, "Pay w/ Visa Card"),
    (MS, "Pay w/ MasterCard"),
    (CRYPTO, "Pay w/ CRYPTO"),
    (PAYPAL, "Pay w/ Paypal"),
    (CASH, "Pay in cash")
    )
    payment_methods = models.CharField(max_length=9,
                  choices=PAYMENT_METHODS,
                  default=CASH)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} {} {} {} {} {}".format(self.clienttour_id, self.client_id, self.status, self.payment_status, self.payment_methods, self.created_at)





