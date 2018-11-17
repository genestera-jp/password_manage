# -*- coding: utf8 -*-

import sys
import tkinter as tk
import pickle
import password_str as pw
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.master.title(u"パスワード一覧")
        self.master.geometry("512x512")
        self.id_list = []
        self.pass_list = []
        self.save_list = []
        self.path = os.path.join(os.path.dirname(__file__),'file_data.dat')

    def create_widgets(self):
        #リストボックス
        self.ListBox1 = tk.Listbox(self,height=16,width=32)
        self.ListBox1.grid(row=0,column=0,padx=5,pady=5,sticky=tk.N)
        self.ListBox1.bind("<Delete>",self.Delete_press)
        self.ListBox1.bind("<Shift-Delete>",self.Ins_press)
        self.ListBox1.bind("<Double-1>",self.Show_press)
        #スクロールバー
        self.scrollbar1 = tk.Scrollbar(self,orient=tk.VERTICAL,command=self.ListBox1.yview)
        self.ListBox1['yscrollcommand'] = self.scrollbar1.set
        self.scrollbar1.grid(row=0,column=1,sticky=tk.W+tk.N+tk.S)
        #入力ボックスフレーム
        self.in_f = tk.Frame(self.master)
        #入力ボックス１
        self.Label2 = tk.Label(self.in_f,text=u'Name')
        self.Label2.grid(row=0)
        self.TextBox1 = tk.Entry(self.in_f,width=32)
        self.TextBox1.grid(row=1)
        #入力ボックス２
        self.Label3 = tk.Label(self.in_f,text=u'ID')
        self.Label3.grid(row=2)
        self.TextBox2 = tk.Entry(self.in_f,width=32)
        self.TextBox2.grid(row=3)
        #入力ボックス３
        self.Label4 = tk.Label(self.in_f,text=u'Password')
        self.Label4.grid(row=4)
        self.TextBox3 = tk.Entry(self.in_f,width=16)
        self.TextBox3.grid(row=5)
        #入力ボタン
        self.Button1 = tk.Button(self.in_f,text=u'入力ボタン',width=20,command=self.button_clickin)
        self.Button1.grid(row=6,pady=20)
        #入力ボックスフレームの表示
        self.in_f.grid(row=0,column=2)
        #クリアボタン
        self.Button4 = tk.Button(text=u'クリアボタン',width=20,command=self.button_clickcr)
        self.Button4.grid(row=1,column=2,pady=5)
        #保存ボタン
        self.Button2 = tk.Button(text=u'保存ボタン',width=20,command=self.button_clicksv)
        self.Button2.grid(row=2,column=0,pady=5)
        #呼び込みボタン
        self.Button3 = tk.Button(text=u'呼込ボタン',width=20,command=self.button_clickld)
        self.Button3.grid(row=2,column=2,pady=5)
        #パスワード作成ボタン
        self.Button5 = tk.Button(text=u'パスワード作成',width=20,command=self.button_clickpw)
        self.Button5.grid(row=3,column=2,pady=5)
        #通知ラベル
        self.Label1 = tk.Label(root,text=u'処理結果を表示します')
        self.Label1.grid(row=4,pady=20,sticky=tk.W+tk.S)

    #入力のクリア
    def button_clickcr(self):
        self.TextBox1.delete(0,tk.END)
        self.TextBox2.delete(0,tk.END)
        self.TextBox3.delete(0,tk.END)
        self.TextBox1.focus_set()
        self.Label1["text"] = u"入力クリアしました"

    #パスワード作成
    def button_clickpw(self):
        self.TextBox3.delete(0,tk.END)
        self.Val = pw.pass_make()
        self.TextBox3.insert(tk.END,self.Val)
        self.Label1["text"] = u"パスワードを作成しました"

    #データ入力
    def button_clickin(self):
        self.Val = self.TextBox1.get()
        if self.Val == '':
            self.Label1["text"] = u"入力されていません"
            return
        self.ListBox1.insert(tk.END,self.Val)
        self.Val = self.TextBox2.get()
        self.id_list.append(self.Val)
        self.Val = self.TextBox3.get()
        self.pass_list.append(self.Val)
        self.button_clickcr()
        self.Label1["text"] = u"入力しました"
        
    #ファイル保存
    def button_clicksv(self):
        self.save_list.append(list(self.ListBox1.get(0,tk.END)))
        self.save_list.append(self.id_list)
        self.save_list.append(self.pass_list)
        with open(self.path,'wb') as file_a:
            pickle.dump(self.save_list,file_a)
        self.Label1["text"] = u"保存しました"
        self.save_list = []

    #ファイルから呼び込み
    def button_clickld(self):
        if os.path.isfile(self.path) == False:
            self.Label1["text"] = u"ファイルがありません"
            return
        with open(self.path,'rb') as file_a:
            self.save_list = pickle.load(file_a)
        for N in self.save_list[0]:
            self.ListBox1.insert(tk.END,N)
        self.id_list = self.save_list[1]
        self.pass_list = self.save_list[2]
        self.Label1["text"] = u"呼び込みました"
        self.save_list = []

    #項目の削除
    def Delete_press(self,event):
        self.Val = self.ListBox1.index(tk.ACTIVE)
        self.ListBox1.delete(self.Val,self.Val)
        del self.id_list[self.Val]
        del self.pass_list[self.Val]
        self.Label1["text"] = u"指定場所を削除しました"

    #項目の挿入
    def Ins_press(self,event):
        self.Val = self.ListBox1.index(tk.ACTIVE)
        self.ins_Val = self.TextBox1.get()
        self.ListBox1.insert(self.Val,self.ins_Val)
        self.ins_Val = self.TextBox2.get()
        self.id_list.insert(self.Val,self.ins_Val)
        self.ins_Val = self.TextBox3.get()
        self.pass_list.insert(self.Val,self.ins_Val)
        self.button_clickcr()
        self.Label1["text"] = u"挿入しました"
        
    #項目の表示
    def Show_press(self,event):
        self.Val = self.ListBox1.index(tk.ACTIVE)
        self.N = self.ListBox1.get(self.Val)
        self.button_clickcr()
        self.TextBox1.insert(tk.END,self.N)
        self.TextBox2.insert(tk.END,self.id_list[self.Val])
        self.TextBox3.insert(tk.END,self.pass_list[self.Val])
        self.master.clipboard_clear()
        self.master.clipboard_append(self.pass_list[self.Val])
        self.Label1["text"] = u"表示しました"

#本体
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
