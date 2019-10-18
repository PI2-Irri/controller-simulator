# Simulador - Central de Controle

## Objetivo

O objetivo do simulador da central de controle é gerar medidas dos atuadores e dos módulos medidores a fim de simular a arquitetura distribuída alocada do irrigador e do sistema envolvido.

Os dados gerados são subdivididos em especificações de dados dos módulos e das medidas associadas, sendo elas divididas
em medidas do atuador e medidas dos módulos medidores:

### Dados de cada módulo medidor

```json
{
  "id": 1,
  "rf_address": "EF0102FF",
  "url": "http://localhost:3000/modules/1"
}
```

### Medidas do atuador

```json
{
  "id": 3,
  "water_consumption": 20.3,
  "reservoir_level": 3,
  "url": "http://localhost:3000/actuator_measurements/"
}
```

### Medidas da coleta dos módulos medidores

```json
{
  "id": 3,
  "temperature": 37.1,
  "ground_humidity": 50,
  "battery_level": 5,
  "module": "http://localhost:3000/modules/1/",
  "url": "http://localhost:3000/module_measurements/3/"
}
```

## Como utilizar?

### Ambiente de desenvolvimento

Para subir o ambiente de desenvolvimento, você deve ter o _docker_ e o _docker-compose_ instalados.

Após a instalação de ambos, caso seja a primeira vez que o ambiente é usado ou quando realiza alguma alteração no arquivo _Dockerfile_, execute:

sudo docker-compose up --build

Caso contrário, após ter feito a _build_ anteriormente, mas sem realizar alterações no _Dockerfile_, use:

sudo docker-compose up

Para acessar o _container_ ou do simulador:

sudo docker exec -it simulator-api bash

ou de seu banco associado:

sudo docker exec -it simulator-db bash

## Endpoints

### ```/modules/```

Objetivo: realizar a criação, a leitura, a deleção e a modificação dos dados relativos aos módulos medidores.

Verbo: ```GET``` - Sem parâmetros

```200```: quando a requisição é feita com sucesso, retorna uma lista de módulos

| Saída               | Tipo            | Descrição                            |
| :-----------------: | :-------------: | :----------------------------------: |
| ```id```            | ``` integer ``` | Id do módulo                         |
| ```rf_address```    | ``` string ```  | Endereço RF para comunicação         |
| ```url```           | ``` string ```  | Url para acessar o módulo específico |

Verbo: ```POST``` - Com parâmetros

| Parâmetros de entrada     | Descrição                       |
| :-----------------------: | :-----------------------------: |
| rf_address                | Endereço RF para comunicação    |

Verbo: ```PUT ou PATCH``` - Com parâmetros

| Parâmetros de entrada     | Descrição                       |
| :-----------------------: | :-----------------------------: |
| rf_address                | Endereço RF para comunicação    |


### ```/module_measurements/```

Verbo: ```GET``` - Sem parâmetros

```200```: quando a requisição é feita com sucesso, retorna uma lista de medidas relacionadas aos módulos cadastrados

| Saída                    | Tipo             | Descrição                            |
| :----------------------: | :--------------: | :----------------------------------: |
| ```id```                 | ``` integer ```  | Id do módulo                         |
| ```temperature```        | ``` float ```    | Temperatura do solo                  |
| ```ground_humidity```    | ``` integer ```  | Umidade do solo                      |
| ```battery_level```      | ``` integer ```  | Nível de bateria do módulo medidor   |
| ```url```                | ``` string ```   | Url para acessar o módulo específico |

### ```/actuator_measurements/```

Verbo: ```GET``` - Sem parâmetros

```200```: quando a requisição é feita com sucesso, retorna uma lista de medidas relacionadas aos atuadores

| Saída                    | Tipo             | Descrição                            |
| :----------------------: | :--------------: | :----------------------------------: |
| ```id```                 | ``` integer ```  | Id do módulo                         |
| ```water_consumption```  | ``` float ```    | Consumo de água a cada irrigação     |
| ```reservoir_level```    | ``` integer ```  | Nível do reservatório de água        |
| ```url```                | ``` string ```   | Url para acessar o módulo específico |
