# -*- coding: utf-8 -*-
"""funcoes_estatisticas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cqkx4nTDcU9K7-yExEjzn1L8rtvo9Gi9
"""

from scipy import stats as st

# ------------------------------------------------------------------------------
### Teste de hipótese da média com σ conhecido
### Técnica do p-valor

def teste_z(est_amostral=None, n_amostras=None, alpha=0.05, mu=0,
            sigma=1, teste='esq'):
  '''Função para teste de hipótese da média mu, com nível de significância
     alpha, supondo desvio padrão populacional sigma conhecido. Forneça a
     média amostral est_amostral, calculada a partir de n_amostras amostras
     e informe o tipo de teste: unilateral à esquerda ('esq'), unilateral à
     direita ('dir') ou bilateral ('bilateral').'''
  # Criação da distribuição amostral das médias
  dist_amostras = st.norm(loc=mu, scale=sigma/n_amostras**0.5)
  # Cálculo do p-valor, de acordo com o tipo de teste
  if teste == 'esq':
    p_valor = dist_amostras.cdf(est_amostral)
    tipo = 'unilateral à esquerda'
  elif teste == 'dir':
    p_valor = dist_amostras.sf(est_amostral)
    tipo = 'unilateral à direita'
  elif teste == 'bilateral':
    p_valor =  2*dist_amostras.cdf(est_amostral)
    tipo = 'bilateral'
  # Saída - Conclusão do teste
  print('*** Teste de hipótese para a média (sigma conhecido) ***')
  print(f'Teste {tipo} com p-valor = {p_valor:.6f}')
  if p_valor <= alpha:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return p_valor

# ------------------------------------------------------------------------------
### Teste de hipótese da média com σ conhecido
### Técnica da região de rejeição

def teste_z_alt(est_amostral=None, n_amostras=None, alpha=0.05, mu=0,
                sigma=1, teste='esq'):
  '''Função para teste de hipótese da média mu, com nível de significância
     alpha, supondo desvio padrão populacional sigma conhecido. Forneça a
     média amostral est_amostral, calculada a partir de n_amostras amostras
     e informe o tipo de teste: unilateral à esquerda ('esq'), unilateral à
     direita ('dir') ou bilateral ('bilateral').'''
  # Criação da distribuição normal padrão
  dist_padrao = st.norm(loc=0, scale=1)
  # Cálculo da estatística de teste padronizada
  z = (est_amostral-mu)/(sigma/n_amostras**0.5)
  # Hipótese nula inicialmente validade
  rejeicao = False
  # Cálculo do z crítico, de acordo com o tipo de teste
  if teste == 'esq':
    z0 = dist_padrao.ppf(alpha)
    tipo = 'unilateral à esquerda'
    # Decisão sobre pertinência de z à região de rejeição
    if z <= z0:
      rejeicao = True
  elif teste == 'dir':
    z0 = dist_padrao.ppf(1-alpha)
    tipo = 'unilateral à direita'
    # Decisão sobre pertinência de z à região de rejeição
    if z >= z0:
      rejeicao = True
  elif teste == 'bilateral':
    z0 = dist_padrao.ppf(alpha/2)
    tipo = 'bilateral'
    # Decisão sobre pertinência de z à região de rejeição
    if (z <= z0) or (z >= -z0):
      rejeicao = True
  # Saída - Conclusão do teste
  print('*** Teste de hipótese para a média (sigma conhecido) ***')
  print(f'Teste {tipo} com z0 = {z0:.6f}')
  if rejeicao:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return z0

# ------------------------------------------------------------------------------
### Teste de hipótese da média com σ desconhecido

