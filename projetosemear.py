import pandas as pd

# Função para validar CPF
def validar_cpf(cpf):
    cpf = str(cpf).zfill(11)  # Adicionar zeros à esquerda
    if len(cpf) != 11 or not cpf.isdigit():  # Verifica se o CPF tem 11 dígitos numéricos
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))  # Calcula o dígito verificador
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):  # Compara o dígito calculado com o informado
            return False
    return True

# Função para calcular impacto por jovem
def calcular_impacto(df):
    # Limpeza e validação de CPFs
    df['CPF'] = df['CPF'].astype(str).str.replace(r'\D', '', regex=True)  # Remove caracteres não numéricos
    df['CPF'] = df['CPF'].apply(lambda x: x.zfill(11))  # Padroniza para 11 dígitos
    df['CPF_Valido'] = df['CPF'].apply(validar_cpf)  # Valida os CPFs

    # Adicionar coluna "Impactado"
    df['Impactado'] = False  # Inicializa como False
    impacto_registrado = set()  # Para rastrear jovens impactados

    # Processar cada linha para calcular impacto
    for index, row in df.iterrows():
        if row['CPF_Valido'] and row['CPF'] not in impacto_registrado and row['Carga_Horaria'] >= 1:
            df.loc[index, 'Impactado'] = True  # Marca como impactado
            impacto_registrado.add(row['CPF'])  # Adiciona o CPF ao conjunto de impactados
    return df

# Exemplo de uso com um DataFrame fictício
data = {
    'CPF': ['123.456.789-00', '98765432100', '111.222.333-44', '44455566677'],
    'Carga_Horaria': [0.5, 1.5, 2, 0.8],
    'Data': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04']
}
df = pd.DataFrame(data)

# Aplicar a função ao DataFrame
df = calcular_impacto(df)

# Exibir resultado
print(df)
