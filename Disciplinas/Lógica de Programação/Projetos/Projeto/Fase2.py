# Funcao para converter uma linha do arquivo em um dicionario
def converterLinha(linha):
    try:
        valores = linha.split(',')
        if len(valores) != 8:
            print(f"Linha inválida: {linha}")
            return None

        # Ignorar cabecalho
        if valores[0] == 'data' and valores[1] == 'precip' and valores[2] == 'maxima' and valores[3] == 'minima' and valores[4] == 'horas_insol' and valores[5] == 'temp_media' and valores[6] == 'um_relativa' and valores[7] == 'vel_vento':
            return None

        data = valores[0]
        precip_mm = float(valores[1])
        temp_max = float(valores[2])
        temp_min = float(valores[3])
        velocidade_vento = float(valores[4])
        umidade_relativa = float(valores[5])
        pressao_atm = float(valores[6])
        insolacao_horas = float(valores[7])

        return {
            'data': data,
            'precipitacao': precip_mm,
            'temp_maxima': temp_max,
            'temp_minima': temp_min,
            'umidade': umidade_relativa,
            'vento': velocidade_vento
        }

        # return [data, precip_mm, temp_max, temp_min, velocidade_vento, umidade_relativa, pressao_atm, insolacao_horas]
    except ValueError as ve:
        print(f"Erro de conversão de valor: {ve}")
        return None

# Função para ler o arquivo e converter suas linhas em dicionário


def lerArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    dadosConvertidos = []
    for i, linha in enumerate(linhas):
        linha = linha.strip()  # strip remove espacos em branco no inicio e no fim
        if linha == 0:
            continue
        if linha:  # verifica se a linha não está vazia
            resultado = converterLinha(linha)
            if resultado:
                dadosConvertidos.append(resultado)
            else:
                print(f"Linha Inválida: {linha}")

    return dadosConvertidos


nomeArquivo = 'ArquivoDados.csv'
dadosConvertidos = lerArquivo(nomeArquivo)

print(dadosConvertidos[:5])


'''
def lerArquivo(nomeArquivo):
    dados = []
    with open(nomeArquivo, 'r') as arquivo:
        cabecalho = arquivo.readline().strip().split(';')

        for linha in arquivo:
            valores = linha.strip().split(';')
            if len(valores) == 6:
                data, precip, maxima, minima, um_relativa, vel_vento = valores
                dados.append({
                    'data': data,
                    'precipitacao': precip,
                    'temp_maxima': maxima,
                    'temp_minima': minima,
                    'umidade': um_relativa,
                    'vento': vel_vento
                })
            else:
                print(f"Linha inválidaa: {linha}")

    return dados
'''

# Função para obter entrada do usuário e garantir que seja um número inteiro


