# Gmailcheck

Gmailcheck é uma ferramenta que surgiu da necessidade de validar a existência de e-mails enumerados ou permutados. 
O Google dificulta o máximo o processo de verificação de existência de e-mails a isso criamos este script utilizando selenium que tronou possível validar a existência dos e-mails.

Vale ressaltar que de acordo com o número de requests pode ser necessário reavaliar o timesleep entre as requisições. Atualmente o script foi montado observando o diferente comportamento entre as respostas para e-mail inexistente tanto no caso de e-mails @gmail.com ou mesmo de e-mails de empresas que utilizam o Gmail como serviço de email.

# Observações:

- O Script foi criado para uso com o Firefox.
- É necessário o binário geckodriver.
- Não executar o script como root. Por questões de segurança o Firefox não permite a execução como root.


Script feito por @oliveiralimajr e @DaniBoy-off
