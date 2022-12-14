from django.contrib import admin
from apps.attribute.abstract.admin import AttributeFildSet
from apps.attribute.models import AttributeGroupUnit, AttributeGroup, AttributeSubGroup, AttributeUnitGroup, \
    AttributeUnit, Attribute, Colors


@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    pass


# Attribute Group Unit
@admin.register(AttributeGroupUnit)
class AttributeGroupUnitAdmin(admin.ModelAdmin):
    list_display = ['name']


# Attribute Unit Group
class AttributeUnitInline(AttributeFildSet):
    model = AttributeUnit
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "attribute":
            parent_id = request.resolver_match.kwargs.get('object_id')
            kwargs["queryset"] = Attribute.objects.filter(group__unit_group=parent_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_max_num(self, request, obj=None, **kwargs):
        if not obj or obj.custom:
            return 0


@admin.register(AttributeUnitGroup)
class AttributeUnitGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [AttributeUnitInline]


class AttributeUnitGroupInline(admin.StackedInline):
    show_change_link = True
    model = AttributeUnitGroup
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        if not obj or obj.custom:
            return 0


# Attribute Sub Group
class AttributeSubGroupInline(admin.StackedInline):
    show_change_link = True
    model = AttributeSubGroup
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        if not obj or obj.custom:
            return 0


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'attribute_group']


class AttributeInline(AttributeFildSet):
    model = Attribute
    extra = 0

    def get_max_num(self, request, obj=None, **kwargs):
        if not obj or obj.custom:
            return 0


@admin.register(AttributeGroup)
class AttributeGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'type']
    inlines = [
        AttributeSubGroupInline,
        AttributeUnitGroupInline,
        AttributeInline
    ]
