"""
NESSE MÓDULO É CRIADO AS CLASSES QUE VIRARÃO TABELAS NO BANCO DE DADOS
"""

from django.db import models

# As classes têm que herdar de models.Model para que se tenha acesso aos métodos de criar tabela
class Course(models.Model):
    # CharField é um campo de texto e tem no máximo 100 caracteres (max_length=100)
    name = models.CharField('Nome', max_length=100)

    # SlugField vai servir pra colocar urls
    slug = models.SlugField('Atalho')
    
    # TextField não tem limite de caracteres, blanck=True significa que o campo não é obrigatório
    description = models.TextField('Descrição', blank=True)
    
    # null=True significa que pode ter o valor nulo
    start_date = models.DateField('Data de início', null=True, blank=True)
    
    # Django não armazena imagens no banco de dados, mas sim o caminho onde vai salvá-las
    # É necessário adicionar ao settings o caminho onde será salvo as imagens (MEDIA_ROOT)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    
    # Ao criar o curso auto_now_add automaticamente coloca a data atual
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    
    # Ao atualizar o curso auto_now automaticamente coloca a data atual
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