def teste_t(est_amostral=None, n_amostras=None, alpha=0.05,
            mu=0, s_amostral=1, teste='esq'):
  '''Função para teste de hipótese da média mu, com nível de significância
     alpha, supondo desvio padrão populacional sigma desconhecido. Forneça a
     média amostral est_amostral, calculada a partir de n_amostras amostras,
     o desvio padrão populaciona s_amostral e informe o tipo de teste:
     unilateral à esquerda ('esq'), unilateral à direita ('dir') ou
     bilateral ('bilateral').'''
  # Criação da distribuição t
  dist_t = st.t(df=n_amostras-1)
  # Cálculo da estatística de teste padronizada
  t = (est_amostral-mu)/(s_amostral/n_amostras**0.5)
  # Hipótese nula inicialmente validade
  rejeicao = False
  # Cálculo do z crítico, de acordo com o tipo de teste
  if teste == 'esq':
    t0 = dist_t.ppf(alpha)
    tipo = 'unilateral à esquerda'
    # Decisão sobre pertinência de z à região de rejeição
    if t <= t0:
      rejeicao = True
  elif teste == 'dir':
    t0 = dist_t.ppf(1-alpha)
    tipo = 'unilateral à direita'
    # Decisão sobre pertinência de z à região de rejeição
    if t >= t0:
      rejeicao = True
  elif teste == 'bilateral':
    t0 = dist_t.ppf(alpha/2)
    tipo = 'bilateral'
    # Decisão sobre pertinência de z à região de rejeição
    if (t <= t0) or (t >= -t0):
      rejeicao = True
  # Saída - Conclusão do teste
  print('*** Teste de hipótese para a média (sigma desconhecido) ***')
  print(f'Teste {tipo} com t0 = {t0:.6f}')
  if rejeicao:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return t0

# ------------------------------------------------------------------------------
# Teste de hipótese da variância ou do desvio padrão

def teste_chi2(est_amostral=None, pop=None, n_amostras=None, alpha=0.05,
               teste='esq', parametro='sig'):
  '''Função para teste de hipótese da variância (parametro='sig') ou do desvio
     padrão (parametro='pad') populacional (pop), com nível de significância alpha.
     A estatística amostral (est_amostral) é obtida a partir de uma amostra com
     n_amostras elementos. Forneça o tipo de teste: unilateral à esquerda
     ('esq'), unilateral à direita ('dir') ou bilateral ('bilateral').'''
  # Criação da distribuição chi-quadrado
  dist_chi2 = st.chi2(df=n_amostras-1)
  # Cálculo da estatística de teste padronizada
  if parametro == 'sig':
    chi2 = (n_amostras-1)*est_amostral/pop
    param = 'variância'
  elif parametro == 'pad':
    chi2 = (n_amostras-1)*est_amostral**2/pop**2
    param = 'desvio padrão'
  # Hipótese nula inicialmente validade
  rejeicao = False
  # Cálculo do z crítico, de acordo com o tipo de teste
  if teste == 'esq':
    X20 = dist_chi2.ppf(alpha)
    tipo = 'unilateral à esquerda'
    # Decisão sobre pertinência de z à região de rejeição
    if chi2 <= X20:
      rejeicao = True
  elif teste == 'dir':
    X20 = dist_chi2.ppf(1-alpha)
    tipo = 'unilateral à direita'
    # Decisão sobre pertinência de z à região de rejeição
    if chi2 >= X20:
      rejeicao = True
  elif teste == 'bilateral':
    X2L = dist_chi2.ppf(alpha/2)
    X2R = dist_chi2.ppf(1-alpha/2)
    tipo = 'bilateral'
    X20 = (X2L, X2R)
    # Decisão sobre pertinência de z à região de rejeição
    if (chi2 <= X2L) or (chi2 >= X2R):
      rejeicao = True
  # Saída - Conclusão do teste
  print(f'*** Teste de hipótese para {param} ***')
  print(f'Teste {tipo} com:')
  print(f'Estatística de teste padronizada = {chi2:.4f}')
  if isinstance(X20, tuple):
    print(f'Valores chi-quadrado críticos = {X20[0]:.4f} e {X20[1]:.4f}')
  else:
    print(f'Valor chi-quadrado crítico = {X20:.4f}')
  if rejeicao:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return chi2, X20

# ------------------------------------------------------------------------------
# Teste de hipótese da diferença entre médias com σ's conhecidos

