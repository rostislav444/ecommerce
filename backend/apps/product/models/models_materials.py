from django.db import models

from apps.abstract.fields import DeletableImageField


class ProductPartScene(models.Model):
    camera = models.ForeignKey('product.CameraLocations', on_delete=models.CASCADE, related_name='parts')
    part = models.ForeignKey('material.ProductPart', on_delete=models.CASCADE)


class ProductPartSceneMaterial(models.Model):
    part = models.ForeignKey(ProductPartScene, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey('material.ProductPartMaterials', on_delete=models.CASCADE,
                                 related_name='material_scene')


class ProductPartSceneMaterialImage(models.Model):
    scene_material = models.OneToOneField(ProductPartSceneMaterial, on_delete=models.CASCADE, related_name='image')
    image = DeletableImageField()
