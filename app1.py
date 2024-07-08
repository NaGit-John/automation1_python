# ウィンドウ立ち上げ
#--------------------------------

# Tkinterモジュールのインポート
import tkinter

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

root.title("自動入力")

root.geometry("400x400")

label = tkinter.Label(root, text="a")

#ラベルの表示
label.grid()

buttonFrame = tkinter.Frame(root)
button = tkinter.Button(buttonFrame, text="Load Image", command=root.load_image, width=10)
button.grid(column=0, row=0)

# イベントループ（TK上のイベントを捕捉し、適切な処理を呼び出すイベントディスパッチャ）
root.mainloop()

