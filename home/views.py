from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Viagem, Loja, Suporte, Servico, User, SenhaUsuario
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from home.forms import CreateUserFom, SuporteImage
from datetime import datetime

@login_required
def main(request):

    viagens_programadas_para_este_mes = Viagem.objects.filter(concluida=False, data_saida__gt=datetime.now().date(), data__month=datetime.now().date().month)
    viagens_programadas_para_os_proximos_meses = Viagem.objects.filter(concluida=False, data_saida__gt=datetime.now().date(), data__month__gt=datetime.now().date().month)
    
    lista_suporte_com_viagens_concluidas_no_ano = []
    
    suportes = Suporte.objects.all()

    for suporte in suportes:
        if suporte.get_qtd_viagens_concluidas_no_ano() > 0:
            lista_suporte_com_viagens_concluidas_no_ano.append(suporte)
    
    
    context = {
        'viagens_concluidas': Viagem.objects.filter(concluida=True, data__year__exact=datetime.now().date().year),
        'viagens_em_andamento': Viagem.objects.filter(concluida=False, data_saida__lte=datetime.now().date()),
        'viagens_programadas_para_este_mes': viagens_programadas_para_este_mes,
        'viagens_programadas_para_os_proximos_meses': viagens_programadas_para_os_proximos_meses,
        'suportes': sorted(lista_suporte_com_viagens_concluidas_no_ano, key=lambda x: x.get_qtd_viagens_concluidas_no_ano(), reverse=True),
        'ano': datetime.now().date().year
    }

    
    return render(request, 'inicio.html', context)

# def index(request):

#     return render(request, 'index.html')

def viagens_em_andamento(request):

    if request.method == 'POST':
        for id in request.POST.getlist('encerrar-viagem'):
            viagem = Viagem.objects.get(auto_increment_id=id)
            viagem.concluida = True
            viagem.save()
    
    viagens = Viagem.objects.filter(concluida=False, data_saida__lte=datetime.now().date()).order_by('data')

    loja = None

    if viagens:
        loja = Loja.objects.get(sigla=viagens[0].get_lojas())

    context = {
        'viagens_em_andamento': viagens,
        'loja': loja
    }

    return render(request, 'viagens-em-andamento.html', context)

def viagens_encerradas(request):

    if request.method == 'POST':
        for id in request.POST.getlist('reabrir-viagem'):
            viagem = Viagem.objects.get(auto_increment_id=id)
            viagem.concluida = False
            viagem.save()
    
    viagens = Viagem.objects.filter(concluida=True, data__year__exact=datetime.now().date().year).order_by('data')

    loja = None

    if viagens:
        loja = Loja.objects.get(sigla=viagens[0].get_lojas())

    context = {
        'viagens_encerradas': viagens,
        'loja': loja
    }

    return render(request, 'encerradas.html', context)

def viagens_programadas_para_este_mes(request):

    viagens = Viagem.objects.filter(concluida=False, data_saida__gt=datetime.now().date(), data__month=datetime.now().date().month)

    loja = None
    
    if viagens:
        loja = Loja.objects.get(sigla=viagens[0].get_lojas())

    context = {
        'viagens_programadas_para_este_mes': viagens,
        'loja': loja
    }

    return render(request, 'programadas-para-este-mes.html', context)

def viagens_programadas_para_o_proximo_mes(request):

    viagens = Viagem.objects.filter(concluida=False, data_saida__gt=datetime.now().date(), data__month__gt=datetime.now().date().month).order_by('data')

    loja = None
    if viagens:
        loja = Loja.objects.get(sigla=viagens[0].get_lojas())

    context = {
        'viagens_programadas_para_os_proximos_meses': viagens,
        'loja': loja
    }

    return render(request, 'programadas-para-o-proximo-mes.html', context)

def postos(request):

    context = {
        'projeto': print('Postos')
    }

    return render(request, 'postos.html', context)

def recibos(request):

    context = {
        'projeto': print('Recibos')
    }

    return render(request, 'recibos.html', context)

def recibo_botao_consultar(request):

    context = {
        'projeto': print('Botao-Consultar')
    }

    return render(request, 'botao-consultar.html', context)

def consulta_postos(request):
    
    context = {
        'projeto': print('consulta postos')
    }

    return render(request, 'consulta-postos.html', context)

def cadastro_rcibos(request):

    context = {
        'projeto': print('Cadastro de recibos')
    }

    return render(request, 'recibos-cadastro.html', context)

