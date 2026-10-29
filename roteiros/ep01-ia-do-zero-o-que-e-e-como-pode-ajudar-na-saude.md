---
projeto: "Estrateg[IA]"
temporada: 1
episodio: 1
titulo: "Inteligência Artificial do zero: da conversa à criação"
publicacao_planejada: "2026-11-16"
duracao_alvo_minutos: "35–42 (inclui demonstrações e pausas)"
status: "versão 2 — reconstruída, a ensaiar e testar na ferramenta"
formato: "professora na câmera + slides HTML + gravação de tela"
---

# Aula 01 — Inteligência Artificial do zero: da conversa à criação

**Professora:** Rosa Kethllyn, enfermeira, especialista em educação permanente e em criação com IA.  
**Público:** profissionais e gestores da saúde, inclusive quem nunca utilizou IA.  
**Promessa pedagógica:** compreender modelo, aplicativo, contexto, chatbot, ferramentas e agente; distinguir respostas de execução e criar, testar e revisar um protótipo simples com dados fictícios.  
**Duração estimada:** 35–42 minutos, dependendo do ritmo e da execução. Marcas de tempo são guias, não metragem garantida.

> Referência de estrutura: Aula 1 de Ruan Braz, *Claude Code for Beginners | From Basic to Advanced* (39 min). Análise feita com base nos capítulos e no resumo disponibilizado publicamente, **não em transcrição integral**. Este roteiro é original, com exemplos próprios e foco em IA geral e saúde. Fonte: https://www.youtube.com/watch?v=P3PSw-mhPDM .
>
> **Para gravar:** os blocos de fala são completos. As marcações de câmera, prompts e pausas de interação não devem ser lidos literalmente. Mostre resultados reais da ferramenta escolhida; nunca antecipe uma saída como se já tivesse ocorrido. Revise preços, botões, disponibilidade de recursos e políticas na data de gravação.
>
> **Segurança:** todas as atividades são fictícias. Nenhum prontuário, dado sensível ou documento institucional não autorizado é necessário.

## 01 — ABERTURA — O QUE ESTAMOS DEIXANDO DE FAZER COM A IA | 00:00–02:30

**PRODUÇÃO:** CÂMERA: abrir sem vinheta longa. Mostrar muito rapidamente um antes/depois do painel interativo que será construído. Não atribuir resultados fictícios a uma ferramenta real.

**FALAS PARA TELEPROMPTER:**

> Quando você ouve falar em inteligência artificial, o que vem na sua cabeça? ChatGPT? Um robô respondendo perguntas? Ou alguma coisa muito complicada, que só quem programa consegue usar?
>
> Eu quero começar essa aula te mostrando uma diferença. Uma coisa é abrir um chat, fazer uma pergunta, copiar a resposta e fechar a página. Outra coisa é entender o que está por trás daquela ferramenta e perceber que você pode usar a IA pra pesquisar, analisar arquivos, organizar um projeto, criar um material e até construir uma pequena ferramenta que antes você nem saberia por onde começar.
>
> Não estou dizendo que você deve entregar suas decisões pra uma máquina. Principalmente na saúde, isso seria um erro. Eu estou falando de aprender a usar uma tecnologia que já consegue produzir muito mais do que respostas em texto, desde que você saiba dar direção e conferir o resultado.
>
> Olha esse painel que está aparecendo aqui na tela. Ele tem indicadores fictícios, atividades, filtros e botões. Não é um sistema hospitalar de verdade. É uma demonstração que a gente vai construir do zero ao longo dessa aula, usando uma conversa com IA. E eu vou te explicar o que está acontecendo por trás, passo a passo.
>
> Então, se você nunca usou inteligência artificial, ou se já usa mas sente que só conversa com ela, fica comigo. Hoje você não precisa decorar comandos. Precisa construir um mapa mental que vai fazer os próximos conteúdos deste canal terem muito mais sentido.

## 02 — APRESENTAÇÃO E O QUE É O ESTRATEG[IA] | 02:30–04:10

**PRODUÇÃO:** CÂMERA: GC Rosa Kethllyn | Enfermeira, especialista em educação permanente e criação com IA. Mostrar discretamente o logo e o nome do canal.

**FALAS PARA TELEPROMPTER:**

