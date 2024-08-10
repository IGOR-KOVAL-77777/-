def send_email(message, recipient, sender='university.help@gmail.com'):
    ending = ['.com', '.ru', '.net']
    end_recipient = False
    end_sender = False
    if '@' in recipient and '@' in sender:
        for i in range(len(ending)):
            if ending[i] == recipient[len(recipient) - len(ending[i]):]:
                end_recipient = True
                break
        for i in range(len(ending)):
            if ending[i] == sender[len(sender) - len(ending[i]):]:
                end_sender = True
                break
        if end_recipient == False or end_sender == False:
            print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
            return
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            return
        if sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с  адреса ' + sender + ' на адрес ' + recipient)
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с  адреса ' + sender + ' на адрес ' + recipient)
    else:
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
