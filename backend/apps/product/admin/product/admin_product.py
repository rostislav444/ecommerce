from django.contrib import admin

from apps.abstract.admin import ParentLinkMixin
from apps.product.forms import ProductOptionPriceMultiplierFromSet, ProductOptionPriceMultiplierFrom
from apps.product.models import Product, Product3DBlenderModel, ProductOptionPriceMultiplier, ProductClass
from .admin_product_attribute import ProductAttributeInline
from .admin_sku import SkuInline


# TODO add From, Formset, min and max
class ProductOptionPriceMultiplierInline(admin.StackedInline):
    model = ProductOptionPriceMultiplier
    form = ProductOptionPriceMultiplierFrom
    formset = ProductOptionPriceMultiplierFromSet

    @staticmethod
    def calc_num(obj):
        return obj.get_price_sub_group_multiplier_attribute_groups.count()

    def get_min_num(self, request, obj=None, **kwargs):
        return self.calc_num(obj)

    def get_max_num(self, request, obj=None, **kwargs):
        return self.calc_num(obj)


class Product3DBlenderModelInline(admin.StackedInline):
    model = Product3DBlenderModel


@admin.register(Product)
class ProductAdmin(ParentLinkMixin, admin.ModelAdmin):
    parent_model = ProductClass
    inlines = [
        Product3DBlenderModelInline,
        ProductOptionPriceMultiplierInline,
        ProductAttributeInline,
        SkuInline
    ]
    fieldsets = [
        [None, {
            'fields': (
                'code', ('price', 'stock'), ('render_variants', 'generate_sku'),
            )
        }, ],
    ]