> Antes de continuar, deixa eu me apresentar. Meu nome é Rosa Kethllyn, eu sou enfermeira, especialista em educação permanente e em criação com inteligência artificial, e sou a criadora do Estrateg[IA].
>
> Eu conheço de perto a linguagem e os desafios de quem trabalha na saúde. Mas o que eu quero ensinar aqui não é só um jeito de fazer um relatório mais rápido. A minha proposta é que você realmente aprenda inteligência artificial: desde os primeiros conceitos até ferramentas que consigam ajudar você a criar coisas e trabalhar de uma forma diferente.
>
> Isso significa que nós vamos falar de ChatGPT, de Claude, de ferramentas de pesquisa, de criação de conteúdo, de projetos, agentes, automações e, mais pra frente, até de construção de soluções sem precisar ter uma formação em programação.
>
> Eu vou usar exemplos de gestão da saúde porque esse é o nosso território. Mas o conhecimento sobre IA que você vai construir aqui vale pra muito mais coisas. E eu quero que você saia das aulas entendendo o raciocínio, não apenas reproduzindo um botão que pode mudar de lugar amanhã.
>
> Se surgir algum termo novo, não precisa parar o vídeo pra decorar. Eu tenho um glossário gratuito do Estrateg[IA], que vou deixar na descrição. A gente vai entender cada conceito no momento em que ele fizer sentido.

## 03 — O MAPA — MODELO, APLICATIVO E AGENTE | 04:10–07:25

**PRODUÇÃO:** SLIDES: três camadas MODEL0 → APLICATIVO → FERRAMENTAS/AGENTE; destacar diferenças. Evitar apresentar marcas como equivalentes exatos de produtos ou modelos.

**FALAS PARA TELEPROMPTER:**

> Pra começar, precisamos separar três coisas que parecem iguais, mas não são: o modelo de inteligência artificial, o aplicativo que você usa pra conversar com ele e os recursos que permitem que ele faça tarefas.
>
> Imagina um hospital. Você pode ter uma equipe com conhecimento técnico. Mas, pra essa equipe conseguir trabalhar, também precisa de um ambiente, de acesso às informações necessárias, de processos e de instrumentos. Com a IA acontece algo semelhante, embora a comparação não seja perfeita.
>
> O modelo de linguagem é a tecnologia treinada pra processar e gerar linguagem. Ele pode ajudar a explicar um conceito, resumir um texto, analisar uma solicitação e produzir uma resposta. Já o aplicativo é o lugar em que você usa esse modelo: por exemplo, uma conversa no ChatGPT ou no Claude.
>
> E aí existem as ferramentas. Dependendo da configuração e das permissões, o aplicativo pode pesquisar na internet, trabalhar com arquivos, gerar imagens, produzir código ou se conectar a serviços externos. Nem toda conta oferece tudo isso e nem todo modelo pode usar todas essas ferramentas.
>
> Essa distinção vai evitar uma confusão muito comum. Quando alguém fala 'o GPT consegue fazer isso' ou 'o Claude faz aquilo', a gente precisa perguntar: você está falando do modelo, do aplicativo ou de alguma ferramenta conectada a ele? Às vezes o que parece uma capacidade mágica depende, na verdade, de um recurso específico que precisa estar disponível.
>
> Vamos pensar no nosso exercício. Eu posso pedir que um modelo escreva como deveria ser um painel. Mas pra ele construir um arquivo, editar algo ou abrir uma página, eu preciso de algum caminho que permita trabalhar com esses arquivos. E pra usar dados reais de uma instituição, preciso de muito mais: autorização, segurança e integração adequada.
>
> Guarda essa ideia: modelo é uma parte, aplicativo é outra e capacidade de agir depende de ferramentas e limites. Agora sim dá pra entender por que duas pessoas usando a mesma IA podem conseguir resultados muito diferentes.

## 04 — COMO UMA IA GENERATIVA FUNCIONA, SEM MISTÉRIO | 07:25–11:10

**PRODUÇÃO:** SLIDES: processo de treinamento simplificado; tokens; contexto; previsão de continuação. Não afirmar que todo modelo é idêntico ou que treina com conversas pessoais da pessoa.

**FALAS PARA TELEPROMPTER:**

