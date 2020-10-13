import win32com.client as win32

def send_mail():
    outlook = win32.Dispatch('Outlook.Application')

    mail_item = outlook.CreateItem(0) # 0: olMailItem

    mail_item.Recipients.Add('1822107818@qq.com')
    mail_item.Subject = 'Mail Test'

    mail_item.BodyFormat = 2          # 2: Html format
    mail_item.HTMLBody  = '''
        <H2>Hello, This is a test mail.</H2>
        Hello Guys and. 
        '''
    mail_item.Send()

if __name__ == '__main__':
    send_mail()
