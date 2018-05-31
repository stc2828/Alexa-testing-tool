# -*- coding: utf-8 -*-  
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer 
# 构建ChatBot并指定  
bot = ChatBot(  
   'Default Response Example Bot',  
     storage_adapter='chatterbot.storage.SQLStorageAdapter', 
     input_adapter='chatterbot.input.TerminalAdapter',
     output_adapter='chatterbot.output.TerminalAdapter', 
   logic_adapters=[  
      {  
           'import_path': 'chatterbot.logic.BestMatch'  
       },  
       #{  
        #   'import_path': 'chatterbot.logic.LowConfidenceAdapter',  
         #  'threshold': 0.65,  
          # 'default_response': 'I am sorry, but I do not understand.'  
       #}  
   ],  
   trainer='chatterbot.trainers.ListTrainer') 
   
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english"
)
# 手动给定一点语料用于训练  
'''bot.train([  
   'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.'])'''
# 给定问题并取回结果  
'''question = 'How do I make an omelette?'  
print(question)  
response = bot.get_response(question)  
print(response)  
print("\n")  
question = 'how to make a chat bot?'  
print(question)  
response = bot.get_response(question)  
print(response) '''
while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break