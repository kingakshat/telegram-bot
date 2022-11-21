from time import time
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from gspread_formatting  import *
import datetime
import gspread
  
updater = Updater("5595907878:AAF9ovoZ91Dpb7hpb6_1UFq707PsSKbh-hM", use_context=True)
class my_funtion:
    def __init__(self):
        
        sa = gspread.service_account(filename="service_account.json")
        sh = sa.open("Monthly budget")

        self.wks = sh.worksheet("Transactions")
        self.wks2 = sh.worksheet("Summary")
        self.wks3 = sh.worksheet("Relapse")
        self.Balance = self.wks2.get("D3") 
        self.c = 16
        self.d = 25
        
        
    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.") 

    def help(self, update: Update, context: CallbackContext):
        update.message.reply_text("""Available Commands :-
        /d - To get the youtube URL
        /c - To get the LinkedIn profile URL""")
    
   
    def view(self,update: Update, context: CallbackContext):  
        a = self.wks2.get("D3")  
        str_list = str(len(list(filter(None, self.wks.col_values(2)))) + 1)
        print(str(len(str_list)+1))  
        str_list = list(filter(None, self.wks.col_values(7)))
        print(str(len(str_list)+1))  
        update.message.reply_text(f"Current Balance :- {a}")
    
   
    def creditORdebit(self,update: Update, context: CallbackContext):
        
        if update.message.text == "kings never die":
            d,m,y = map(int,datetime.date.today().strftime("%d-%m-%Y").split('-'))
            refd = {"C":1,"D":2,"E":3,"F":4,"G":5,"H":6,"I":7,"J":8,"K":9,"L":10,"M":11,"N":12,"O":13,"P":14,"Q":15,"R":16,"S":17,"T":18,"U":19,"V":20,"W":21,"X":22,"Y":23,"Z":24,"AA":25,"AB":26,"AC":27,"AD":28,"AE":29,"AF":30,"AG":31}
            refm = {10:1,11:2,12:3,1:4,2:5,3:6,4:7,5:8,6:9,7:10,8:11,9:12}
            col = list(set([(k if v==d else "A") for k,v in refd.items()]))[-1]
            row = list(set([(v if k==m else 0) for k,v in refm.items()]))[-1]

            fmt = cellFormat(
            backgroundColor=color(1, 0, 0),
            textFormat=textFormat(bold=True, foregroundColor=color(0, 1, 0)),
            horizontalAlignment='CENTER'
            )

            format_cell_range(self.wks3, 'Q3', fmt)
        elif update.message.text == "wont back down":
            fmt = cellFormat(
            backgroundColor=color(1, 0, 0),
            textFormat=textFormat(bold=True, foregroundColor=color(0, 1, 0)),
            horizontalAlignment='CENTER'
            )

            format_cell_range(self.wks3, 'Q3', fmt)
        elif update.message.text == "v":
            a = self.wks2.get("D3")
            update.message.reply_text(f"Current Balance :- {a}")
        else:
            data = update.message.text.split(" ")
            print(data)
            if int(data[0])<0:
                c = "BCDE"
                d = str(len(list(filter(None, self.wks.col_values(2)))) + 1)
            else:
                c = "GHIJ"
                d = str(len(list(filter(None, self.wks.col_values(7)))) + 1)
            try:
                data = update.message.text.split(" ")
                self.wks.update(f'{c[0]}{d}', datetime.date.today().strftime("%d-%b-%Y"))
                self.wks.update(f'{c[1]}{d}', abs(int(data[0])))
                self.wks.update(f'{c[2]}{d}', data[2])
                self.wks.update(f'{c[3]}{d}', data[1])
        
                a = self.wks2.get("C3")
                update.message.reply_text(f"Done \n Current Balance :- {a}")
            except Exception as e:
                print(e)
                update.message.reply_text(f"Could not save the Transaction \n Current Balance :- {self.Balance} \n error :- {e}")

            update.message.reply_text( "Done",update.message.text)

    def workout(self,update: Update, context: CallbackContext):  
        fmt = cellFormat(
        backgroundColor=color(1, 0, 0),
        textFormat=textFormat(bold=True, foregroundColor=color(0, 1, 0)),
        horizontalAlignment='CENTER'
        )

        format_cell_range(self.wks3, 'Q3', fmt)



obj = my_funtion()  

updater.dispatcher.add_handler(CommandHandler('start', obj.start))

updater.dispatcher.add_handler(CommandHandler('v', obj.view))

updater.dispatcher.add_handler(CommandHandler('w', obj.workout))

updater.dispatcher.add_handler(CommandHandler('help', obj.help))

updater.dispatcher.add_handler(MessageHandler(Filters.text, obj.creditORdebit))

updater.start_polling()