> Mas afinal, por que esse modelo consegue responder tanta coisa? Sem entrar numa aula de matemática, a ideia é a seguinte: modelos de linguagem são treinados com grandes quantidades de exemplos e aprendem padrões nas relações entre palavras, estruturas, ideias e outros tipos de informação.
>
> Quando você escreve um pedido, a ferramenta processa esse pedido em partes menores, frequentemente chamadas de tokens. Você pode imaginar os tokens como pedacinhos que o sistema usa pra trabalhar com a linguagem. Um token não é necessariamente uma palavra inteira; dependendo do texto, pode ser uma parte de palavra, um sinal ou outra unidade.
>
> A partir do contexto recebido e do que o modelo aprendeu no treinamento, ele gera uma resposta, avançando passo a passo. Isso é muito mais sofisticado do que escolher uma frase pronta de um banco de respostas, mas também não significa que ele esteja consultando automaticamente uma fonte verdadeira a cada frase que escreve.
>
> É por isso que a IA às vezes responde com muita segurança e mesmo assim erra. Ela pode criar uma referência que não existe, confundir uma data, interpretar um arquivo de maneira incorreta ou completar uma informação que estava faltando como se ela fosse real.
>
> Na saúde, isso exige um cuidado adicional. Imagine pedir uma síntese de uma diretriz clínica. O texto pode parecer impecável, mas se um detalhe estiver errado, as consequências podem ser importantes. Então a ferramenta pode ajudar a localizar pontos pra estudo, estruturar perguntas e organizar uma análise; ela não substitui a consulta à fonte oficial, o protocolo vigente nem a responsabilidade profissional.
>
> Outra palavra importante é contexto. Contexto é aquilo que a ferramenta tem disponível para entender a tarefa naquele momento: sua pergunta, trechos anteriores da conversa, instruções, arquivos que você compartilhou e os resultados de ferramentas autorizadas, conforme o produto.
>
> Quanto mais claro e relevante for o contexto, maior a chance de a resposta ser útil. Mas contexto não é memória infinita. Existem limites de quantidade de informação que podem ser processados de cada vez, e conversas muito longas podem precisar de resumos ou de uma organização melhor.
>
> Então, antes de pensar em 'qual é o melhor prompt do mundo', eu quero que você entenda que o resultado depende muito de três coisas: o modelo, o contexto que você oferece e o trabalho de revisão que vem depois. Vamos guardar essas três porque elas vão aparecer na demonstração.

## 05 — CHATBOT, ASSISTENTE E AGENTE: QUAL É A DIFERENÇA? | 11:10–14:30

**PRODUÇÃO:** SLIDE: CHAT → PROJETO COM CONTEXTO → AGENTE COM FERRAMENTAS. Mostrar quatro passos do ciclo objetivo→planejar→agir→conferir.

**FALAS PARA TELEPROMPTER:**

> Até aqui nós falamos de conversa. Agora chegamos numa mudança importante: a diferença entre usar IA como chatbot e usar IA em um fluxo de trabalho.
>
> Quando você pergunta 'o que significa um indicador de qualidade?', ela te explica. Isso é uma interação típica de chatbot. Quando você pede 'analise esse conjunto fictício de informações, identifique perguntas e apresente um quadro', você já está conduzindo uma tarefa com etapas. E quando um sistema pode usar ferramentas autorizadas para buscar arquivos, executar ações, verificar os resultados e continuar trabalhando até atingir um objetivo, entramos no universo dos agentes.
>
> Agente não é simplesmente um nome bonito pra um prompt longo. A diferença está no processo e nas ferramentas. Dependendo de como foi configurado, ele pode receber um objetivo, planejar uma sequência, executar uma ação, observar o que aconteceu e decidir se precisa corrigir alguma coisa ou pedir sua ajuda.
>
> Imagina uma equipe organizando um evento científico. Uma pessoa recebe a missão de preparar a programação. Ela consulta os dados disponíveis, faz uma primeira proposta, percebe que falta o horário de uma palestra, pergunta ao responsável e revisa. Não é porque ela recebeu a missão que ganhou autorização para decidir tudo sozinha. Com um agente, a lógica de trabalhar por etapas também precisa de limites e pontos de aprovação.
>
> Esse ciclo é chamado muitas vezes de ciclo agêntico: observar, planejar, agir e verificar. Em ferramentas mais avançadas, pode repetir várias vezes. Mas repetição automática não é garantia de qualidade. Se o objetivo está mal definido ou se o acesso está amplo demais, ele pode trabalhar rápido na direção errada.
>
> Pra quem está começando, a consequência prática é simples: não basta perguntar 'o que a IA consegue fazer?'. Pergunte também 'o que eu quero delegar?', 'com quais informações?', 'que ferramentas ela vai usar?' e 'quem vai aprovar?'.
>
> E não precisa criar agente hoje. Primeiro você entende o mecanismo. Depois a gente vai aprender a montar fluxos cada vez mais completos, com ChatGPT, Claude e outras opções.

