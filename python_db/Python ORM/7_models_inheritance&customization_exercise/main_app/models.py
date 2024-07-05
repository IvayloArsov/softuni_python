from datetime import timedelta

from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def reply_to_message(self, reply_content):
        new_msg = Message.objects.create(
            sender=self.receiver,
            receiver=self.sender,
            content=reply_content,
        )
        return new_msg

    def forward_message(self, receiver):
        new_msg = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=self.content
        )

        return new_msg


class StudentIDField(models.PositiveIntegerField):
    def to_python(self, value):
        if value is None:
            return None
        try:
            return int(float(value))
        except (TypeError, ValueError):
            raise ValueError("Invalid input for student ID")

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value <= 0:
            raise ValidationError("ID cannot be less than or equal to zero")


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")

        if not value.isdigit():
            raise ValidationError("The card number must contain only digits")

        if len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")

        return f'****-****-****-{value[-4:]}'

    def get_prep_value(self, value):
        return self.to_python(value)


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField()


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")
        super().save(*args, **kwargs)
        return f"Room {self.number} created successfully"


class BaseReservation(models.Model):
    class Meta:
        abstract = True

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def reservation_period(self):
        return (self.end_date - self.start_date).days

    def calculate_total_cost(self):
        return round(self.room.price_per_night * self.reservation_period(), 2)

    def clean(self):
        super().clean()
        if self.start_date >= self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

    def check_overlapping_reservations(self, exclude_pk=None):
        queryset = self.__class__.objects.filter(
            room=self.room,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        )
        if exclude_pk:
            queryset = queryset.exclude(pk=exclude_pk)
        if queryset.exists():
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

    def save(self, *args, **kwargs):
        self.full_clean()
        self.check_overlapping_reservations(exclude_pk=self.pk)
        super().save(*args, **kwargs)
        class_name = self.__class__.__name__.replace('Reservation', '').strip()
        return f"{class_name} reservation for room {self.room.number}"


class RegularReservation(BaseReservation):
    pass


class SpecialReservation(BaseReservation):
    def extend_reservation(self, days: int):
        new_end_date = self.end_date + timedelta(days=days)
        old_end_date = self.end_date
        self.end_date = new_end_date

        try:
            self.check_overlapping_reservations()
            self.save()
            return f"Extended reservation for room {self.room.number} with {days} days"
        except ValidationError:
            self.end_date = old_end_date
            raise ValidationError('Error during extending reservation')