def incluir_recibos(request):

    context = {
        'projeto': print('Incluir Recibos')
    }
    
    return render(request, 'incluir-recibos.html', context)

def cadastro_viagens(request):

 
       
    return render(request, 'cadastro-viagens.html')

def cadastro_viagens_insert(request):

    if request.POST['chamado'] == '':
        return redirect('cadastro-viagens')
    
    try:
        chamado_var = int(request.POST['chamado'])
    except:
        return redirect('cadastro-viagens')
    
    viagem = Viagem()
    viagem.chamado = chamado_var
    viagem.save()

    return redirect('cadastro-viagens-edit', id=viagem.auto_increment_id)

def cadastro_viagens_edit_insert(request, id):


    if request.POST['chamado'] == '':
        return redirect('cadastro-viagens-edit-toast')
    
    try:
        chamado_var = int(request.POST['chamado'])
    except:
        return redirect('cadastro-viagens-edit', id)
    
    viagem  = Viagem.objects.get(auto_increment_id=id)

    
    viagem.chamado = chamado_var

    viagem.save()


    return redirect('cadastro-viagens-edit-toast')

def cadastro_viagens_edit_toast(request):

    return render(request, 'cadastro-lojas-edit-toast.html')

def cadastro_viagens_edit(request, id):

    viagem_edit = Viagem.objects.get(auto_increment_id=id)

    lista_loja = []

    lista_suporte = []

    lista_servico = []

    for loja in viagem_edit.lojas.all():
        lista_loja.append(loja.__str__())
    
    for suporte in viagem_edit.suportes.all():
        lista_suporte.append(suporte.__str__())
    
    for servico in viagem_edit.servicos.all():
        lista_servico.append(servico.__str__())
    
    
    context = {
        'viagem': viagem_edit,
        'id': viagem_edit.auto_increment_id,
        'lojas': lista_loja,
        'suportes': lista_suporte,
        'servicos': lista_servico,
        'chamado': viagem_edit.chamado
    }

    return render(request, 'cadastro-loja-editar.html', context)

def inserir_loja(request):

    context = {
        'lojas': Loja.objects.all()
    }

    return render(request, 'inserir-loja.html', context)

def inserir_loja_edit(request, id):

    viagem_atualizada = Viagem.objects.get(auto_increment_id=id)
    context = {
        'id': viagem_atualizada.auto_increment_id,
        'lojas': Loja.objects.all()
    }

    return render(request, 'inserir-loja-edit.html', context)

def loja_add(request):

    nova_viagem = Viagem()
    nova_viagem.save()
    
    loja_inserida = request.POST['lojas']
    loja = Loja.objects.get(sigla=loja_inserida)
    nova_viagem.lojas.add(loja)
    
    return redirect('cadastro-viagens-edit', id=nova_viagem.auto_increment_id)

def loja_add_edit(request, id):

    viagem_edit = Viagem.objects.get(auto_increment_id=id)
    loja_inserida = request.POST['lojas']
    loja = Loja.objects.get(sigla=loja_inserida)
    viagem_edit.lojas.add(loja)

    return redirect('cadastro-viagens-edit', id=id)

def deletar_loja(request, id, loja):
    viagem =Viagem.objects.get(auto_increment_id=id)
    loja_deletada = Loja.objects.get(sigla=loja)

    viagem.lojas.remove(loja_deletada)
    viagem.save()

    return redirect('cadastro-viagens-edit', id)

def deletar_chamado(request, id):

    viagem = Viagem.objects.get(auto_increment_id=id)

    viagem.chamado = None

    viagem.save()

    return redirect('cadastro-viagens-edit', id)

def deletar_data(request, id):
    viagem = Viagem.objects.get(auto_increment_id=id)
    viagem.data = None
    viagem.save()

    return redirect('cadastro-viagens-edit', id)

def inserir_data_sem_parametros(request):

    context = {}

    return render (request, 'inserir-data.html', context)

# ---------------------------------------------------------------
# DATA SAIDA

def inserir_data_saida(request):

    context = {}

    return render (request, 'inserir-data-saida.html', context)

def inserir_data_saida_com_id(request, id):

    print(id)

    context = {
        'viagem': Viagem.objects.get(auto_increment_id=id)
    }

    print(context)

    return render (request, 'inserir-data-saida.html', context)

def deletar_data_saida(request, id):
    viagem = Viagem.objects.get(auto_increment_id=id)
    viagem.data_saida = None
    viagem.save()

    return redirect('cadastro-viagens-edit', id)

