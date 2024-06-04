# Pesquisa de eBooks Automatizada com Python e Selenium 📚

Este projeto em Python foi desenvolvido para automatizar a busca de eBooks na Amazon, capturando screenshots e informações relevantes para análise. Utilizando a poderosa biblioteca Selenium, é possível interagir de forma programática com o navegador web, executando todas as etapas do processo de automação.

A automação abrange desde a pesquisa de eBooks na Amazon até a captura de screenshots das páginas de resultados. O projeto utiliza o WebDriver do Selenium para abrir o navegador, navegar até a página da Amazon, inserir os termos de pesquisa e clicar nos botões necessários, garantindo uma experiência de automação robusta.

Além disso, foi implementada uma pipeline de integração contínua utilizando o GitActions. Esta pipeline executa os testes automatizados do projeto após cada commit no repositório, assegurando a qualidade do código. Após a conclusão dos testes, o GitActions envia notificações para um bot no Telegram, proporcionando feedback imediato sobre o sucesso ou falha dos testes. Essa integração contínua é fundamental para identificar rapidamente problemas e manter a eficiência do projeto.

## Pipeline de Testes Automatizados com Notificação no Telegram

Este repositório inclui uma pipeline automatizada que executa os testes definidos no projeto e envia uma mensagem de notificação no Telegram com os resultados.

### Recursos da Pipeline:

- **Testes Automatizados:** A pipeline executa os testes automatizados definidos no projeto para garantir sua integridade e qualidade.

- **Integração Contínua:** A pipeline é acionada automaticamente sempre que há uma nova alteração no repositório, garantindo que os testes sejam executados regularmente.

- **Notificação no Telegram:** Após a conclusão dos testes, a pipeline envia uma mensagem no Telegram para notificar os desenvolvedores sobre o status dos testes.

### Como Funciona:

1. **Configuração da Pipeline:** A pipeline está configurada usando uma ferramenta de integração contínua, como GitHub Actions ou GitLab CI/CD. Os detalhes específicos da configuração podem ser encontrados nos arquivos de configuração da pipeline no repositório.

2. **Execução dos Testes:** Durante a execução da pipeline, os testes automatizados são executados para verificar se o projeto está funcionando conforme esperado.

3. **Notificação no Telegram:** Após a conclusão dos testes, a pipeline envia uma mensagem no Telegram para um grupo ou canal especificado, informando sobre o resultado dos testes.

### Contribuições:

Contribuições para a melhoria da pipeline ou para adicionar novos recursos são bem-vindas! Se você tem sugestões ou ideias para melhorar a pipeline de testes automatizados, sinta-se à vontade para enviar um pull request.

***Recursos e Tecnologias Utilizadas:***
- Python ✅
- Biblioteca Selenium ✅
- WebDriver do Selenium ✅

***Link dos produtos pesquisados:***
- https://www.amazon.com.br/gp/product/B0B7GMVYJS?ref_=dbs_p_pwh_rwt_cpsb_cl_0&storeType=ebooks
- https://www.amazon.com.br/Manual-QAINICIANTE-implementar-qualidade-software-ebook/dp/B0C2X172QC/?_encoding=UTF8&pd_rd_w=NxZCe&content-id=amzn1.sym.ca21ea20-e0a6-4fcd-9709-8136382a6f66%3Aamzn1.symc.d10b1e54-47e4-4b2a-b42d-92fe6ebbe579&pf_rd_p=ca21ea20-e0a6-4fcd-9709-8136382a6f66&pf_rd_r=M62PHYSHQDNNWAPKYMN4&pd_rd_wg=pZFOW&pd_rd_r=66d02168-0e70-48de-8f1b-e8db9a9f2706&ref_=pd_hp_d_atf_ci_mcx_mr_hp_atf_m
