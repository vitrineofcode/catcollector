from django.db import models
from datetime import date
from django.contrib.auth.models import User


# A tuple defining meal choices for the Feeding model
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=100)  # Name of the cat
    breed = models.CharField(max_length=100)  # Breed of the cat
    description = models.TextField(max_length=250)  # Description of the cat
    age = models.IntegerField()  # Age of the cat
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
      # Return the cat's name when its object is called as a string
      return self.name
    
    def fed_for_today(self):
      # Checks if the cat has been fed all meals today by comparing the number of feedings today with the number of meals defined
      return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding date')  # Date of feeding
    meal = models.CharField(
        max_length=1,
        choices=MEALS,  # Set meal type based on MEALS tuple
        default=MEALS[0][0]  # Default meal type to 'Breakfast'
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)  # Foreign key linking back to Cat, deletes on cat deletion

    def __str__(self):
        # Return a string representing the meal and date
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']  # Orders the Feeding instances by date in descending order

