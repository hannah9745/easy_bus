from django.db import models


# Create your models here.

class login_table(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


class user_table(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    image = models.FileField()


class route_table(models.Model):
    from_rout = models.CharField(max_length=100)
    to_rout = models.CharField(max_length=100)


class busowner_table(models.Model):
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()


class stop_table(models.Model):
    route = models.ForeignKey(route_table, on_delete=models.CASCADE)
    stopname = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    fair = models.BigIntegerField()
    stage = models.BigIntegerField()


class bus_table(models.Model):
    bus_owner = models.ForeignKey(busowner_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    regno = models.CharField(max_length=20)
    photo = models.FileField()
    fitness=models.CharField(max_length=20)
    insurance = models.BigIntegerField()
    rcbook = models.CharField(max_length=100)


class trip_table(models.Model):
    route = models.ForeignKey(route_table, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_table, on_delete=models.CASCADE)
    tripname = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class timing_table(models.Model):
    trip = models.ForeignKey(trip_table, on_delete=models.CASCADE)
    stop = models.ForeignKey(stop_table, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)


class booking_table(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    trip = models.ForeignKey(trip_table, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    from_booking = models.CharField(max_length=100)
    to_booking  = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    status = models.CharField(max_length=100)


class employee_table(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    image = models.FileField()
    license = models.CharField(max_length=100)
    owner=models.ForeignKey(busowner_table, on_delete=models.CASCADE)
    login = models.ForeignKey(login_table, on_delete=models.CASCADE)


class assign_table(models.Model):
    employe = models.ForeignKey(employee_table, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_table, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class complaint_table(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)


class collection_table(models.Model):
    trip = models.ForeignKey(trip_table, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    amount = models.BigIntegerField()


class notification_table(models.Model):
    notification = models.CharField(max_length=100)
    date = models.DateField()
    details = models.CharField(max_length=100)


class feedback_table(models.Model):
    user = models.ForeignKey(user_table, on_delete=models.CASCADE)
    bus = models.ForeignKey(bus_table, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)
    rating = models.FloatField()
