from django.contrib import admin
from home.models import Viagem, Loja, Suporte, Servico, SenhaUsuario

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'senha', 'grupo')

@admin.register(Suporte)    
class SuportesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'whatsapp', 'owner', 'desativado')

@admin.register(Viagem)    
class ViagensAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id', 'get_lojas', 'data_saida', 'data', 'get_suportes', 'get_servicos', 'iframe', 'chamado', 'concluida')

@admin.register(Loja)    
class LojasAdmin(admin.ModelAdmin):
    list_display = 'id', 'sigla', 'cidade', 'tipo', 'loja_mae', 'uf', 'latitude_longitude'

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

@admin.register(SenhaUsuario)
class SenhaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('senha', 'usuario',)

