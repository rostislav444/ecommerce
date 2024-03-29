from rest_framework import serializers

from apps.material.models import ProductPart, ProductPartMaterialsGroups, ProductPartMaterials
from apps.material.serializers import ColorSerializer
from apps.product.models import Product3DBlenderModel, ProductClass, Product, Sku, CameraLocations
from apps.product.serializers.serializers_scene_parts import ProductPartSceneSerializer


class SkuRenderSerializer(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Sku
        fields = ['id', 'materials']

    @staticmethod
    def get_materials(obj):
        return {material.material.group.product_part.blender_name: material.material.id for material in
                obj.materials.all()}


class CameraLocationsSerializer(serializers.ModelSerializer):
    parts = ProductPartSceneSerializer(many=True, read_only=True)

    class Meta:
        model = CameraLocations
        fields = '__all__'


class ProductRender3DBlenderModelSerializer(serializers.ModelSerializer):
    cameras = CameraLocationsSerializer(many=True, read_only=True)

    class Meta:
        model = Product3DBlenderModel
        fields = ['obj', 'mtl', 'cameras']


class ProductRenderSerializer(serializers.ModelSerializer):
    sku = serializers.SerializerMethodField()
    model_3d = ProductRender3DBlenderModelSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'code', 'model_3d', 'sku', ]

    @staticmethod
    def get_sku(obj):
        qs = obj.sku.filter(images__isnull=True).distinct()
        # qs = obj.sku.all().distinct()
        return SkuRenderSerializer(qs, many=True).data


class ProductPartRenderMaterialSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    material = serializers.SerializerMethodField()

    class Meta:
        model = ProductPartMaterials
        fields = ('id', 'color', 'material',)

    def get_material(self, obj):
        if obj.material and obj.material.blender_material:
            data = obj.material.blender_material.get_data
            data['name'] = obj.material.blender_material.name
            return data
        return None


class ProductPartRenderMaterialsGroupsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='group.type')
    materials = ProductPartRenderMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = ProductPartMaterialsGroups
        fields = ('product_part', 'type', 'materials',)


class ProductPartRenderSerializer(serializers.ModelSerializer):
    material_groups = ProductPartRenderMaterialsGroupsSerializer(many=True, read_only=True)

    class Meta:
        model = ProductPart
        fields = ('blender_name', 'name', 'material_groups')


class ProductRenderWithSkuSerializer(serializers.ModelSerializer):
    parts = serializers.SerializerMethodField()
    products = ProductRenderSerializer(many=True, read_only=True)

    class Meta:
        model = ProductClass
        fields = ['id', 'parts', 'products']

    def get_parts(self, obj):
        if obj.materials_set:
            return ProductPartRenderSerializer(obj.materials_set.parts.all(), many=True, read_only=True,
                                               context=self._context).data