def insert_date_saida(request):

    nova_viagem = Viagem()

    nova_viagem.data_saida = request.POST['trip_date']

    nova_viagem.save()

    
    return redirect('cadastro-viagens-edit', id=nova_viagem.auto_increment_id)

def insert_date_saida_id(request, id):

    print(id)

    viagem = Viagem.objects.get(auto_increment_id=id)

    viagem.data_saida = request.POST['trip_date']

    viagem.save()

    
    return redirect('cadastro-viagens-edit', id=viagem.auto_increment_id)

# --------------------------------------------------------------

def inserir_data_com_parametros(request, id):

    context = {
        'viagem': Viagem.objects.get(auto_increment_id=id)
    }
    
    return render(request, 'inserir-data-com-parametros.html', context)

def inserir_data_na_viagem(request):

    nova_viagem = Viagem()

    nova_viagem.data = request.POST['trip_date']

    nova_viagem.save()

    
    return redirect('cadastro-viagens-edit', id=nova_viagem.auto_increment_id)



def inserir_data_na_viagem_com_id(request, id):

    viagem_cadastrada = Viagem.objects.get(auto_increment_id=id)

    viagem_cadastrada.data = request.POST['trip_date']

    viagem_cadastrada.save()

    return redirect('cadastro-viagens-edit', id=id)

def inserir_suporte(request):

    context = {
        'suportes': Suporte.objects.all()
    }
    
    return render(request, 'inserir-suporte.html', context)

def inserir_suporte_id(request, id):

    context = {
        'id':id,
        'suportes': Suporte.objects.all()
    }
   
    return render(request, 'inserir-suporte.html', context)

def suporte_add(request):

    viagem = Viagem()
    viagem.save()

    suporte = Suporte.objects.get(nome=request.POST['suportes'])
    viagem.suportes.add(suporte)
    
    return redirect('cadastro-viagens-edit', id=viagem.auto_increment_id)

def suporte_add_id(request, id):
    viagem = Viagem.objects.get(auto_increment_id=id)

    suporte = Suporte.objects.get(nome=request.POST['suportes'])
    viagem.suportes.add(suporte)

    viagem.save()

    return redirect('cadastro-viagens-edit', id=id)

def deletar_suporte(request, id, nome):

    viagem = Viagem.objects.get(auto_increment_id=id)

    suporte = Suporte.objects.get(nome=nome)

    viagem.suportes.remove(suporte)

    return redirect('cadastro-viagens-edit', id)

def inserir_servico(request):

    context = {
        'servicos': Servico.objects.all()
    }

    return render(request, 'inserir-servico.html', context)

def inserir_servico_id(request, id):

    context = {
        'id': id,
        'type': type(id),
        'servicos': Servico.objects.all()
    }

    return render(request, 'inserir-servico.html', context)

def servico_add(request):

    viagem = Viagem()
    viagem.save()
    servico = Servico.objects.get(id=request.POST['servicos'])
    viagem.servicos.add(servico)

    return redirect('cadastro-viagens-edit', id=viagem.auto_increment_id)

def servico_add_id(request, id):

    viagem = Viagem.objects.get(auto_increment_id=id)

    servico = Servico.objects.get(id=request.POST['servicos'])

    viagem.servicos.add(servico)


    return redirect('cadastro-viagens-edit', id=id)

def deletar_servico(request, id, servico):

    viagem = Viagem.objects.get(auto_increment_id=id)
    servico = Servico.objects.get(nome=servico)
    viagem.servicos.remove(servico)


    return redirect('cadastro-viagens-edit', id=id)

def tela_cadastros(request):

    return render(request, 'tela-cadastros.html')

def cadastro_lojas(request):

    context = {
        'filiais': Loja.objects.filter(tipo='Filial')
    }

    return render(request, 'cadastro-lojas.html', context)

def inserir_loja_bd(request):
    
    loja = Loja()

    loja.sigla = request.POST['sigla']
    loja.sigla = loja.sigla.upper()
    loja.cidade = request.POST['cidade']
    loja.uf = request.POST['uf']
    loja.uf = loja.uf.upper()
    loja.tipo = request.POST['tipo-loja']
    if request.POST['tipo-loja'] == 'Filial':
        loja.tipo = request.POST['tipo-loja']
        loja.loja_mae = request.POST['sigla'].upper()
    else:
        loja.tipo = request.POST['tipo-loja']
        loja.loja_mae = request.POST['loja-mae']

    loja.latitude_longitude = request.POST['coordenadas']
    loja.save()

    print(loja.tipo)
    print(loja.loja_mae)

    return redirect('cadastro-lojas-toast')

