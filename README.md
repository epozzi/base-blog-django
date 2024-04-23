# Desenvolvimento de um blog utilizando Django


## Postagem

* Para criar e editar postagens foi criado modelo com
    - Título
    - Resumo
    - Conteúdo
    - Autor
    - Categoria
    - Publicar
    - Data

## Bibliotecas utilizadas

* Para edição no console admin foi utilizado a lib ckeditor (que está com um problema, pois não está utilizando a versão LTS uma vez que essa é paga)

    `pip install django-ckeditor`

    - Verificar a possibilidade de colocar o ckeditor 5 ou algum outro que faça a mesma função.

* Para o campo Categoria estou utilizando a lib multiselectfield

    `pip install django-multiselectfield`

    - Essa lib na versão atual tem um problema de compatibilidade com o Django 5.0 na funcionalidade flatchoices (ainda preciso estudar essa parte para entender)
    - Essa incompatibilidade é 'resolvida' editando o arquivo venv/lib/python3.10/site-packages/multiselectfield/db/fields.py retirando a função _get_flatchoices.