## 06 — DOCUMENTAÇÃO OFICIAL E A IMPORTÂNCIA DE APRENDER A APRENDER | 14:30–17:10

**PRODUÇÃO:** TELA: abrir docs/help oficiais em aba de exemplo. Não citar caminhos de interface que possam ter mudado sem checagem. Links no material de apoio.

**FALAS PARA TELEPROMPTER:**

> Uma coisa que eu quero te ensinar desde o primeiro vídeo é a não depender de um tutorial pra cada mudança de botão. Essas plataformas evoluem o tempo inteiro. Um recurso que hoje está num lugar, amanhã pode mudar de nome, de plano ou até de funcionamento.
>
> Por isso, além de assistir a aulas como esta, vale aprender a consultar a documentação oficial. O ChatGPT tem páginas de ajuda explicando projetos, ferramentas e arquivos. O Claude também tem documentação para o aplicativo e para o Claude Code. E existem materiais oficiais sobre agentes e integrações.
>
> Vou abrir aqui uma página de ajuda. Repara como eu procuro primeiro o nome da função e depois vejo pra que ela serve, quais são os pré-requisitos, os limites e as opções de segurança. Eu não preciso ler toda a documentação de uma vez. Eu preciso saber onde procurar quando surgir uma dúvida real.
>
> Isso é muito melhor do que ficar colecionando cinquenta comandos que você nunca testou. Minha sugestão é ter uma pequena biblioteca pessoal: links oficiais, nomes dos recursos que você já experimentou, exemplos de prompts que funcionaram e observações sobre o que precisou corrigir.
>
> No nosso projeto eu preparei um glossário exatamente pra isso. Um termo de cada vez, com exemplos que façam sentido pra quem vive a rotina da saúde. Mas nenhuma definição deve virar uma verdade imutável: quando falamos de botões, permissões e planos, precisamos conferir a versão atual.
>
> E agora que você já entende o que é modelo, contexto e agente, fica muito mais fácil compreender outras palavras que aparecem em vídeos e nas telas dessas ferramentas.

## 07 — PROJETOS, SKILLS, CONECTORES, PLUGINS E MCP | 17:10–22:15

**PRODUÇÃO:** SLIDES: analogias visuais em cinco cards com conceitos distintos, sem afirmar equivalência entre plataformas. Inserir aviso de disponibilidade por conta e plano.

**FALAS PARA TELEPROMPTER:**

> Vamos organizar cinco conceitos que você provavelmente vai ouvir bastante daqui pra frente: projeto, Skill, conector, plugin e MCP. Parece muita coisa, mas vamos fazer com calma.
>
> Projeto, dentro de um aplicativo de IA, é uma forma de reunir conversas, arquivos e instruções em torno de um assunto. Pense numa pasta de trabalho bem organizada. Se você vai desenvolver um curso, por exemplo, faz sentido ter um lugar com as referências, os objetivos, o público e o histórico daquele curso. No ChatGPT existem recursos de projetos; outros aplicativos podem organizar o contexto de formas diferentes.
>
> Skill, ou habilidade, é um conjunto de instruções reutilizáveis que ensina um agente a executar um tipo de tarefa seguindo um método. Em vez de explicar toda vez como estruturar um roteiro de aula, por exemplo, você pode ter instruções sobre linguagem, duração, capítulos, critérios de revisão e formato de entrega. O agente pode recorrer a essas instruções quando o ambiente oferecer suporte.
>
> Conector é o recurso que dá acesso a uma fonte ou a um serviço externo, dentro das permissões concedidas. A diferença entre pedir 'resuma meus arquivos' e conseguir realmente localizar um arquivo de um Drive conectado é enorme. Sem esse acesso, a IA não deveria fingir que abriu nada.
>
> Plugin é uma forma de reunir capacidades e fluxos de trabalho. Dependendo da plataforma, pode combinar habilidades e integrações. Ele não é sinônimo universal de agente e não deve receber permissões irrestritas só porque parece útil.
>
> E MCP é a sigla de um protocolo que ajuda ferramentas de IA a conversar com serviços e fontes externas de maneira padronizada. Não precisa memorizar o nome completo agora. O que importa é entender a ideia: ele facilita uma ponte entre a IA e algo que está fora da conversa, quando essa conexão é configurada e autorizada.
>
> Talvez você esteja pensando: preciso aprender tudo isso antes de conseguir usar a IA? Não. A aula de hoje é um mapa. Eu quero que, quando você ouvir alguém dizer 'instala essa Skill', 'conecta esse serviço' ou 'cria um agente', você saiba pelo menos qual é a função de cada peça.
>
> E olha como as coisas se conectam. Você pode ter um projeto com contexto, uma habilidade que estabelece o método de trabalho, uma ferramenta que executa ações e um conector que acessa uma fonte autorizada. Esse conjunto permite ir além de uma conversa isolada. Mas ele só é útil se a pessoa souber qual problema quer resolver.

