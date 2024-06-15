from django.urls import path
from home.views import main, viagens_em_andamento, viagens_encerradas,\
    viagens_programadas_para_este_mes, viagens_programadas_para_o_proximo_mes,\
        postos, recibos, recibo_botao_consultar, consulta_postos, cadastro_rcibos,\
            incluir_recibos, cadastro_viagens,cadastro_viagens_edit, inserir_loja,\
            loja_add, inserir_loja_edit, loja_add_edit, deletar_loja, inserir_data_sem_parametros,\
            inserir_data_na_viagem, inserir_data_na_viagem_com_id, inserir_data_com_parametros,\
            deletar_data, inserir_suporte,suporte_add,inserir_suporte_id, suporte_add_id,\
            deletar_suporte, inserir_servico, servico_add, servico_add_id, inserir_servico_id,\
            deletar_servico, tela_cadastros, cadastro_lojas, inserir_loja_bd, cadastro_lojas_toast,\
            cadastro_suporte, cadastro_usuario, cadastro_servico, inserir_servico_bd, cadastro_servicos_toast,\
            inserir_suporte_db, cadastro_suportes_toast, cadastro_viagens_insert, deletar_chamado,\
            cadastro_viagens_edit_insert, register, cadastro_usuarios_toast, consulta_cadastros,\
            consulta_usuarios, consulta_suportes, consulta_lojas, consulta_servicos, consulta_viagens,\
            cadastro_viagens_edit_toast, altera_usuario, inserir_usuario_alterado, excluir_usuario,\
            confirmar_exclusao_usuario, alterar_suporte, inserir_suporte_alterado, excluir_suporte,\
            confirmar_exclusao_suporte, alterar_loja, inserir_loja_alterada, excluir_loja, confirmar_exclusao_loja,\
            modal_info_senha, alterar_servico, inserir_servico_alterado, excluir_servico, confirma_exclusao_servico,\
            excluir_viagem, confirmar_exclusao_viagem, dashboard_viagens, inserir_data_saida, insert_date_saida, \
            deletar_data_saida, inserir_data_saida_com_id, insert_date_saida_id, loginPage, logoutUser, perfil

            #index, 

