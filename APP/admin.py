from django.contrib import admin

from APP.models.Test import Test


admin.site.site_header = "Test"
admin.site.index_title = "Test"
admin.site.site_title = "Test"

class TestAdmin(admin.ModelAdmin):
    list_display = (
        'testdata',
    )
    search_fields = ['testdata',]

admin.site.register(Test, TestAdmin)