class User:
    Chat_id = 0
    Name = ''
    Sec_name = ''
    Text = ''

    def __init__(self, Json):
        self.Chat_id = Json['result'][-1]['message']['chat']['id']
        self.Name = Json['result'][-1]['message']['chat']['first_name']
        self.Sec_name = Json['result'][-1]['message']['chat']['last_name']
        self.Text = Json['result'][-1]['message']['text']