urlpatterns = [
    # path('', index, name='index'),
    path('', loginPage, name='index'),
    path('logout/', logoutUser, name='logout'),
    path('inicio/', main, name='inicio' ),
    path('viagens-em-andamento/', viagens_em_andamento, name='viagens-em-andamento'),
    path('viagens-ecerradas/', viagens_encerradas, name='viagens-encerradas'),
    path('viagens-programadas-para-este-mes/', viagens_programadas_para_este_mes, name='viagens-programadas-para-este-mes'),
    path('viagens-programadas-para-o-proximo-mes/', viagens_programadas_para_o_proximo_mes, name='viagens-programadas-para-o-proximo-mes'),
    path('postos/', postos, name='postos' ),
    path('recibos/', recibos, name='recibos' ),
    path('consultar-recibos/', recibo_botao_consultar, name='recibo-botao-consultar'),
    path('consulta-postos/', consulta_postos, name='consulta-postos'),
    path('cadastro-de-recibos/', cadastro_rcibos, name='cadastro-recibos'),
    path('inclusao-de-recibos/', incluir_recibos, name='incluir-recibos'),
    path('cadastro-viagens/', cadastro_viagens, name='cadastro-viagens'),
    path('cadastro-viagens/<int:id>', cadastro_viagens_edit, name='cadastro-viagens-edit'),
    path('loja-add/', loja_add, name='loja-add'),
    path('loja-add-edit/<int:id>', loja_add_edit, name='loja-add-edit'),
    path('deletar-loja/<int:id>/<str:loja>', deletar_loja, name='deletar-loja'),
    path('deletar-data/<int:id>', deletar_data, name='deletar-data'),
    path('deletar-data-saida/<int:id>', deletar_data_saida, name='deletar-data-saida'),
    path('inserir-data/', inserir_data_sem_parametros, name='inserir-data'),
    path('inserir-data-saida/', inserir_data_saida, name='inserir-data-saida'),
    path('inserir-data-saida/<int:id>', inserir_data_saida_com_id, name='inserir-data-saida'),
    path('inserir-data/<int:id>', inserir_data_com_parametros, name='inserir-data'),
    path('insert-date/', inserir_data_na_viagem, name='insert-date'),
    path('insert-date-saida/', insert_date_saida, name='insert-date-saida'),
    path('insert-date-saida/<int:id>', insert_date_saida_id, name='insert-date-saida'),
    path('insert-date/<int:id>', inserir_data_na_viagem_com_id, name='insert-date'),
    path('inserir-suporte/', inserir_suporte, name='inserir-suporte'),
    path('inserir-suporte/<int:id>', inserir_suporte_id, name='inserir-suporte'),
    path('suporte-add/', suporte_add, name='suporte-add'),
    path('suporte-add/<int:id>', suporte_add_id, name='suporte-add'),
    path('deletar-suporte/<int:id>/<str:nome>', deletar_suporte, name='deletar-suporte'),
    path('inserir-servico/', inserir_servico, name='inserir-servico'),
    path('inserir-servico/<int:id>', inserir_servico_id, name='inserir-servico'),
    path('servico-add/', servico_add, name='servico-add'),
    path('servico-add/<int:id>', servico_add_id, name='servico-add'),
    path('deletar-servico/<int:id>/<str:servico>', deletar_servico, name='deletar-servico'),
    path('cadastro/', tela_cadastros, name='cadastro'),
    path('cadastro-lojas/', cadastro_lojas, name='cadastro-lojas'),
    path('inserir-loja-bd/', inserir_loja_bd, name='inserir-loja-bd'),
    path('cadastro-lojas-toast/', cadastro_lojas_toast, name='cadastro-lojas-toast'),
    path('cadastro-suportes/', cadastro_suporte, name='cadastro-suportes'),
    path('cadastro-usuarios/', cadastro_usuario, name='cadastro-usuarios'),
    path('cadastro-servicos/', cadastro_servico, name='cadastro-servicos'),
    path('inserir-servico-bd/', inserir_servico_bd, name='inserir-servico-bd'),
    path('cadastro-servicos-toast/', cadastro_servicos_toast, name='cadastro-servicos-toast'),
    path('inserir-suporte-db/', inserir_suporte_db, name='inserir-suporte-db'),
    path('cadastro-suportes-toast/', cadastro_suportes_toast, name='cadastro-suportes-toast'),
    path('cadastro-viagens-insert/', cadastro_viagens_insert, name='cadastro-viagens-insert'),
    path('deletar-chamado/<int:id>/', deletar_chamado, name='deletar-chamado'),
    path('cadastro-viagens-edit-insert/<int:id>/', cadastro_viagens_edit_insert, name='cadastro-viagens-edit-insert'),
    path('register/', register, name='register'),
    path('cadastro-usuarios-toast/', cadastro_usuarios_toast, name='cadastro-usuarios-toast'),
    path('consulta-cadastros/', consulta_cadastros, name='consulta-cadastros'),
    path('consulta-usuarios/', consulta_usuarios, name='consulta-usuarios'),
    path('consulta-suportes/', consulta_suportes, name='consulta-suportes'),
    path('consulta-lojas/', consulta_lojas, name='consulta-lojas'),
    path('consulta-servicos/', consulta_servicos, name='consulta-servicos'),
    path('consulta-viagens/', consulta_viagens, name='consulta-viagens'),
    path('cadastro-viagens-edit-toast/', cadastro_viagens_edit_toast, name='cadastro-viagens-edit-toast'),
    path('consulta-usuarios-editar/<str:username>', altera_usuario, name='altera-usuario'),
    path('inserir-usuario-alterado/<int:id>', inserir_usuario_alterado, name='inserir-usuario-alterado'),
    path('excluir-usuario/<int:id>', excluir_usuario, name='excluir-usuario'),
    path('confirmar-exclusao-cadastro/<int:id>', confirmar_exclusao_usuario, name='confirmar-exclusao-cadastro'),
    path('alterar-suporte/<int:id>', alterar_suporte, name='alterar-suporte'),
    path('inserir-suporte-alterado/<int:id>', inserir_suporte_alterado, name='inserir-suporte-alterado'),
    path('excluir-suporte/<int:id>', excluir_suporte, name='excluir-suporte'),
    path('confirmar-exclusao-suporte/<int:id>', confirmar_exclusao_suporte, name='confirmar-exclusao-suporte'),
    path('alterar-loja/<int:id>', alterar_loja, name='alterar-loja'),
    path('inserir-loja-alterada/<int:id>', inserir_loja_alterada, name='inserir-loja-alterada'),
    path('excluir-loja/<int:id>', excluir_loja, name='excluir-loja'),
    path('confirmar-exclusao-loja/<int:id>', confirmar_exclusao_loja, name='confirmar-exclusao-loja'),
    path('modal-info-senha/<int:id>', modal_info_senha, name='modal-info-senha'),
    path('alterar-servico/<int:id>', alterar_servico, name='alterar-servico'),
    path('inserir-servico-alterado/<int:id>', inserir_servico_alterado, name='inserir-servico-alterado'),
    path('excluir-servico/<int:id>', excluir_servico, name='excluir-servico'),
    path('confirma-exclusao-servico/<int:id>', confirma_exclusao_servico, name='confirma-exclusao-servico'),
    path('excluir-viagem/<int:id>', excluir_viagem, name='excluir-viagem'),
    path('confirmar-exclusao-viagem/<int:id>', confirmar_exclusao_viagem, name='confirmar-exclusao-viagem'),
    path('dashboard-viagens/', dashboard_viagens, name='dashboard-viagens'),
    path('perfil/<int:id>', perfil, name='perfil'),









    # path('login/', loginPage, name='login'),
    # path('logout/', logoutUser, name='logout'),
    # path('encerrar-manutencao/', encerrar_manutencao, name='encerrar-manutencao')
]

htmx_urlpatterns = [
    path('inserir-loja/', inserir_loja, name='inserir-loja'),
    path('inserir-loja-edit/<int:id>', inserir_loja_edit, name='inserir-loja-edit'),
]

urlpatterns += htmx_urlpatterns