## 08 — PRIMEIRA DEMONSTRAÇÃO — DE UM PEDIDO A UM PROTÓTIPO | 22:15–27:30

**PRODUÇÃO:** CÂMERA → GRAVAÇÃO DE TELA. Mostrar passo a passo e o prompt 01 completo em painel expandível. Escolher ChatGPT ou Claude, conforme função disponível, em conversa nova.

**FALAS PARA TELEPROMPTER:**

> Chegou a parte prática. Em vez de pedir uma tabela ou só um texto, eu vou tentar construir uma coisa que a gente consiga abrir no navegador. É um protótipo, não é um sistema de verdade. A ideia é você perceber que dá pra começar com um objetivo, explicar os requisitos e ver a ferramenta produzir uma primeira versão.
>
> Vou criar um painel demonstrativo de gestão, com dados totalmente fictícios. Nele eu quero três indicadores, uma lista de atividades, botões que mudam o status e um filtro pra mostrar as pendências. O valor aqui não é ter números bonitos; é ver uma interface respondendo ao que a gente faz.
>
> Eu vou abrir uma conversa nova. Você pode usar ChatGPT ou Claude; o caminho de geração de arquivos e visualização depende do plano e dos recursos disponíveis na sua conta. Não vou prometer que a tela de todo mundo vai ser igual.
>
> Olha como eu vou estruturar o pedido. Primeiro digo quem é o público: gestores e coordenadores que nunca programaram. Depois descrevo exatamente o que quero construir: uma página chamada Painel de Gestão. Em seguida defino os elementos que precisam aparecer e, tão importante quanto isso, os limites do protótipo.
>
> Repara nesse detalhe: eu digo que os dados são fictícios, que não deve haver login, banco de dados nem integração com sistemas externos e que qualquer alteração de status vale só enquanto a página estiver aberta. Isso impede que a gente confunda uma demonstração visual com um produto pronto para trabalhar com dados da instituição.
>
> Eu peço também que a ferramenta entregue um único arquivo HTML com o visual e as interações. HTML é um formato de arquivo usado para estruturar páginas web. Você não precisa se tornar programador pra fazer esse primeiro teste, mas é importante saber que por trás do resultado existe código que pode precisar de revisão.
>
> Agora eu vou colar o prompt completo que deixei no material de apoio e enviar. [PAUSA: MOSTRAR O PEDIDO E A RESPOSTA REAL.]
>
> Se o seu aplicativo tiver a opção de gerar ou visualizar arquivos, aproveite esse caminho. Se ele mostrar apenas um bloco de código, eu vou demonstrar como copiar tudo, salvar como um arquivo com final .html e abrir no navegador. Na hora de salvar no Windows, a gente precisa escolher o tipo de arquivo correto pra ele não virar painel.html.txt.
>
> Perceba a diferença para aquela nossa conversa do começo. Eu não estou só pedindo uma explicação sobre painéis. Eu estou descrevendo um resultado que eu quero testar.

## 09 — TESTE DE VERDADE — FUNCIONA OU SÓ PARECE FUNCIONAR? | 27:30–32:20

**PRODUÇÃO:** CAPTURA: abrir prévia/arquivo, clicar nos filtros e completar atividade. Mostrar possíveis erros reais. Se não funcionar, usar Prompt 02. Não simular execução ou integração.

**FALAS PARA TELEPROMPTER:**

