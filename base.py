from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_text():
    text = request.json["text"]
    text = text.lower()
    text = " ".join(text.splitlines())
    result = ""
    i = 'a'
    j = "a"

    ##############################
    #### DESPACHOS E DECISÕES ####
    ##############################

    # GRATUIDADE DE JUSTIÇA - CONCESSÃO
    ## Parte Autora
    GJCA = ["*gj.a", "*gratuidade de justiça autor", "*justiça gratuita autor"]
    if any(word in text for word in GJCA):
        result += f"{i}) Uma vez que comprovada a insuficiência de recursos para a realização do pagamento das custas, despesas processuais e honorários advocatícios, concedo à parte autora o benefício da Gratuidade da Justiça, nos termos e sob as penas do art. 98 e seguintes do Código de Processo Civil.\nAnote-se nos autos, evitando-se cobranças indevidas.\n"
        i = chr(ord(i) + 1)

    ## Parte Ré
    GJCR = ["*gj.r", "*gratuidade de justiça réu", "*justiça gratuita réu"]
    if any(word in text for word in GJCR):
        result += f"{i}) Uma vez que comprovada a insuficiência de recursos para a realização do pagamento das custas, despesas processuais e honorários advocatícios, concedo à parte ré o benefício da Gratuidade da Justiça, nos termos e sob as penas do art. 98 e seguintes do Código de Processo Civil.\nAnote-se nos autos, evitando-se cobranças indevidas.\n"
        i = chr(ord(i) + 1)

    # DESPACHO INICIAL - PROCEDIMENTO COMUM
    CITESEPC = ["*cite-se.pc", "*cite-se procedimento comum"]
    if any(word in text for word in CITESEPC):
        result += f"{i}) Conforme dados estatísticos repassados pelo Coordenador do CEJUSC – Londrina, no ano de 2019 foram agendadas 7.439 sessões de conciliação/mediação das dez varas cíveis desta Comarca, sendo realizadas apenas 5.873, ou seja, a taxa de cancelamento foi de 21% e, ainda, do total, apenas 438 acordos foram formalizados, obtendo-se grau de êxito inferior a 6%.\nCom isso, a experiência vem demonstrando que, a despeito dos esforços do Poder Judiciário, com a implantação do CEJUSC, capacitação de servidores e destinação de espaço e estrutura adequadas para o desempenho de sua vocação, os índices de conciliação são inexpressivos no cível.\nA constatação é ainda mais desoladora quando instituições financeiras, seguradoras e concessionárias de telefonia figuram em qualquer dos polos da relação processual, quer por gestão de risco, estratégia de ação ou defesa, ou pelo emprego de correspondentes sem alçada para transigir em qualquer quantia ou condição.\nOutras causas, por sua natureza, inviabilizam até a realização do ato, a exemplo da usucapião e ações possessórias com litisconsórcio, não raro, indeterminável em seu primeiro momento (confinantes e proprietários registrais e/ou sucessores, composses ou esbulho multitudinário).\nA fase do art. 334 do Código de Processo Civil em processos com parte(s) domiciliada(s) em comarca(s) diversa(s), por igual, atua unicamente para retardar o fluxo do procedimento, na medida em que sequer para prestar depoimento pessoal (que é ato impositivo) o interessado é obrigado a deslocar-se à sede do juízo em que tramita o feito, menos ainda para ato conciliatório que exige, sobretudo, sua vontade em transigir.\nAlém disso, inúmeros são os casos em que frustrada a primeira citação, desdobram-se diligências voltadas à localização do réu, derivando, em cada tentativa fracassada, a obstrução da pauta do CEJUSC e o fatal embaraço da solução definitiva de conflitos de maiúscula relevância social, a exemplo daqueles onde se discute a preservação de bens e direitos de crianças, idosos, enfermos e incapazes.\nÀ vista de todas essas circunstâncias concretas, considero essencial o descongestionamento do CEJUSC, de sorte a liberar sua pauta às ações com efetivo potencial conciliatório, e/ou cuja salvaguarda de bem jurídico indisponível demande a tempestiva aproximação das partes em busca de solução eficaz da demanda já deduzida.\nNada impede, porém, que, postulando as partes pela designação do ato, seja o feito, então, encaminhado ao CEJUSC em qualquer fase do procedimento, observado prévio contraditório em respeito ao princípio da voluntariedade da transação.\nVale lembrar, ainda, que desafiando o feito a instrução processual, impõe o art. 359 do CPC que, na abertura da audiência, busque o juiz conciliar as partes, derribando, assim, qualquer ideia de que a não realização do ato previsto no art. 334 subtraiu dos litigantes a chance da autocomposição.\nA inclusão de feitos indiscriminados e às cegas na fase do art. 334 do Código de Processo Civil coopera apenas para transgredir a garantia da razoável duração do processo (o ato precisa ser designado, em média, com antecedência de 60-90 dias, para que haja tempo dos Correios ou Oficial de Justiça cumprirem a diligência com a antecedência mínima de 20 dias úteis prevista no art. 334), promover o uso irracional e ineficiente de mecanismo processual de imensurável valor, entravando a célere solução de conflitos com potencial conciliatório, em favor daqueles que estatisticamente já demonstraram nenhum pendor ou viabilidade para o acordo.\nAssim, deixo de designar a audiência contemplada pelo art. 334 do Código de Processo Civil e, por consequência, determino a citação da parte ré para que apresente resposta ao pedido em 15 (quinze) dias úteis, cujo termo inicial ocorrerá na forma do art. 335, III, contado nos termos do art. 231, do CPC. \nIntimem-se.\nDiligências necessárias.\n"
        i = chr(ord(i) + 1)

    # DESPACHO INICIAL - EXIGIR CONTAS
    CITESEEC = ["*cite-se.ec", "*cite-se exigir contas"]
    if any(word in text for word in CITESEEC):
        result += f"{i}) Cite-se a parte ré para que preste as contas solicitadas, na forma adequada (com especificação das receitas, aplicação das despesas e investimentos e apresentação do saldo – art. 551 do CPC) ou oferte contestação, ambos no prazo de 15 (quinze) dias cotados da juntada da carta/mandado de citação, sob pena de prosseguimento do processo em sua segunda fase, nos termos do art. 550, § 4º do Código de Processo Civil.\n"
        i = chr(ord(i) + 1)

    ###################
    #### SENTENÇAs ####
    ###################

    # 1. RELATÓRIO

    # 1.1. PETIÇÕES INICIAIS

    # 1.1.1. FATOS e FUNDAMENTOS

    # 1.1.1.2. ADVOGADOS GENÉRICOS

    # PETIÇÃO INICIAL + CONTESTAÇÃO (entre a inicial e a contestação)

    PI = ["ex positis", "digne Vossa Excelência receber a presente", ", vem perante vossa excelência propor"]
    CON = ["apresentar contestação, pelas razões de fato e de direito",
           "requer seja acolhida a preliminar arguida, extinguindo-se o presente feito sem resolução de mérito",
           "requer que a presente ação seja julgada totalmente improcedente"]
    if any(word in text for word in PI) and any(word in text for word in CON):
        result += "\nI - Relatório\nA parte autora, qualificada na petição inicial, ajuizou a presente AÇÃO DE XXXXXXX, contra a parte ré, igualmente qualificada na inicial, arguindo em resenha que:\n"

    # GRATUIDADE DE JUSTIÇA REQUERIDA PELO AUTOR
    GJ = ["requer a concessão dos benefícios da assistência judiciária gratuita",
          "requer a concessão dos benefícios da assistência judiciária",
          "não possui condições de arcar com às custas processuais",
          "não possuir condições de arcar com às custas processuais e honorários, sem prejuízo próprio ou de sua família",
          "não possuem condições de arcar com os custos do processo e os honorários advocatícios",
          "inviável o custeio das despesas processuais e o pagamento dos honorários",
          "requerer a concessão da assistência judiciária gratuita",
          "requer a concessão da assistência judiciária gratuita"]
    if any(word in text for word in GJ):
        result += f"{i}) não possui condições de arcar com as despesas do processo, motivo pelo qual lhe deve ser concedido o benefício da assistência judiciária gratuita;\n"
        i = chr(ord(i) + 1)

    # PRIORIDADE DE TRAMITAÇÃO REQUERIDA PELO AUTOR - IDOSO
    PRIOTRAM = ["requer seja concedido prioridade processual na tramitação dos autos",
                "possui mais de 60 anos de idade"]
    if any(word in text for word in PRIOTRAM):
        result += f"{i}) possui mais de 60 anos de idade e, por isso, lhe deve ser concedido o benefício da prioridade de tramitação;\n"
        i = chr(ord(i) + 1)

    # AUTOR MANIFESTA DESINTERESSE NA REALIZAÇÃO DA AUDIÊNCIA DE CONCILIAÇÃO
    DESINTCONCI = ["opta pela não realização de audiência conciliatória", "não possui interesse na realização de acordo"]
    if any(word in text for word in DESINTCONCI):
        result += f"{i}) não possui interesse na realização da audiência de conciliação;\n"
        i = chr(ord(i) + 1)

    # 1.1.1.3. ADVOGADOS ESPECÍFICOS

    # THIAGO CARDOSO RAMOS 1
    THICR1 = ["celebrou com o requerido, o contrato pessoal",
              "abusando da necessidade da parte autora, aplicou juros exorbitantes"]
    if any(word in text for word in THICR1):
        result += f"{i}) celebrou contrato de empréstimo com o banco réu para pagamento parcelado, mas foram aplicados juros excessivos;\n"
        i = chr(ord(i) + 1)

    # THIAGO CARDOSO RAMOS 2
    THICR2 = ["uma vez caracterizada a abusividade da cobrança dos juros remuneratórios, necessário se faz sua revisão para adequá-los à média do mercado",
        "requer sejam fixados os juros de acordo com a menor taxa média de mercado, conforme vem decidindo os nossos tribunais pátrios.",
        "evidente que a taxa efetivamente cobrada não é mais vantajosa ao demandante, logo é de se aplicar a taxa média de mercado"]
    if any(word in text for word in THICR2):
        result += f"{i}) diante dos juros abusivos cobrados, o valor do empréstimo deve ser recalculado, limitando os juros à taxa média de mercado estabelecida pelo Banco Central do Brasil;\n"
        i = chr(ord(i) + 1)

    #  THIAGO CARDOSO RAMOS 3
    THICR3 = ["desproporção entre o que poderia ter sido cobrado com o que efetivamente o foi",
              "evidencia a quebra da boa-fé objetiva que deve vigorar entre as partes contratantes"]
    if any(word in text for word in THICR3):
        result += f"{i}) a ré deve ser condenada ao pagamento dos danos materiais sofridos consistente na diferença entre o que foi cobrado e aquilo que é realmente devido;\n"
        i = chr(ord(i) + 1)

    #  THIAGO CARDOSO RAMOS 4
    THICR4 = ["os danos morais, que devem punir moderadamente o causador do ilícito",
              "o dano moral em ações desse jaez deve cumprir não só o caráter reparatório como também o pedagógico"]
    if any(word in text for word in THICR4):
        result += f"{i}) a cobrança abusiva realizada pelo réu causou danos morais, os quais devem ser indenizados;\n"
        i = chr(ord(i) + 1)

    #  THIAGO CARDOSO RAMOS 5
    THICR5 = ["faz jus à facilitação da defesa de seus interesses em juízo mediante a inversão do ônus da prova",
              "requer seja deferida a inversão do ônus da prova, conforme mencionado alhures, de modo que o requerido, na qualidade de fornecedor de serviços, demonstrar que não houve falha na prestação de serviços e traga aos autos o instrumento contratual"]
    if any(word in text for word in THICR5):
        result += f"{i}) incide ao caso as normas e proteções do Código de Defesa do Consumidor, com aplicação da inversão do ônus da prova, ante a verossimilhança das alegações e sua hipossuficiência;\n"
        i = chr(ord(i) + 1)

        #  THIAGO CARDOSO RAMOS 6
    THICR6 = [
        "verba honorária deve ser fixada em quantia certa e determinada, que recompense dignamente o trabalho realizado pelo advogado"]
    if any(word in text for word in THICR6):
        result += f"{i}) a verba honorária deve ser fixada em quantia certa e determinada, que recompense dignamente o trabalho realizado pelo advogado;\n"
        i = chr(ord(i) + 1)

    # 1.1.2. PEDIDOS

    # Parte INICIAL dos Pedidos
    PEDIDOS = ["– dos pedidos", "digne vossa excelência receber a presente"]
    if any(word in text for word in PEDIDOS):
        result += "Pugnou pela "

        #  THIAGO CARDOSO RAMOS PEDIDOS 1
        THICRP1 = ["descapitalização a ser aplicada ao empréstimo realizado entre as parte no patamar"]
        if any(word in text for word in THICRP1):
            result += "descapitalização dos juros; "

        #  THIAGO CARDOSO RAMOS PEDIDOS 2
        THICRP2 = ["ano, conforme taxa média de mercado determinado pelo banco central"]
        if any(word in text for word in THICRP2):
            result += "redução dos juros conforme taxa média de mercado determinada pelo Banco Central; "

        #  THIAGO CARDOSO RAMOS PEDIDOS 3
        THICRP3 = ["), o qual deverá ser pago pela parte requerida de forma dobrada"]
        if any(word in text for word in THICRP3):
            result += "restituição dobrada dos valores indevidamente cobrados; "

        #  THIAGO CARDOSO RAMOS PEDIDOS 4
        THICRP4 = ["condenar ainda o réu a indenizar a título de danos morais a parte autora"]
        if any(word in text for word in THICRP4):
            result += "condenação da ré ao pagamento de indenização pelos danos morais sofridos; "

        # Parte FINAL dos Pedidos
        if any(word in text for word in PEDIDOS):
            result += "além da condenação da parte ré ao pagamento das custas, despesas processuais e honorários advocatícios.\n"

        VLRCS = ["dá-se à causa", "dá-se a causa"]
        if any(word in text for word in VLRCS):
            result += "Atribuiu à causa o valor de R$00.000,00."
        else:
            result += "\n***OBS.: NÃO IDENTIFIQUEI ATRIBUIÇÃO AO VALOR DA CAUSA!!!!!"

    # PETIÇÃO INICIAL + CONTESTAÇÃO (entre a inicial e a contestação)

    if any(word in text for word in PI) and any(word in text for word in CON):
        result += "\nA petição inicial foi recebida, determinado-se a citação.\nA parte ré apresentou contestação, arguindo em resenha que:\n"

    # 1.2. CONTESTAÇÕES

    # 1.2.3. PRELIMINARES

    # 1.2.3.1. ADVOGADOS GENÉRICOS

    # IF CONTESTAÇÃO
    # CONTESTACAO = ["apresentar contestação, pelas razões de fato"]
    # if any(word in text for word in CONTESTACAO):
    #    result += "\nCONTESTAÇÃO:\n"

    #  CONEXÃO
    CONEXAO = ["reputam-se conexas duas ou mais ações quando lhes for comum o objeto ou a causa de pedir",
               "tem como objetivo evitar a prolação de decisões contraditórias", "o autor ajuizou ações idênticas",
               "deve ser determinada a reunião dos processos, conforme dispõe o artigo 55, § 1º"]
    if any(word in text for word in CONEXAO):
        result += f"{j}) há conexão e, por isso, os processos devem ser reunidos para julgamento conjunto;\n"
        j = chr(ord(j) + 1)

    #  IMPUGNAÇÃO À GRATUIDADE DE JUSTIÇA

    IMPUGGJ = ["fatores esses que afastam a presunção necessária ao deferimento da justiça gratuita",
               "a parte autora contratou advogado particular para demandar esse processo",
               "necessário que o Juízo a quo intime a parte autora para fazer prova da sua não condição de arcar com as custas processuais"]
    if any(word in text for word in IMPUGGJ):
        result += f"{j}) as circunstâncias do processo afastam a presunção necessária ao deferimento da justiça gratuita e, por isso, a parte autora deve ser intimada para fazer prova de sua condição;\n"
        j = chr(ord(j) + 1)

    # 1.2.3.2. ADVOGADOS ESPECÍFICOS

    #  Kuster Machado - CREFISA - Impossibilidade Perícia na Fase de Conhecimento

    IRPCFC = ["da impossibilidade de realização de perícia contábil em fase de conhecimento",
              "a parte autora pleiteie a realização de perícia contábil, o pedido de tal prova resta desde já impugnado",
              " a realização desta perícia na fase de conhecimento é totalmente descabida, pois pouco produtiva e em nada irá auxiliar o magistrado em sua decisão",
              "a perícia, com a finalidade de se apurar o valor devido, somente deve/pode ser realizada em eventual fase de cumprimento de sentença"]
    if any(word in text for word in IRPCFC):
        result += f"{j}) é descabida a realização de perícia contábil na fase de conhecimento, visto que o perito não tem uma base de cálculo para revisar o contrato, podendo ser produzida apenas na fase de cumprimento da sentença;\n"
        j = chr(ord(j) + 1)

    # 1.2.4. MÉRITO

    # 1.2.4.1. ADVOGADOS GENÉRICOS

    #    ??? = [""]
    #    if any(word in text for word in ???):
    #        result += f"{j}) ?????;\n"
    #        j = chr(ord(j) + 1)

    # 1.2.4.2. ADVOGADOS ESPECÍFICOS

    #  Kuster Machado - CREFISA 1 - Apresentação

    CREFISA1 = ["apresentação da crefisa e do produto contratado pelo(a) autor(a)",
                "concede empréstimos a clientes de alto risco, os quais, na maioria das vezes, possuem vários protestos e dívidas cadastradas nos órgãos de proteção ao crédito",
                "está em discussão a taxa de juros cobrada em empréstimos não consignados",
                "a maior parte dos empréstimos concedidos pela crefisa tem como forma de pagamento o débito na conta corrente"]
    if any(word in text for word in CREFISA1):
        result += f"{j}) concede empréstimos a clientes de alto risco, os quais, na maioria das vezes, possuem vários protestos e dívidas cadastradas nos órgãos de proteção ao crédito e a forma de pagamento é por débito na conta corrente, inexistindo garantia atrelada à contratação e, por isso, não se aplica a ideia de onerosidade excessiva ou abusividade;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 2 -

    CREFISA2 = ["no julgamento do mesmo recurso especial nº 1.061.530/rs",
                "escolhido como representativo da controvérsia em incidente de processo repetitivo",
                "é admitida a revisão das taxas em situações excepcionais, desde que caracterizada a relação de consumo",
                "as taxas médias não podem “servir de ferramenta” exclusiva para aferir a abusividade de determinado percentual de juros remuneratórios"]
    if any(word in text for word in CREFISA2):
        result += f"{j}) conforme restou sedimentado no Recurso Especial nº 1.061.530/RS, escolhido como representativo da controvérsia em Incidente de Processo Repetitivo, a instituição de juros remuneratórios superiores a 12% ao ano, por si só, não indica abusividade, bem como que é admitida a revisão das taxas em situações excepcionais, desde que caracterizada a relação de consumo e que a abusividade (capaz de colocar o consumidor em desvantagem exagerada – art. 51, § 1º, do CDC) fique cabalmente demonstrada, ante as peculiaridades do julgamento concreto, não sendo apropriada a utilização das taxas médias divulgadas pelo Banco Central como critério exclusivo para a caracterização de prática abusiva;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 3 - SOBERANIA E AUTONOMIA DE VONTADE DOS CONTRATANTES

    CREFISA3 = ["nos empréstimos celebrados pela crefisa, os juros não são cobrados sem anuência dos contratantes",
                "a taxa de juros consta em todos os contratos e os contratantes, plenamente capazes, decidem por livre e espontânea vontade, sem qualquer vício de consentimento, celebrar os contratos de empréstimo",
                " respeitar a força obrigatória dos contratos, que faz lei entre as partes, sob pena de impedir a liberdade de contratar e, por consequência, provocar insegurança jurídica nos negócios jurídicos"]
    if any(word in text for word in CREFISA3):
        result += f"{j}) os juros não são cobrados sem anuência dos contratantes, havendo pleno consentimento e, assim, deve-se respeitar a força obrigatória dos contratos, que faz lei entre as partes, sob pena de impedir a liberdade de contratar e, por consequência, provocar insegurança jurídica nos negócios jurídicos;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 4 - NÃO EXISTE LEI QUE LIMITE A COBRANÇA DE JUROS REMUNERATÓRIOS PELAS INSTITUIÇÕES FINANCEIRAS

    CREFISA4 = [
        "a lei n.º 4.595/64, atribuiu ao conselho monetário nacional a competência para fixar a taxa de juros, as comissões e os custos dos serviços bancários",
        "liberou para o regime de mercado as taxas de juros praticadas pelas instituições financeiras, através da resolução n.º 1.064, de 05.12.85",
        "as operações ativas dos bancos comerciais, de investimento e de desenvolvimento serão realizadas a taxas de juros livremente pactuáveis",
        "não há limite para a cobrança de juros pelas instituições financeiras, podendo as taxas ser livremente pactuadas"]
    if any(word in text for word in CREFISA4):
        result += f"{j}) o Conselho Monetário Nacional, alicerçado no artigo 4º, inciso IX, da Lei n.º 4.595/64, liberou para o regime de mercado as taxas de juros praticadas pelas instituições financeiras, através da Resolução n.º 1.064, de 05.12.85 e, assim, não há limite para a cobrança de juros pelas instituições financeiras, podendo as taxas ser livremente pactuadas;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 5 - TAXAS DE JUROS VARIAM CONFORME PERFIL DO CLIENTE

    CREFISA5 = ["as taxas de juros variam em função de cada operação e de cada cliente",
                "na celebração dos contratos, após a análise de todos os fatores aqui mencionados e do perfil do Contratante é que as taxas de juros foram fixadas e aceitas"]
    if any(word in text for word in CREFISA5):
        result += f"{j}) as taxas de juros variam em função de cada operação e de cada cliente e somente depois da análise de todos os fatores de risco e do perfil do contratante que as taxas são fixadas, inexistindo ilegalidade em tal conduta;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 6 - CONTRARIEDADE AO PEDIDO DE RESTITUIÇÃO

    CREFISA6 = ["nenhum valor foi cobrado indevidamente do(a) autor(a)",
                "não há que se falar em restituição de qualquer valor ao(à) autor(a)"]
    if any(word in text for word in CREFISA6):
        result += f"{j}) nenhum valor foi cobrado indevidamente, inexistindo prova de má-fé e, por isso, não há que se falar em restituição de qualquer valor;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 7 - NÃO PRATICOU ATO ILÍCITO E, POR ISSO, SEM DANOS MORAIS

    CREFISA7 = [
        "não infringiu nenhum dever legal de conduta porque não agiu contrariamente ao direito, nem omitiu-se quando deveria agir",
        "agiu no exercício regular de seu direito, de maneira lícita, razoável e moderada, o que não representa qualquer ilicitude",
        "não há prova de qualquer dano experimentado pelo demandante",
        "não houve prática de ato ilícito, nem demonstração da ocorrência de danos",
        "não há que se falar na condenação ao pagamento de indenização por danos morais"]
    if any(word in text for word in CREFISA7):
        result += f"{j}) não praticou ato ilícito e, por isso, não há que se cogitar na condenação ao pagamento de indenização por danos morais;\n"
        j = chr(ord(j) + 1)

    #  Kuster Machado - CREFISA 8 - DA IMPOSSIBILIDADE DE INVERSÃO DO ÔNUS DA PROVA

    CREFISA8 = ["a inversão do ônus da prova somente deve ser aplicada quando presentes os requisitos que a justificam",
                "nenhuma prova foi produzida pela requerente para que possa ser considerado hipossuficiente, razão pela qual, não há sequer indícios de sua fragilidade técnica",
                "o simples requerimento de inversão do ônus da prova sem a devida comprovação da verossimilhança do pedido e da hipossuficiência do consumidor não pode ensejar a inversão do ônus da prova"]
    if any(word in text for word in CREFISA8):
        result += f"{j}) não estão presentes os requisitos autorizadores da inversão do ônus da prova em favor do consumidor;\n"
        j = chr(ord(j) + 1)

    # 1.2.5 - REQUERIMENTOS DA CONTESTAÇÃO

    # Parte INICIAL dos Requerimentos
    REQCONT = ["– requerimentos finais", "requer seja acolhida a preliminar arguida",
               "extinguindo-se o presente feito sem resolução de mérito",
               "requer que a presente ação seja julgada totalmente improcedente"]
    if any(word in text for word in REQCONT):
        result += "Pugnou pela "

        # Acolhimento da Preliminar
        ACPRELM = ["requer seja acolhida a preliminar arguida"]
        if any(word in text for word in ACPRELM):
            result += "acolhida das questões preliminares arguidas"
            ACPRELMCEX = ["a, extinguindo-se o presente feito sem resolução de mérito"]
            if any(word in text for word in ACPRELMCEX):
                result += ", extinguindo-se o presente feito sem resolução de mérito ou pela "

        # Improcedência dos Pedidos
        IMPROCED = ["requer que a presente ação seja julgada totalmente improcedente"]
        if any(word in text for word in IMPROCED):
            result += "improcedência dos pedidos formulados na petição inicial."

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
