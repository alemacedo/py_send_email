import smtplib
import email.message

def __main():
    print(f'>>>Iniciando programa de envio de email')

    # Pegar senha de arquivo
    password = get_password()

    if not password:
        print(f'Necessário informar senha.')
    else:
        enviar_email(password)

def enviar_email(password):
    print(f'função enviar email')
    corpo_email = """
    <p>Testando envio de email.</p>
    <p>Enviado via Python</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Teste python"
    # Email do remetente vai aqui
    msg['From'] = 'SENDER'
    # Email do destinatário vai aqui
    msg['To'] = 'RECEIVER'
    # Senha da conta de email
    # password = 'PASSWORD'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def prompt_password():
    # Pegar senha digitada pelo usuário
    password = input('Qual é a senha do seu email? ')

    return password

def get_password():
    # Pegar senha de arquivo secret
    with open('secret') as f:
        lines = f.readlines()

    password = lines[0]

    if password:
        return password
    else:
        # Pegar senha digitada pelo usuário
        password = prompt_password()
        return password

__main()