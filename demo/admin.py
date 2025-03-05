from django.contrib import admin



# ! monday
# display in object


from demo.models import customers

# admin.site.register(customers)







# in this is registeration not required

# dispaly in table format


# ! tuesday


@admin.register(customers)
class customers(admin.ModelAdmin):
    #? table format
    list_display=('id','name','password','phone','image')
    #? search field list of tuple
    search_fields=('id',)
    #? all the data
    # list_filter=('phone',)
    # list_filter=('name',)
    list_filter=('id',)
    # orderby  give id because id is primary key
    ordering=('id',)
    