def entradaUsuario(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Entrada inválida. Por favor, digite um número.")

# Função para filtrar dados com base no período e tipo de dados especificados pelo usuário


def filtrarDados(dados, anoInicial, mesInicial, anoFinal, mesFinal, tipoDados):
    dadosFiltrados = []

    for registro in dados:
        data = registro['data']
        ano = int(data.split('/')[2])
        mes = int(data.split('/')[1])

        if anoInicial <= ano <= anoFinal and (ano != anoInicial or mes >= mesInicial) and (ano != anoFinal or mes <= mesFinal):
            if tipoDados == 1:
                dadosFiltrados.append(registro)
            elif tipoDados == 2:
                dadosFiltrados.append({
                    'data': registro['data'],
                    'precipitacao': registro['precipitacao']
                })
            elif tipoDados == 3:
                dadosFiltrados.append({
                    'data': registro['data'],
                    'temp_maxima': registro['temp_maxima'],
                    'temp_minima': registro['temp_minima']
                })
            elif tipoDados == 4:
                dadosFiltrados.append({
                    'data': registro['data'],
                    'umidade': registro['umidade'],
                    'vento': registro['vento']
                })

    return dadosFiltrados

# Função para exibir dados filtrados


def exibirDados(dados):
    for registro in dados:
        print(registro)

# Função para encontrar o mês mais chuvoso no conjunto de dados


def encontrarMesMaisChuvoso(dados):
    precipMensal = {}

    for registro in dados:
        data = registro['data']
        ano, mes = data.split('/')[2], data.split('/')[1]
        chave = f"{ano}-{mes}"

        if chave not in precipMensal:
            precipMensal[chave] = 0.0

        precipMensal[chave] += float(registro['precipitacao'])

    mesMaisChuvoso = max(precipMensal, key=precipMensal.get)
    maiorPrecip = precipMensal[mesMaisChuvoso]

    return mesMaisChuvoso, maiorPrecip

# Função para calcular a média da temperatura mínima para um determinado mês nos últimos 11 anos


def calcularMediaTempMinima(dados, mesDesejado):
    tempMinimaAno = {}
    anosInteresse = range(2006, 2017)

    for ano in anosInteresse:
        chave = f"{mesDesejado:02d}-{ano}"
        tempMinimaAno[chave] = []

    for registro in dados:
        data = registro['data']
        ano, mes = int(data.split('/')[2]), int(data.split('/')[1])

        if ano in anosInteresse and mes == mesDesejado:
            chave = f"{mes:02d}-{ano}"
            tempMinimaAno[chave].append(float(registro['temp_minima']))

    mediaTempMinima = {}
    for chave, temperaturas in tempMinimaAno.items():
        if temperaturas:
            mediaTempMinima[chave] = sum(temperaturas) / len(temperaturas)
        else:
            mediaTempMinima[chave] = None

    return mediaTempMinima

# Função para calcular a média geral da temperatura mínima para um determinado mês nos últimos 11 anos


def calcularMediaGeralTempMinima(mediasTempMinima):
    temperaturas = [media for media in mediasTempMinima.values()
                    if media is not None]
    if temperaturas:
        mediaGeral = sum(temperaturas) / len(temperaturas)
        return mediaGeral
    else:
        return None


nomeArquivo = 'ArquivoDados.csv'
dadosMeteorologicos = lerArquivo(nomeArquivo)

print("Informe o período que deseja visualizar os dados.")
anoInicio = entradaUsuario("Ano inicial (1961-2016): ")
mesInicio = entradaUsuario("Mês inicial (1-12): ")
anoFim = entradaUsuario("Ano final (1961-2016): ")
mesFim = entradaUsuario("Mês final (1-12): ")

print("Escolha o tipo de dados que deseja visualizar: ")
print("1 - Todos os dados")
print("2 - Precipitação")
print("3 - Temperatura")
print("4 - Umidade e vento")
tipoDado = entradaUsuario("Opção (1-4): ")

dadosFiltrados = filtrarDados(
    dadosMeteorologicos, anoInicio, mesInicio, anoFim, mesFim, tipoDado)
exibirDados(dadosFiltrados)

# mes mais chuvoso
mesMaisChuvoso, maiorPrecip = encontrarMesMaisChuvoso(dadosMeteorologicos)
print(f"Mês mais chuvoso: {
      mesMaisChuvoso}, Precipitação: {maiorPrecip:.2f} mm")

# calcular media temperatura minima
mesDesejado = entradaUsuario(
    "Informe o mês para calcular a média de temperatura mínima (1-12): ")
mediasTempMinima = calcularMediaTempMinima(dadosMeteorologicos, mesDesejado)

for chave, media in mediasTempMinima.items():
    if media is not None:
        print(f"{chave}: Média da temperatura mínima = {media:.2f}C°")
    else:
        print(f"{chave}: Dados insuficientes.")

# calcular media geral temperatura minima
mediaGeral = calcularMediaGeralTempMinima(mediasTempMinima)
if mediaGeral is not None:
    print(f"Média geral da temperatura mínima no mês {
          mesDesejado} nos últimos 11 anos: {mediaGeral:.2f}C°")
else:
    print(f"Dados insuficientes.")
