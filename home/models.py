from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class SenhaUsuario(models.Model):
    senha = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True, related_name='senha_raw')

    def __str__(self):
        return self.senha
    
class Loja(models.Model):
    TIPO_LOJA = (
        ('Filial', 'Filial'),
        ('Posto', 'Posto'),
        ('Representante', 'Representante'),
        ('Deposito', 'Deposito')
    )
    id = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=3, unique=True)
    cidade = models.CharField(max_length=30)
    loja_mae = models.CharField(max_length=3, default='N/A')
    tipo = models.CharField(max_length=20, choices=TIPO_LOJA, default='N/A')
    uf = models.CharField(max_length=2, null=True, blank=True)
    latitude_longitude = models.CharField(max_length=30, null=True, blank=True)
    postos = models.CharField(max_length=50, null=True, blank=True, default='')
    republica = models.CharField(max_length=50, null=True, blank=True, default='')
    desativado = models.BooleanField(default=False)


    def __str__(self):
        return self.sigla
    
    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'


class Suporte(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=11, blank=True, null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='suportes', default=None)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True, null=True, related_name='suporte')
    desativado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    def get_qtd_viagens_concluidas_no_ano(self):
        qtd_viagens_concluidas_no_ano = self.viagens.filter(concluida=True, data__year=datetime.now().date().year).count()
        
        return qtd_viagens_concluidas_no_ano
    
    def get_percent_viagens_concluidas_ano(self):
        qtd_viagens_concluida_ano = Viagem.objects.filter(concluida=True, data__year=datetime.now().date().year).count()
        qtd_viagens_concluidas_individual = self.viagens.filter(concluida=True, data__year=datetime.now().date().year).count()
        return int((qtd_viagens_concluidas_individual/qtd_viagens_concluida_ano)*100)*2
    
    class Meta:
        verbose_name = 'Suporte'
        verbose_name_plural = 'Suportes'    

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    desativado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Viagem(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    lojas = models.ManyToManyField(Loja, blank=True, related_name='viagens')
    data_saida = models.DateField(null=True, blank=True) #default=timezone.now
    data = models.DateField(null=True, blank=True)
    suportes = models.ManyToManyField(Suporte, blank=True, related_name='viagens')
    servicos = models.ManyToManyField(Servico, blank=True, related_name='servicos')
    iframe = models.CharField(max_length=500, blank=True, null=True)
    chamado = models.CharField(max_length=6, blank=True, null=True)
    concluida = models.BooleanField(default=False)
    desativado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.auto_increment_id)
    
    def get_lojas(self):
        if self.lojas:
            return ', '.join(loja.sigla for loja in self.lojas.all())
        else:
            return 'Nenhuma'
    
    def get_data(self):
        if self.data:
            return self.data
        else:
            return 'Nenhuma'
    
    def get_suportes(self):
        return ', '.join(suporte.nome for suporte in self.suportes.all())
    
    def get_servicos(self):
        return ', '.join(servico.nome for servico in self.servicos.all())
    
    def get_month_name(self):

        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', \
                      'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_viagem = []

        if self.data:
            x = self.data.month
        else:
            x = datetime.now().date().month

        mes_viagem.append(meses[x-1])

        return mes_viagem[0]
    
    def get_month_number(self):

        if self.data:
            return self.data.month
        else:
            return datetime.now().date().month
    
    def get_chamado(self):
        if self.chamado == None:
            return 'Nenhum'
        else:
            return self.chamado
    
    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'