def cadastro_lojas_toast(request):
    return render(request, 'cadastro-lojas-toast.html')

def cadastro_suporte(request):

    return render(request, 'cadastro-suportes.html')

def inserir_suporte_db(request):

    suporte = Suporte()

    suporte.nome = request.POST['nome']

    try:
        whatsap_int = int(request.POST['whatsapp'])
    except:
        return redirect('cadastro-suportes')
    
    suporte.whatsapp = whatsap_int

    suporte.save()

    return redirect('cadastro-suportes-toast')

def cadastro_suportes_toast(request):

    return render(request, 'cadastro-suportes-toast.html')
# =================================================================================
# cadastro usuarios
def cadastro_usuario(request):

    form = CreateUserFom()

    if request.method == 'POST':
        form = CreateUserFom(request.POST)

        if form.is_valid():

            form.save()

            return redirect('cadastro-usuarios')

    context = {'form': form}

    return render(request, 'cadastro-usuarios.html', context)
# ==========================================================================================

def cadastro_servico(request):

    return render(request, 'cadastro-servicos.html')

def inserir_servico_bd(request):

    servico = Servico()
    servico.nome = request.POST['nome']
    servico.save()

    return redirect('cadastro-servicos-toast')

def cadastro_servicos_toast(request):

    return render(request, 'cadastro-servicos-toast.html')

# ====================================================================
# =============== # REGISTER # =====================================#

def register(request):

    form = CreateUserFom()

    if request.method == 'POST':
        form = CreateUserFom(request.POST)

        if form.is_valid():

            form.save()

            n_usuario = User.objects.get(username=form['username'].value())

            senha_usuario = SenhaUsuario()
            senha_usuario.senha = form['password1'].value()
            senha_usuario.save()


            senha_usuario.usuario = n_usuario
            senha_usuario.save()

            if request.POST['create-suport'] == 'sim':
                suporte = Suporte()
                suporte.nome = form['username'].value()
                suporte.save()

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('cadastro-usuarios')
        else:
            messages.error(request, 'Não conseguimos processar sua solicitação')
            return redirect('cadastro-usuarios')

    context = {'form': form}

    return redirect('cadastro-usuarios', context)

# =========================================================================

def cadastro_usuarios_toast(request):

    return render(request, 'cadastro-usuarios-toast.html')

def consulta_cadastros(request):

    return render(request, 'consulta-cadastros.html')

def consulta_usuarios(request):

    usuario_paginator = Paginator(User.objects.filter(is_active=True).order_by('id'), 10)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)

    context = {
        'usuarios': page
    }
    
    return render(request, 'consulta-usuarios.html', context)

def consulta_suportes(request):

    suporte_paginator = Paginator(Suporte.objects.filter(desativado=False).order_by('id'), 10)
    page_num = request.GET.get('page')
    page = suporte_paginator.get_page(page_num)

    context = {
        'suportes': page
    }

    return render(request, 'consulta-suportes.html', context)

def consulta_lojas(request):

    loja_paginator = Paginator(Loja.objects.all().order_by('id'), 10)
    page_num = request.GET.get('page')
    page = loja_paginator.get_page(page_num)


    context = {
        'lojas': page
    }

    return render(request, 'consulta-lojas.html', context)

def consulta_servicos(request):

    servico_paginator = Paginator(Servico.objects.all().order_by('id'), 10)
    page_num = request.GET.get('page')
    page = servico_paginator.get_page(page_num)

    context = {
        'servicos': page
    }

    return render(request, 'consulta-servicos.html', context)

def consulta_viagens(request):

    viagem_paginator = Paginator(Viagem.objects.all().order_by('-auto_increment_id'), 10)
    page_num = request.GET.get('page')
    page = viagem_paginator.get_page(page_num)

    context = {
        'viagens': page
    }

    return render(request, 'consulta-viagens.html', context)

def altera_usuario(request, username):

    context = {
        'usuario': User.objects.get(username=username)
    }


    return render(request, 'alterar-usuario.html', context )

def inserir_usuario_alterado(request, id):

    usuario = User.objects.get(id=id)
    u_senha = SenhaUsuario.objects.get(usuario=usuario)
    u_senha.senha = request.POST['password']
    u_senha.save()

    usuario.username = request.POST['usuario']
    usuario.email = request.POST['email']
    usuario.set_password(request.POST['password'])

    role = request.POST['role']
    if role == 'Tecnico':
        usuario.is_staff = False
    else:
        usuario.is_staff = True

    usuario.save()


    return redirect('consulta-cadastros')

