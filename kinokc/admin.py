from django.contrib import admin
from .models import Post, SignUp, Reservation
class ReservationAdmin(admin.ModelAdmin):
	list_display = ("__str__", "imię", "film", "ilość_biletów", "dzień", "godzina")
	class Meta:
		model = Reservation


admin.site.register(Post)
admin.site.register(SignUp)
admin.site.register(Reservation, ReservationAdmin)