> Agora vem a parte que eu mais gosto: testar. Não adianta a IA dizer 'terminei' se o resultado não faz o que foi combinado. Vamos abrir esse protótipo e olhar como alguém que vai usar a tela.
>
> Primeiro, os indicadores aparecem? Eles estão marcados como fictícios? A página fica legível? Depois eu vou clicar numa atividade e marcar como concluída. O botão realmente muda o status? E quando eu seleciono o filtro de pendentes, aquela atividade some da lista de pendências? Esse é o tipo de verificação que faz parte do uso profissional da IA.
>
> Se algum botão não funcionar, eu não preciso começar tudo de novo. Posso voltar à conversa e explicar o erro: 'Quando clico no filtro, nada acontece. Corrija isso sem mudar o restante da aparência'. Quanto mais específica for a descrição do problema, mais fácil fica orientar a próxima tentativa.
>
> Também preciso conferir algo que quase sempre passa despercebido: a IA não criou uma base de dados real, não se conectou a um sistema hospitalar e não começou a registrar as informações oficiais da instituição. Se eu atualizar a página e perder o status, isso era esperado porque eu pedi um protótipo sem armazenamento.
>
> Vou fazer agora um segundo pedido de revisão. Quero que a ferramenta confira botões, filtros, legibilidade e os avisos sobre limites. Se ela encontrar problemas, deve entregar uma versão completa corrigida. [PAUSA: COLAR O PROMPT DE REVISÃO E TESTAR A SAÍDA.]
>
> Isso que a gente está fazendo é um ciclo: objetivo, proposta, teste, feedback e correção. É uma versão simples daquele raciocínio agêntico que comentei antes, mas aqui eu estou conduzindo as etapas pessoalmente. Não estamos executando um agente autônomo, e essa distinção importa.
>
> Observe também que um protótipo bonito não vira automaticamente uma solução segura. Se um dia essa ideia fosse usada de verdade numa clínica ou num hospital, precisaríamos discutir segurança, acessibilidade, armazenamento, autorização, manutenção e integração com as ferramentas oficiais.
>
> Mas pra quem nunca imaginou criar uma página interativa, já é uma mudança de perspectiva. A IA pode ajudar você a passar de uma ideia descrita em português para uma primeira versão que dá pra abrir e testar.

## 10 — POR QUE ALGUNS RESULTADOS FICAM RUINS? CONTEXTO E ITERAÇÃO | 32:20–35:20

**PRODUÇÃO:** SLIDE: prompt vago vs pedido com objetivo, público, conteúdo, formato, limites e teste. Opcional mostrar um antes/depois extra na tela.

**FALAS PARA TELEPROMPTER:**

> Talvez o seu primeiro resultado não fique tão bom. E isso não significa que você não sabe usar IA. Significa que a gente precisa aprender a conversar com a ferramenta de um jeito que dê direção.
>
> Compara duas solicitações. A primeira: 'crie um painel bonito'. O que é bonito? Que painel? Pra quem? Com quais dados? Com que finalidade? O modelo tem que preencher um monte de lacunas, e ele pode inventar detalhes que não fazem sentido.
>
> Agora olha o pedido que fizemos. Ele descreve o público, o objetivo, os elementos da interface, os números fictícios, os botões, as restrições técnicas e os cuidados que precisam aparecer. Isso não garante um resultado perfeito, mas nos dá critérios pra avaliar se a entrega está correta.
>
> Um bom pedido não precisa ser gigantesco. Ele precisa ter as informações que fazem diferença. Às vezes, pra uma tarefa simples, duas frases resolvem. Pra criar uma interface com várias interações, vale especificar mais.
>
> Também não quero que você ache que existe uma frase mágica que funciona em qualquer ferramenta pra qualquer objetivo. O que funciona é o raciocínio: definir o que quer, dar contexto, explicar o formato, estabelecer limites, testar e revisar.
>
> E a revisão não é um detalhe depois do trabalho. Ela faz parte do trabalho. Em saúde isso é ainda mais importante. Sempre que o assunto envolver conduta, paciente, protocolo, prazo regulatório ou informação sigilosa, precisa haver fontes, autorização e responsabilidade humana.
>
> Quanto mais você pratica esse ciclo, mais deixa de ser alguém que apenas consome respostas e começa a conduzir a IA pra resolver problemas que você realmente escolheu resolver.

## 11 — QUANDO USAR CHATGPT, CLAUDE E FERRAMENTAS MAIS AVANÇADAS | 35:20–38:10

**PRODUÇÃO:** SLIDE comparativo de capacidades por classe de ferramenta sem rankings absolutistas ou alegar que features existem em todo plano. Mostrar páginas de documentação oficiais.

**FALAS PARA TELEPROMPTER:**

