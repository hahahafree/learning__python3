import tkinter as tk
#实例化一个Tk，用于容纳整个工艺程序
app = tk.Tk()#Tk类生成了一个顶层窗口的实例app。是top level级别的一个窗口，也是root窗口

#设置它的标题栏
app.title("hello")
#设置Label组件，Label组件是最常用的组件之一。可以用于显示文本图标图片
theLabel = tk.Label(app,text='my first program')
#pack()方法用于自动调节组件自身的尺寸以及位置
theLabel.pack()
#mainloop()是窗口的主事件循环，一般是放在整个工艺程序的最后一行，因为进入主事件循环后，就由Tkinter接管一切
app.mainloop()