from email.policy import default
from tabnanny import verbose
from unittest.util import _MAX_LENGTH


from django.db import models
from django.db.models.deletion import CASCADE
import datetime


class Mesa(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    numero = models.PositiveIntegerField(verbose_name='numero',unique=True)

    capacidad = models.DecimalField(verbose_name='capacidad', max_digits=10,decimal_places=0,default=0)

    descripcion = models.CharField(verbose_name='descripcion',max_length=60,default='')

    estado = models.BooleanField(verbose_name='estado',default=False)

    class Meta:
        db_table = 'mesa'

    def __str__(self):
         return str(self.numero)


class Categoria(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    codigo = models.PositiveIntegerField(verbose_name='codigo',unique=True)

    nombre = models.CharField(verbose_name='nombre',max_length=100)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return str(self.nombre)


class Comprobante(models.Model):

    id = models.AutoField(db_column='ID', primary_key=True)

    tipo = models.CharField(verbose_name = 'tipo', unique = True, max_length=20, default = '')

    class Meta:
        db_table = 'comprobante'

    def __str__(self):
        return str(self.tipo)


class UnMedida(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    un_medida = models.CharField(verbose_name='un_medida', unique=True, max_length=30)

    class Meta:
        db_table = 'un_medida'

    def __str__(self):
        return str(self.un_medida)



class Proveedor(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    codigo = models.PositiveIntegerField(verbose_name='codigo',unique=True, default=0)

    nombre = models.CharField(verbose_name = 'proveedor',max_length=50)

    cuit = models.CharField(verbose_name = 'cuit',max_length=50, default = '')

    direccion = models.CharField(verbose_name = 'direccion',max_length=50, default = '')

    telefono = models.CharField(verbose_name = 'telefono', max_length=100)

    e_mail = models.EmailField(verbose_name = 'e_mail',max_length=50, default = '')

    porc_iva = models.DecimalField(verbose_name = 'porc_iva',max_digits=5, decimal_places=2, default = 0)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return str(self.nombre)

class Moza_o(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    legajo = models.PositiveIntegerField(verbose_name='legajo', unique=True,default=0)

    nombre = models.CharField(verbose_name='nombre', max_length=80, default='')

    fecha_ingreso = models.DateField(verbose_name='fecha_ingreso',default=datetime.date.today)

    cuil = models.CharField(verbose_name='cuil', max_length=80, default='')

    direccion = models.CharField(verbose_name='direccion', max_length=80, default='')

    telefono = models.CharField(verbose_name='telefono', max_length=80, default='')

    class Meta:
        db_table = 'moza_o'

    def __str__(self):
        return str(self.nombre)




class Producto(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    codigo = models.PositiveIntegerField(verbose_name='codigo',unique=True, default = 0)

    categoria = models.ForeignKey(Categoria, on_delete=CASCADE,default='')

    nombre = models.CharField(verbose_name='nombre', max_length=80, default='')

    descripcion = models.CharField(verbose_name='descripcion', max_length=80, default='')

    precio_costo = models.DecimalField(verbose_name='precio_costo',max_digits=10, decimal_places=2,default=0)

    precio_venta = models.DecimalField(verbose_name='precio_venta',max_digits=10, decimal_places=2,default=0)

    un_medida = models.ForeignKey(UnMedida, on_delete=CASCADE, default='')

    medida_producto = models.DecimalField(verbose_name='medida_producto',max_digits=10, decimal_places=3,default=0)

    cantidad = models.DecimalField(verbose_name='cantidad',max_digits=10, decimal_places=2)

    stock = models.DecimalField(verbose_name='stock',max_digits=10, decimal_places=2,
                                default=0,blank=True,null=True)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return str(self.nombre)


class CtaProv(models.Model):

    id = models.AutoField(db_column='ID',primary_key=True)

    fecha = models.DateField(verbose_name='fecha',default=datetime.date.today)

    proveedor = models.ForeignKey(Proveedor, on_delete=CASCADE)
    
    tipo_cpte = models.ForeignKey(Comprobante, on_delete=CASCADE)

    cpte_nro = models.PositiveIntegerField(verbose_name='cpte_nro')

    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)

    producto = models.ForeignKey(Producto, on_delete=CASCADE, blank=True, null=True)

    cantidad = models.DecimalField(verbose_name='cantidad',decimal_places=2,max_digits=10,default=0)

    precio = models.DecimalField(verbose_name='precio',max_digits=10, decimal_places=2)

    importe = models.DecimalField(verbose_name='importe',max_digits=10, decimal_places=2)

    iva = models.DecimalField(verbose_name='iva',max_digits=10, decimal_places=2)

    importe_total = models.DecimalField(verbose_name='importe_total',max_digits=10, decimal_places=2)

    debe = models.DecimalField(verbose_name='debe',max_digits=10,
                                decimal_places=2,null=True,blank=True)

    haber = models.DecimalField(verbose_name='haber',max_digits=10, decimal_places=2,
                                null=True,blank=True)

    saldo = models.DecimalField(verbose_name='saldo',max_digits=10, decimal_places=2,
                                null=True,blank=True)
    
    class Meta:
        db_table = 'cta_prov'

    def __str__(self):
        return str(self.id,self.proveedor)