def teste_z2(xbarra_1=None, sig_1=None, n_1=None,
             xbarra_2=None, sig_2=None, n_2=None,
             alpha=0.05, teste='bilateral'):
  '''Função para teste de hipótese da diferença entre as médias populacionais,
     com nível de significância alpha, supondo desvios padrão populacionais
     sig_1 e sig_2 conhecidos. Forneça as médias amostrais xbarra_1 e xbarra_2,
     os tamanhos das amostras n_1 e n_2 e  informe o tipo de teste: unilateral
     à esquerda ('esq'), unilateral à direita ('dir') ou bilateral ('bilateral').'''
  # Criação da distribuição normal padrão
  dist_padrao = st.norm(loc=0, scale=1)
  # Cálculo da estatística de teste padronizada
  z = (xbarra_1-xbarra_2)/(sig_1**2/n_1 + sig_2**2/n_2)**0.5
  # Hipótese nula inicialmente validade
  rejeicao = False
  # Cálculo do z crítico, de acordo com o tipo de teste
  if teste == 'esq':
    z0 = dist_padrao.ppf(alpha)
    tipo = 'unilateral à esquerda'
    # Decisão sobre pertinência de z à região de rejeição
    if z <= z0:
      rejeicao = True
  elif teste == 'dir':
    z0 = dist_padrao.ppf(1-alpha)
    tipo = 'unilateral à direita'
    # Decisão sobre pertinência de z à região de rejeição
    if z >= z0:
      rejeicao = True
  elif teste == 'bilateral':
    z0 = dist_padrao.ppf(alpha/2)
    tipo = 'bilateral'
    # Decisão sobre pertinência de z à região de rejeição
    if (z <= z0) or (z >= -z0):
      rejeicao = True
  # Saída - Conclusão do teste
  print('*** Teste de hipótese para a diferença entre médias populacionais ***')
  print('-> Desvios padrão populacionais conhecidos')
  if tipo == 'bilateral':
    print(f'-> Teste {tipo} com z_padrão = {z:.6f}, z01 = {z0:.6f} e z02 = {-z0:.6f}')
  else:
    print(f'-> Teste {tipo} com z_padrão = {z:.6f} e z0 = {z0:.6f}')
  if rejeicao:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return z, z0

# ------------------------------------------------------------------------------
# Teste de hipótese da diferença entre médias com σ's desconhecidos

def teste_t2(xbarra_1=None, s_1=None, n_1=None,
             xbarra_2=None, s_2=None, n_2=None,
             alpha=0.05, var='=', teste='bilateral'):
  '''Função para teste de hipótese da diferença entre as médias populacionais,
     com nível de significância alpha, supondo desvios padrão populacionais
     sig_1 e sig_2 desconhecidos. Forneça as médias amostrais xbarra_1 e xbarra_2,
     os tamanhos das amostras n_1 e n_2 e  informe o tipo de teste: unilateral
     à esquerda ('esq'), unilateral à direita ('dir') ou bilateral ('bilateral').'''
  # Graus de liberdade e erro padrão
  if var == '=':
    gl = n_1 + n_2 - 2
    sig_chapeu = (((n_1-1)*s_1**2 + (n_2-1)*s_2**2)/gl)**0.5
    erro_pad = sig_chapeu*(1/n_1 + 1/n_2)**0.5
  elif var == '!=':
    gl = min(n_1-1, n_2-1)
    erro_pad = (s_1**2/n_1 + s_2**2/n_2)**0.5
  # Criação da distribuição t
  dist_t = st.t(df=gl)
  # Cálculo da estatística de teste padronizada
  t = (xbarra_1 - xbarra_2)/erro_pad
  # Hipótese nula inicialmente validade
  rejeicao = False
  # Cálculo do t crítico, de acordo com o tipo de teste
  if teste == 'esq':
    t0 = dist_t.ppf(alpha)
    tipo = 'unilateral à esquerda'
    # Decisão sobre pertinência de z à região de rejeição
    if t <= t0:
      rejeicao = True
  elif teste == 'dir':
    t0 = dist_t.ppf(1-alpha)
    tipo = 'unilateral à direita'
    # Decisão sobre pertinência de z à região de rejeição
    if t >= t0:
      rejeicao = True
  elif teste == 'bilateral':
    t0 = dist_t.ppf(alpha/2)
    tipo = 'bilateral'
    # Decisão sobre pertinência de z à região de rejeição
    if (t <= t0) or (t >= -t0):
      rejeicao = True
  # Saída - Conclusão do teste
  print('*** Teste de hipótese para a diferença entre médias populacionais ***')
  print('-> Desvios padrão populacionais desconhecidos')
  if tipo == 'bilateral':
    print(f'-> Teste {tipo} com t_padrão = {t:.6f}, t01 = {t0:.6f} e t02 = {-t0:.6f}')
  else:
    print(f'-> Teste {tipo} com t_padrão = {t:.6f} e t0 = {t0:.6f}')
  if rejeicao:
    print(f'Hipótese nula rejeitada ao nível de significância {alpha*100}%')
  else:
    print(f'Hipótese nula NÃO rejeitada ao nível de significância {alpha*100}%')
  return t, t0