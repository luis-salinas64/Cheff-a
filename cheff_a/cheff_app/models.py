from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.deletion import CASCADE
import datetime


class Comprobante(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    nombre = models.CharField(verbose_name = 'cptes', unique = True, max_length=20, default = 'cpte')
    
    class Meta:
        db_table = 'comprobante'

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    nombre = models.CharField(verbose_name = 'proveedor',max_length=50)

    cuit = models.CharField(verbose_name = 'cuit',max_length=50, default = '')

    debe = models.DecimalField(verbose_name='debe',max_digits=10, decimal_places=2, default=0)

    haber = models.DecimalField(verbose_name='haber',max_digits=10, decimal_places=2, default=0)

    saldo = models.DecimalField(verbose_name='saldo', max_digits=10, decimal_places=2, default=0)

    contacto = models.CharField(max_length=100)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

class UnMedida(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    un_medida = models.CharField(max_length=30)

    class Meta:
        db_table = 'un_medida'

    def __str__(self):
        return self.un_medida

class Ingredientes(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    nombre = models.CharField(max_length=100)

    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    un_medida = models.ForeignKey(UnMedida, on_delete=CASCADE)

    medida_producto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    class Meta:
        db_table = 'ingredientes'

    def __str__(self):
        return self.nombre

class Insumos_Mesa(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    nombre = models.CharField(max_length=100)

    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    un_medida = models.ForeignKey(UnMedida, on_delete=CASCADE)

    medida_producto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'insumos_mesa'

    def __str__(self):
        return self.nombre

class ProductoTerminado(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    codigo = models.PositiveIntegerField(verbose_name='codigo',unique=True, default = 0)

    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)

    nombre = models.CharField(verbose_name='nombre', max_length=80, default='')

    precio_costo = models.DecimalField(verbose_name='precio_costo',max_digits=10, decimal_places=2,default=0)

    precio_venta = models.DecimalField(verbose_name='precio_venta',max_digits=10, decimal_places=2,default=0)

    un_medida = models.ForeignKey(UnMedida, on_delete=CASCADE, default='')

    medida_producto = models.DecimalField(verbose_name='medida_producto',max_digits=10, decimal_places=2,default=0)

    cantidad = models.DecimalField(verbose_name='cantidad',max_digits=10, decimal_places=2)

    stock = models.DecimalField(verbose_name='stock',max_digits=10, decimal_places=2, default=0)

    desperdicio = models.DecimalField(verbose_name='desperdicio',max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'producto_terminado'

    def __str__(self):
        return self.nombre

class ProductoElaborado(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)    

    codigo = models.PositiveIntegerField(verbose_name='codigo',unique=True)

    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)

    nombre = models.CharField(verbose_name='nombre', max_length=80, default='')

    descripcion = models.CharField(verbose_name='descripcion', max_length=80, default='')

    imagen = models.ImageField(verbose_name='imagen', upload_to='productos/', null = True, default='')

    ingrediente_base = models.ForeignKey(Ingredientes, on_delete=CASCADE)
    un_medida_base = models.ForeignKey(UnMedida, on_delete=CASCADE, default='')
    cant_ing_base = models.DecimalField(verbose_name='cant_ing_base',max_digits=10, decimal_places=2, default=0)

    ingrediente_2 = models.ForeignKey(Ingredientes, on_delete=CASCADE, null=True, blank=True, related_name='ingrediente_2')
    un_medida_2 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_2',default='')
    cant_ing_2 = models.DecimalField(verbose_name='cant_ing_2',max_digits=10, decimal_places=2, default=0)

    ingrediente_3 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_3',null=True, blank=True)
    un_medida_3 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_3',default='')
    cant_ing_3 = models.DecimalField(verbose_name='cant_ing_3',max_digits=10, decimal_places=2, default=0)

    ingrediente_4 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_4',null=True, blank=True)
    un_medida_4 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_4',default='')
    cant_ing_4 = models.DecimalField(verbose_name='cant_ing_4',max_digits=10, decimal_places=2, default=0)

    ingrediente_5 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_5',null=True, blank=True)
    un_medida_5 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_5',default=0)
    cant_ing_5 = models.DecimalField(verbose_name='cant_ing_5',max_digits=10, decimal_places=2, default=0)

    ingrediente_6 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_6',null=True, blank=True)
    un_medida_6 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_6',default=0)
    cant_ing_6 = models.DecimalField(verbose_name='cant_ing_6',max_digits=10, decimal_places=2, default=0)

    ingrediente_7 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_7',null=True, blank=True)
    un_medida_7 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_7',default=0)
    cant_ing_7 = models.DecimalField(verbose_name='cant_ing_7',max_digits=10, decimal_places=2, default=0)

    ingrediente_8 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_8',null=True, blank=True)
    un_medida_8 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_8',default=0)
    cant_ing_8 = models.DecimalField(verbose_name='cant_ing_8',max_digits=10, decimal_places=2, default=0)

    ingrediente_9 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_9',null=True, blank=True)
    un_medida_9 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_9',default=0)
    cant_ing_9 = models.DecimalField(verbose_name='cant_ing_9',max_digits=10, decimal_places=2, default=0)

    ingrediente_10 = models.ForeignKey(Ingredientes, on_delete=CASCADE, related_name='ingrediente_10',null=True, blank=True)
    un_medida_10 = models.ForeignKey(UnMedida, on_delete=CASCADE, related_name='un_medida_10',default='')
    cant_ing_10 = models.DecimalField(verbose_name='cant_ing_10',max_digits=10, decimal_places=2, default=0)

    porcentual_desperdicio = models.DecimalField(verbose_name='desperdicio',max_digits=10, decimal_places=2,null=True, blank=True)


    class Meta:
        db_table = 'producto_elaborado'

    def __str__(self):
        return self.nombre

class Moza_o(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    nombre = models.CharField(verbose_name='nombre', max_length=80, default='')

    fecha_ingreso = models.DateField(verbose_name='fecha_ingreso',default=datetime.date.today)

    cuil = models.CharField(verbose_name='cuil', max_length=80, default='')

    direccion = models.CharField(verbose_name='direccion', max_length=80, default='')

    telefono = models.CharField(verbose_name='telefono', max_length=80, default='')

    class Meta:
        db_table = 'moza_o'

    def __str__(self):
        return self.nombre



class Mesa(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    numero = models.PositiveIntegerField(verbose_name='numero',unique=True)

    cant_comensales = models.DecimalField(verbose_name='cant_comensales', max_digits=10,decimal_places=0,default=0)

    descripcion = models.CharField(verbose_name='descripcion',max_length=60,default='')

    class Meta:
        db_table = 'mesa'           

    # def __str__(self):
    #     return self.numero



class Operacion(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    cpte_nro = models.PositiveIntegerField(verbose_name='cpte_nro',unique=True, default = 0)

    moza_o = models.ForeignKey(Moza_o, on_delete=CASCADE,default='')

    fecha = models.DateField(verbose_name='fecha',default=datetime.date.today)

    tipo = models.ForeignKey(Comprobante, on_delete=CASCADE)

    proveedor = models.ForeignKey(Proveedor, on_delete=CASCADE)

    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)

    producto_terminado = models.ForeignKey(ProductoTerminado, on_delete=CASCADE, blank=True, null=True)

    producto_elaborado = models.ForeignKey(ProductoElaborado, on_delete=CASCADE, blank=True, null=True)

    ingredientes = models.ForeignKey(Ingredientes, on_delete=CASCADE, blank=True, null=True)

    precio = models.DecimalField(verbose_name='precio',max_digits=10, decimal_places=2)

    cantidad = models.DecimalField(verbose_name='cantidad',max_digits=10, decimal_places=2)

    importe = models.DecimalField(verbose_name='importe',max_digits=10, decimal_places=2,default=0)

    class Meta:
        db_table = 'operacion'

    def __str__(self):
        return self.id




class Ticket(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)  

    fecha = models.DateField(verbose_name='fecha',default=datetime.date.today)

    mesa = models.ForeignKey(Mesa, on_delete=CASCADE)

    moza_o = models.ForeignKey(Moza_o, on_delete=CASCADE)

    codigo_pt = models.ForeignKey(ProductoTerminado, on_delete=CASCADE, blank=True, null=True)

    cant_pt = models.DecimalField(verbose_name='cantidad_pt',max_digits=10, decimal_places=2,default=0)

    codigo_pe = models.ForeignKey(ProductoElaborado, on_delete=CASCADE, blank=True, null=True)

    cant_pe = models.DecimalField(verbose_name='cantidad_pe',max_digits=10, decimal_places=2,default=0)

    insumo_mesa = models.ForeignKey(Insumos_Mesa, on_delete=CASCADE, blank=True, null=True)

    importe = models.DecimalField(verbose_name='importe',max_digits=10, decimal_places=2,default=0)

    class Meta:
        db_table = 'ticket'

    def __str__(self):
        return self.id

