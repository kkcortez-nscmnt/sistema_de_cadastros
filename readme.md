<h1 align="center"> TestDev - Django REST FrameWork </h1>

<p align ="center"> Sistema de Cadastro Proddutos-Fornecedores<p>

Objetivos implementados:

- Criar endpoints para CRUD de **produtos**. O produto deve conter nome, data de cadastro, data de atualização e descrição. O `nome` do **produto** deve ser único e não pode ultrapassar 200 caracteres, porém a `descrição` é opcional e deve permitir inserir um texto longo.
- Um **produto** sempre deverá ter uma **categoria**.
- Um **produto** deverá ter vários **fornecedores**. E em cada **fornecedor**, deverá ser informado o preço de custo do produto com este fornecedor. Da mesma forma, o **fornecedor** poderá conter vários **produtos**.
- Criar endpoints para CRUD de **categorias**. A categoria deve conter nome, data de cadastro e data de atualização. O nome da categoria deve ser única.
- Criar endpoins para CRUD de **fornecedores**, com Nome Fantasia, Razão Social, Endereço, CNPJ e Telefones para contato. A forma de organização do endereço e telefones fica a seu critério em relação a estrutura de dados (tabelas adicionais ou campos separados). Porém, os mesmos precisam sempre ser retornados junto com os dados fornecedor.

Objetivos não implementados:

- Quando houver algum erro na validação dos dados, isso precisa ser informado no endpoint em que ocorreu.
- Crie uma página web para consumir os endpoints.
