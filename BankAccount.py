#!/usr/bin/env python
# coding: utf-8

# In[8]:


class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial=0.0):
        self.__nome_titular = nome_titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

    def get_nome_titular(self):
        return self.__nome_titular

    def set_nome_titular(self, novo_nome):
        self.__nome_titular = novo_nome

# Exemplo de uso
conta = ContaBancaria("Diego", 100.0)
conta.consultar_saldo()  # Saída: Saldo atual: R$...

conta.depositar(30.0)  # Saída: Depósito realizado com sucesso.
conta.consultar_saldo()  # Saída: Saldo atual: R$...

conta.sacar(00.0)  # Saída: Saque realizado com sucesso.
conta.consultar_saldo()  # Saída: Saldo atual: R$...

print(conta.get_nome_titular())  # Saída: Diego

conta.set_nome_titular("Alice")
print(conta.get_nome_titular())  # Saída: Alice


# In[ ]:




