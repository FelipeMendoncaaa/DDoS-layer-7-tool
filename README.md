# DDoS Layer 7 Tool

Ferramenta gráfica desenvolvida em **Python** para simulação de ataques **DDoS** (Distributed Denial of Service) na **camada 7** (Layer 7), com o objetivo de testar a resiliência de aplicações web. Através de uma interface amigável, você pode facilmente configurar e executar testes de carga para avaliar a capacidade do servidor em lidar com grandes volumes de tráfego malicioso.

## Funcionalidades

- **Interface gráfica intuitiva**: Usuários podem facilmente inserir a URL de destino e iniciar o ataque com poucos cliques.
- **Simulação de ataques DDoS na camada 7**: Ataques focados na sobrecarga de recursos da aplicação, testando endpoints críticos.
- **Locust como engine**: Utiliza o **Locust**, uma ferramenta poderosa de teste de carga, para gerar requisições em massa e simular ataques de alta frequência.
- **Customização da carga de ataque**: Defina o número de usuários simultâneos e a taxa de requisições por segundo, personalizando o teste de acordo com a necessidade.
- **Executado em segundo plano**: O ataque é iniciado em uma thread separada para que a interface continue responsiva.

## Como Funciona

Esta ferramenta permite que você teste a resiliência de sua aplicação web enviando uma quantidade massiva de requisições HTTP. O teste simula um ataque distribuído, com diferentes tipos de requisições sendo disparadas em alta frequência, o que é comum em ataques DDoS na camada de aplicação.

- **Requisições GET e POST**: Simula interações típicas com a aplicação, sobrecarregando recursos de processamento e memória.
- **Variação de tempo entre requisições**: Define intervalos entre requisições para simular comportamentos mais realistas.
  
## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/ddos-layer7-tool.git

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

3. **Executar a ferramenta**:
  ```bash
   python3 ddos7.py
```
## Uso
  
Abrir a Interface: Após iniciar a ferramenta, uma janela gráfica aparecerá.
Inserir a URL: Digite o URL de destino para o teste de carga.
Iniciar o ataque: Clique em "Iniciar!" e o teste começará. Um pop-up será mostrado quando o ataque for iniciado.
Monitoramento em tempo real: A ferramenta rodará o teste em segundo plano, utilizando o Locust para gerar o tráfego de ataque.
