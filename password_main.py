# -*- coding: utf8 -*-

import sys
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        master.title(u"パスワード一覧")
        master.geometry("512x512")
        self.id_list = []
        self.pass_list = []

    def create_widgets(self):
        #リストボックス
        self.ListBox1 = tk.Listbox(self,height=16,width=48)
        self.ListBox1.grid(column=0,row=0,rowspan=4,padx=5,pady=5)
        self.ListBox1.bind("<Delete>",self.Delete_press)
        self.ListBox1.bind("<Shift-Delete>",self.Ins_press)
        #スクロールバー
        self.scrollbar1 = tk.Scrollbar(self,orient=tk.VERTICAL,command=self.ListBox1.yview)
        self.ListBox1['yscrollcommand'] = self.scrollbar1.set
        self.scrollbar1.grid(column=1,row=0,rowspan=4,sticky=tk.W+tk.N+tk.S)
        #入力ボックス１
        self.Label2 = tk.Label(text=u'Name')
        self.Label2.grid(column=2,row=0,pady=2,sticky=tk.N)
        self.TextBox1 = tk.Entry(width=25)
        self.TextBox1.grid(column=2,row=0,pady=24,sticky=tk.N)
        self.TextBox1.bind("<Return>",self.enter_press)
        #入力ボックス２
        self.Label3 = tk.Label(text=u'ID')
        self.Label3.grid(column=2,row=0,pady=42,sticky=tk.N)
        self.TextBox2 = tk.Entry(width=25)
        self.TextBox2.grid(column=2,row=0,pady=64,sticky=tk.N)
        #入力ボックス３
        self.Label4 = tk.Label(text=u'Password')
        self.Label4.grid(column=2,row=0,pady=82,sticky=tk.N)
        self.TextBox3 = tk.Entry(width=25)
        self.TextBox3.grid(column=2,row=0,pady=104,sticky=tk.N)

        #ボタン１
        self.Button1 = tk.Button(text=u'入力ボタン',width=20,command=self.button_click)
        self.Button1.grid(column=2,row=1,columnspan=2,pady=5)
        #ボタン２
        self.Button2 = tk.Button(text=u'保存ボタン',width=20,command=self.button_click1)
        self.Button2.grid(column=2,row=2,columnspan=2,pady=5)
        #ボタン３
        self.Button3 = tk.Button(text=u'呼込ボタン',width=20,command=self.button_click2)
        self.Button3.grid(column=2,row=3,columnspan=2,pady=5)
        #ラベル
        self.Label1 = tk.Label(text=u'test')
        self.Label1.grid(column=0,row=5,columnspan=2,pady=10,sticky=tk.W)

    #入力の関数
    def button_click(self):
        Val = self.TextBox1.get()
        self.Label1["text"] = Val + " を入力しました"
        self.ListBox1.insert(tk.END,Val)
        self.TextBox1.delete(0,tk.END)
        Val = self.TextBox2.get()
        self.id_list.append(Val)
        Val = self.TextBox3.get()
        self.pass_list.append(Val)
        self.Label1["text"] = self.id_list + self.pass_list

    #ファイル保存の関数
    def button_click1(self):
        file_a = open('testfile.dat','w')
        List_num = self.ListBox1.index(tk.END)
        for N in range(List_num):
            file_a.write(str(self.ListBox1.get(N) + '¥n'))
        file_a.close()
        self.Label1["text"] = "保存しました"

    #ファイルから呼び込み関数
    def button_click2(self):
        file_a = open('testfile.dat')
        line1 = file_a.read()
        file_a.close()
        line1 = line1.split()
        for N in line1:
            self.ListBox1.insert(tk.END,N)
        self.Label1["text"] = "呼び込みました"

    #エンターキーで入力関数
    def enter_press(self,event):
        self.button_click()

    #項目削除の関数
    def Delete_press(self,event):
        self.Label1["text"] ="指定場所を削除しました"
        self.ListBox1.delete(tk.ANCHOR,tk.ACTIVE)
        
    #項目の挿入
    def Ins_press(self,event):
        Val = self.TextBox1.get()
        self.Label1["text"] = Val + " を挿入しました"
        self.ListBox1.insert(tk.ACTIVE,Val)
        self.TextBox1.delete(0,tk.END)

#本体
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