def excluir_usuario(request, id):
    context = {
        'usuario' : User.objects.get(id=id)
    }
    
    return render(request, 'excluir-usuario.html', context)

def confirmar_exclusao_usuario(request, id):

    usuario = User.objects.get(id=id)

    if usuario.is_staff:
        if usuario.is_superuser:
            return redirect('consulta-cadastros')
        
        usuario.is_active = False
        usuario.save()

        return redirect('consulta-cadastros')
    
    elif usuario.is_superuser:
        return redirect('consulta-cadastros')
    else:
        usuario.delete()

    return redirect('consulta-cadastros')

def alterar_suporte(request, id):

    context = {
        'suporte': Suporte.objects.get(id=id)
    }

    return render(request, 'alterar-suporte.html', context)

def inserir_suporte_alterado(request, id):

    suporte = Suporte.objects.get(id=id)
    suporte.nome = request.POST['nome']
    suporte.whatsapp = request.POST['whatsapp']
    suporte.save()

    return redirect('consulta-cadastros')

def excluir_suporte(request, id):

    context = {
        'suporte': Suporte.objects.get(id=id)
    }

    return render(request, 'excluir-suporte.html', context)

def confirmar_exclusao_suporte(request, id):

    suporte = Suporte.objects.get(id=id)

    suporte.desativado = True
    suporte.save()

    return redirect('consulta-cadastros')

def alterar_loja(request, id):

    context = {
        'loja': Loja.objects.get(id=id),
        'filiais': Loja.objects.filter(tipo='Filial')
    }

    return render(request, 'alterar-loja.html', context)

def inserir_loja_alterada(request, id):

    loja = Loja.objects.get(id=id)

    loja.sigla = request.POST['sigla']
    loja.cidade = request.POST['cidade']
    loja.uf = request.POST['uf']
    loja.tipo = request.POST['tipo-loja']
    loja.loja_mae = request.POST['loja-mae']
    loja.latitude_longitude = request.POST['latitude-longitude']
    loja.postos = request.POST['posto']
    loja.republica = request.POST['republica']
    loja.save()

    return redirect('consulta-cadastros')

def excluir_loja(request, id):

    context = {
        'loja': Loja.objects.get(id=id)
    }

    return render(request, 'excluir-loja.html', context)

def confirmar_exclusao_loja(request, id):

    loja = Loja.objects.get(id=id)
    loja.delete()

    return redirect('consulta-cadastros')

def modal_info_senha(request, id):

    context = {
        'usuario': User.objects.get(id=id),
    }

    
    return render(request, 'modal-info-senha.html', context)

def alterar_servico(request, id):

    context = {
        'servico': Servico.objects.get(id=id)
    }

    return render(request, 'alterar-servico.html', context)

def inserir_servico_alterado(request, id):

    servico = Servico.objects.get(id=id)
    servico_alterado = request.POST['servico']
    servico.nome = servico_alterado
    servico.save()

    return redirect('consulta-cadastros')

def excluir_servico(request, id):

    context = {
        'servico': Servico.objects.get(id=id)
    }

    return render(request, 'excluir-servico.html', context)

def confirma_exclusao_servico(request, id):

    servico = Servico.objects.get(id=id)
    servico.delete()

    return redirect('consulta-cadastros')

def excluir_viagem(request, id):

    context = {
        'viagem': Viagem.objects.get(auto_increment_id=id)
    }
    
    return render(request, 'excluir-viagem.html', context)

def confirmar_exclusao_viagem(request, id):

    viagem = Viagem.objects.get(auto_increment_id=id)
    viagem.delete()

    return redirect('consulta-cadastros')

def dashboard_viagens(request):

    context = {
        'viagens': Viagem.objects.filter(concluida=False).order_by('data'),
        'suportes': Suporte.objects.all()
    }
    

    return render(request, 'dashboard-viagens.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario não existe!')
            return redirect('index')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Senha incorreta!')
            return redirect('index')

    return render(request, 'index.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')

def perfil(request, id):
    
    form = SuporteImage(instance=request.user.suporte)

    if request.method == 'POST':
        form = SuporteImage(request.POST, files=request.FILES, instance=request.user.suporte)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('inicio')
    
    context = {
        'usuario': User.objects.get(id=id),
        'form': form
    }

    
    
    return render(request, 'perfil.html', context)