> Agora, uma pergunta que eu sei que vai aparecer: Rosa, afinal, eu preciso aprender ChatGPT ou Claude? E a resposta é que você precisa entender primeiro o tipo de trabalho que quer fazer. Não faz sentido escolher uma ferramenta só porque alguém disse que ela é a melhor.
>
> ChatGPT e Claude têm interfaces de conversa e recursos que podem ajudar com escrita, análise, arquivos e outros tipos de tarefa. Os detalhes mudam com o tempo, com os planos e com as permissões. O que eu ensino aqui é o raciocínio que você consegue transportar de um lugar para outro.
>
> Se a sua necessidade é organizar um estudo, elaborar perguntas ou construir uma primeira proposta, um aplicativo de conversa com bons recursos pode ser suficiente. Se você precisa que a IA trabalhe com arquivos de projeto, altere código, execute tarefas em ferramentas conectadas e verifique resultados, entram os ambientes e agentes que oferecem essas capacidades.
>
> Claude Code, por exemplo, é uma ferramenta voltada para trabalho com projetos e código, com recursos de agentes, contexto e ações autorizadas. O ChatGPT também possui diferentes caminhos de trabalho, conforme o recurso disponível. Isso não quer dizer que você precisa aprender programação antes de começar, nem que essas ferramentas sejam idênticas.
>
> Nas próximas aulas eu vou separar o que é o fundamento e o que é o uso da plataforma. Assim você aprende o que cada uma pode oferecer e faz suas próprias escolhas, sem depender de uma única marca.
>
> E quero te convidar a começar pequeno. Aprender IA não é acumular assinaturas. É experimentar com segurança, medir se ajudou de verdade e aprofundar os recursos quando existir uma necessidade concreta.

## 12 — REVISÃO FINAL E PRÓXIMA AULA | 38:10–40:20

**PRODUÇÃO:** CÂMERA + SLIDE final com cinco conceitos e QR/link do glossário. Fecho no logo.

**FALAS PARA TELEPROMPTER:**

> Se você chegou até aqui, percebeu que a inteligência artificial é muito mais do que um chat que responde perguntas. A gente falou de modelo, de aplicativo, de contexto, de ferramentas e de agentes. E viu uma ideia sair do texto e ganhar forma como um protótipo que pode ser testado.
>
> Você não precisa dominar essas cinco coisas de uma vez. Quero que guarde o principal: a ferramenta não conhece automaticamente a sua realidade, não tem acesso a tudo que existe no seu computador e não deve ser tratada como dona da decisão. Ela pode ajudar a construir, mas você precisa orientar, conferir e entender os limites.
>
> Agora eu tenho um exercício pra você. Pensa em uma ideia pequena, que você gostaria de ver ganhar forma: uma página educativa, um checklist de estudos, um organizador de tarefas fictícias ou um quadro interativo. Descreve o resultado, coloca critérios claros e pede uma primeira versão. Depois testa e anota o que foi necessário corrigir.
>
> O prompt do painel, o segundo prompt de revisão e um mapa dos conceitos dessa aula estão disponíveis no material gratuito. Também deixei os links da documentação e do Glossário Estrateg[IA] pra você estudar no seu ritmo.
>
> Na próxima aula, vamos entrar no ChatGPT desde o começo: o que aparece na interface, como organizar uma conversa, como trabalhar com o contexto e quais cuidados tomar antes de enviar qualquer arquivo. Depois vamos evoluir pra projetos, outras ferramentas e agentes.
>
> Se essa aula te ajudou a enxergar o que dá pra construir com IA, compartilha com alguém que também está começando. E me conta nos comentários: você quer aprender a criar o quê primeiro?
>
> Eu sou Rosa Kethllyn, e esse é o Estrateg[IA]. A gente se vê na próxima aula.

---

## PROMPT 01 — CRIAÇÃO DO PROTÓTIPO (COPIAR, NÃO LER INTEGRALMENTE)

