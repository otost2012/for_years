from  tkinter import *
import random


class Apps:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("猜数字")
        self.windows.geometry("300x150")
        self.creat_res()
        self.num=self.random_num()
        self.windows.mainloop()

    def random_num(self):
        self.num=random.randint(1,100)
        return self.num
    def creat_res(self):
        self.temp=StringVar()
        self.L1=Label(self.windows)
        self.L1.place(x=10,y=8,width=150,height=20)
        self.L2=Label(self.windows)
        self.L2.place(x=10,y=24,width=150,height=50)
        self.E1=Entry(self.windows,textvariable=self.temp,font="宋体 14")
        self.E1.place(x=10,y=70,width=150,height=50)
        self.B1=Button(self.windows,text="开始",bg="pink",command=self.run_game)
        self.B1.place(x=180,y=10,width=110,height=110)

    def run_game(self):
        try:
            self.s=int(self.E1.get())
            print(self.s)
            print(self.num)
            self.L2.config(text="你的数字:%s" % self.s, fg="red")
            if self.s > self.num:
                self.L1.config(text="啊额，太大了",fg="red")
            elif self.s<self.num:
                self.L1.config(text="很遗憾，太小了",fg="green")
            elif self.s==self.num:
                self.L1.config(text="你太棒猜对了,电脑数字%s" % (self.num),fg="blue")
            self.temp.set("")
        except Exception:
            self.L1.config(text="请输入数字，谢谢")


# a1=Apps()


