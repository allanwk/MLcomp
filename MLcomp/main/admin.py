from django.contrib import admin
from .models import Dataset
from cloudinary.api import delete_resources

class DatasetAdmin(admin.ModelAdmin):
    #Lógica para remover imagens do Cloudinary caso 
    #Dataset seja removido
    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        delete_resources(obj.card_image)
        delete_resources(obj.tsne_bar_image)
        delete_resources(obj.tsne_full)

    #Lógica para remover imagens do Cloudinary caso 
    #multiplos Datasets sejam removidos
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            delete_resources(obj.card_image)
            delete_resources(obj.tsne_bar_image)
            delete_resources(obj.tsne_full)
        super().delete_queryset(request, queryset)
    
    #Lógica para remover imagens antigas do Cloudinary,
    #caso o modelo seja atualizado
    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Dataset.objects.get(id=obj.id)

            old_obj_attr = [old_obj.card_image, old_obj.tsne_bar_image, old_obj.tsne_full]
            obj_attr = [obj.card_image, obj.tsne_bar_image, obj.tsne_full]

            compare = list(zip(old_obj_attr, obj_attr))

            for old, new in compare:
                if str(old) != str(new):
                    res = delete_resources(old)['deleted']
        
        super().save_model(request, obj, form, change)

admin.site.register(Dataset, DatasetAdmin)
# Register your models here.