```text
Quero que você atue como uma pessoa desenvolvedora de interfaces educacionais e me ajude a CRIAR um protótipo interativo, sem usar dados reais.

PROJETO: Painel demonstrativo de uma instituição de saúde fictícia, chamado “Painel de Gestão”.
PÚBLICO: coordenadores e gestores da saúde que nunca programaram.

REQUISITOS:
1. Entregue UM arquivo HTML completo, com CSS e JavaScript dentro do próprio arquivo, sem bibliotecas ou links externos.
2. Visual claro e profissional: fundo branco, texto quase preto, cor laranja #F23C00 para destaques, fonte de sistema e espaços de respiro.
3. Mostre três indicadores DIDÁTICOS E FICTÍCIOS: treinamentos concluídos 72%, atividades planejadas 18 e pendências 5. Informe visivelmente que são dados de demonstração.
4. Adicione uma lista de quatro atividades fictícias, cada uma com título, responsável “A definir”, status e um botão para marcar visualmente como concluída.
5. Adicione filtro para exibir todas, pendentes ou concluídas.
6. Crie um pequeno quadro “O que revisar antes de usar em uma instituição”, com alerta sobre dados, validação humana e necessidade de integração segura.
7. A interface deve funcionar em celular e computador.
8. Inclua comentários no código explicando de forma simples as partes principais.

IMPORTANTE:
- Não use servidores, banco de dados, login, APIs ou envio de dados.
- Não afirme que o protótipo já está conectado a qualquer sistema hospitalar.
- Ao atualizar o status, deixe claro que a mudança acontece só na página aberta e não é salva.
- Se a plataforma permitir gerar um arquivo, forneça o HTML. Se não, apresente o código completo em um único bloco ```html para que eu possa copiar e salvar como painel.html.

Antes de começar o código, resuma em 4 linhas o que você vai construir.
```

## PROMPT 02 — REVISÃO DO PROTÓTIPO

```text
Revise o protótipo HTML que você acabou de criar.
1. Verifique se todos os botões realmente funcionam e se o filtro separa corretamente atividades pendentes e concluídas.
2. Confira se nenhum dado fictício foi apresentado como indicador real.
3. Confira acessibilidade básica: contraste, rótulos dos botões, foco de teclado e leitura em celular.
4. Se houver problemas, entregue o HTML COMPLETO corrigido, preservando a aparência.
5. Explique em linguagem simples o que você corrigiu e quais limitações permanecem: sem banco de dados, sem login, sem dados reais e sem integração com sistemas.
```

## ROTEIRO DE TELA

1. Criar conversa nova no ChatGPT ou Claude, sem dados ou notificações privadas.
2. Mostrar em tela os blocos do prompt 01: objetivo, público, interface, interatividade e limites.
3. Enviar o prompt. Se a ferramenta apresentar o HTML em arquivo ou prévia, abrir; caso contrário, copiar o código completo para um editor de texto e salvar **painel.html** (no Windows, selecionar todos os arquivos, não .txt).
4. Abrir a página gerada no navegador e testar os três indicadores fictícios, os quatro cards, os botões e os filtros. Nenhuma integração real foi solicitada.
5. Se necessário, descrever falhas de maneira específica e colar o prompt 02. Comparar versões.
6. Esclarecer que HTML local e dados de demonstração não equivalem a sistema de produção, tampouco conferem acesso automático a arquivos ou registros reais.

## LÂMINAS HTML — MAPA EDITORIAL

01 Capa • 02 Por que IA é maior que um chat • 03 Quem sou eu • 04 Modelo × aplicativo × ferramentas • 05 Tokens e contexto • 06 Chatbot × agente • 07 Loop agêntico • 08 Onde aprender: documentação oficial • 09 Projetos, Skills e conectores • 10 Ponte MCP e plugins • 11 Da ideia ao protótipo • 12 O pedido certo • 13 Teste no navegador • 14 Antes de usar de verdade • 15 Exercício e próximo episódio.

**Estilo:** Funnel Display nos títulos, Poppins no corpo, laranja #F23C00, preto #1A1A1B, branco e cinzas da marca. Usar esquemas, ícones e revelações progressivas; evitar slides lotados de texto.

## LINKS PARA CONSULTAR ANTES DA GRAVAÇÃO

- ChatGPT Projetos: https://help.openai.com/pt-br/articles/10169521-projects-in-chatgpt
- Aplicativos e ferramentas ChatGPT: https://help.openai.com/pt-br/articles/11487775-connected-apps-in-chatgpt
- Claude Code Desktop: https://code.claude.com/docs/pt/desktop
- Glossário Estrateg[IA]: https://rosakethllyn-blip.github.io/modo-ia-saude-glossario/

## REVISÃO PRÉ-GRAVAÇÃO

- [ ] Ensaiar as falas, definir pausas e ajustar o ritmo para sua voz.
- [ ] Confirmar interface e recurso de criação de HTML na conta que será gravada.
- [ ] Testar os prompts antes do dia de filmagem e refazer se necessário.
- [ ] Verificar o arquivo no computador sem expor dados pessoais.
- [ ] Gravar tela real e conferir todos os cliques.
- [ ] Mostrar o protótipo como demonstração, nunca como sistema institucional.
