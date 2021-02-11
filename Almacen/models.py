from django.db import models

class InventarioModel(models.Model):
    inventarioId = models.AutoField(
        primary_key=True,
        db_column="inventario_id",
        null=False,
        unique=True
    )
    inventarioPlato = models.CharField(
        max_length=40,
        db_column="inventario_plato",
        null=False,
        verbose_name="Nombre del Plato"
    )
    inventarioCantidad = models.IntegerField(
        null=False,
        db_column="inventario_cantidad",
        verbose_name="Cantidad del plato"
    )
    inventarioPrecio = models.DecimalField(
        max_digits= 5,
        decimal_places= 2,
        null=False,
        db_column="inventario_precio",
        verbose_name="Precio del plato"
    )

    def __str__(self):
        return self.inventarioPlato
    class Meta:
        db_table="t_inventario"
        verbose_name="Inventario"
        verbose_name_plural="Inventarios"