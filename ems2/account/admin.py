from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from django.contrib.auth.models import Permission


class AccountAdmin(UserAdmin):
	list_display = ('pk', 'email','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('pk', 'email',)
	readonly_fields=('pk', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ('email',)


admin.site.register(Account, AccountAdmin)






