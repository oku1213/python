import tkinter as tk
def btn_click():
    amount=int(entry1.get())
    people=int(entry2.get())

    dnum = amount/people
    pay = dnum // 100*100
    if dnum > pay:
        pay = int(pay+100)
    payorg = amount - pay*(people-1)

    label3=tk.Label(text=f'一人当たり{pay}円({people-1}人)、幹事は{payorg}円です',font=('Arial',10))
    label3.place(x=10,y=200)




root=tk.Tk()
root.title('My Window')

canvas=tk.Canvas(root,width=400,height=600,bg='skyblue')
canvas.pack()


#エントリー説明用のラベルの作成
label=tk.Label(text='金額',font=('Arial',10))
label.place(x=10,y=10)
label2=tk.Label(text='人数',font=('Arial',10))
label2.place(x=10,y=70)

#エントリーの作成
entry1=tk.Entry(width=20)
entry1.place(x=10,y=40)

entry2=tk.Entry(width=20)
entry2.place(x=10,y=100)

btn=tk.Button(text='計算する',command=btn_click)
btn.place(x=10,y=140)

root.mainloop()
