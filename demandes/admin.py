from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from .models import DemandeTravaux


class AttenteFilterSpec(SimpleListFilter):
    title = "Etat des Demandes"
    parameter_name="etat"
    
    def lookups(self, request, model_admin):
        return (
                ('1', "Traité"),
                ('0', "En cours"),
                )
    
    def queryset(self, request, queryset):

        if self.value() == '0':
            return queryset.exclude(chef_avis__isnull=False,resp_avis__isnull=False)
        if self.value() == '1':
            return queryset.filter(chef_avis__isnull=False,resp_avis__isnull=False)
        return queryset


class DemandeTravauxAdmin(admin.ModelAdmin):
    list_display = ("titre","auteur", "val_chef", "chef", "val_resp", "resp")
    list_filter = ("auteur",AttenteFilterSpec,"chef_avis","resp_avis")
    fieldsets = (("Informations Générales", {"fields": ("titre","date","type","commentaire","nature","affectation")}),
        ("Description", {"fields": ("description", "matiere", "commande","delai_fin","dimensions","materiau","quantite")}),
        ("Chef de Travaux", {"fields":("chef_avis","chef_justification")}),
        ("Responsable", {"fields":("resp_avis","resp_justification")}),
        )
    
    def get_form(self, request, obj=None, **kwargs):
        
        readonly_fields = ["chef_avis","chef_justification","resp_avis","resp_justification"]
        
        if request.user.groups.filter(name="chef").exists():
            readonly_fields.remove("chef_avis")
            readonly_fields.remove("chef_justification")
        
        if request.user.groups.filter(name="resp").exists():
            readonly_fields.remove("resp_avis")
            readonly_fields.remove("resp_justification")
        
        self.readonly_fields=tuple(readonly_fields)
        
        return super(DemandeTravauxAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        
        if "chef_avis" in form.changed_data:
            obj.chef = request.user
        
        if "resp_avis" in form.changed_data:
            obj.resp = request.user
        
        if getattr(obj, "auteur", None) is None:
            obj.auteur = request.user
        obj.save()

admin.site.register(DemandeTravaux,DemandeTravauxAdmin)

