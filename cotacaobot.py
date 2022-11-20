import requests


def MandarMensagem(token, chat_id):
    try:
        data = {'chat_id': chat_id, 'text': Cotacao()}
        url = 'https://api.telegram.org/bot{}/sendMessage'.format(token)
        requests.get(url, data)
    except Exception as erro:
        print(f'Erro no sendMessage: {erro}')

# Conseguir o chat_id  ↓
# def last_chat_id(token):
#     try:
#         url = "https://api.telegram.org/bot{}/getUpdates".format(token)
#         response = requests.get(url)
#         if response.status_code == 200:
#             json_msg = response.json()
#             for json_result in reversed(json_msg['result']):
#                 message_keys = json_result['message'].keys()
#                 if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
#                     return json_result['message']['chat']['id']
#             print('Nenhum grupo encontrado')
#         else:
#             print('A resposta falhou, código de status: {}'.format(response.status_code))
#     except Exception as e:
#         print("Erro no getUpdates:", e)
# chat_id = last_chat_id(token)
# print(chat_id)


token = "Insira o Token do Bot"
chat_id = "Insira o id do Grupo"

# moeda tem que ser inserida em formato ISO
def Cotacao():
    moeda1 = 'BTC'
    moeda2 = 'USD'
    moeda = 'Bitcoin: '
    url = 'https://api.exchangerate.host/convert?from={moeda1}&to={moeda2}'.format(moeda1= moeda1, moeda2= moeda2)
    response = requests.get(url)
    data = response.json()
    msg = moeda + str(round(data['info']['rate'], 2))
    return msg


MandarMensagem(token, chat_id)