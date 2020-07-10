import webbrowser
from tkinter import *
from tkinter import scrolledtext


def solve_zeros(num, oper=None):
    def zeros(num):
        if len(num) == 1:
            if float(num).is_integer():
                return int(num)
            else:
                return float(num)
        if num[0] == '.':
            num = '0' + num
            return(float(num))
        elif int(num[0]) != 0:
            if float(num).is_integer(): return int(num)
            else: return float(num)
        else:
            return zeros(num[1:])
    c = zeros(num)
    if oper == None:
        return c
    else:
        for i in str(c):
            if i == '.':
                continue
            else:
                if i != '0':
                    return c
        return False

def callback(url):
    webbrowser.open_new(url)



def cross():
    global equation
    opers = ['+', '-', '*', '/']
    if equation == []:
        return
    if equation[-1] in opers:
        equation.pop(-1)
        if equation != []:
            input_num.configure(text=equation[-1])
        else:
            input_num.configure(text='0')
    else:
        if len(str(equation[-1])) == 1:
            equation.pop(-1)
            input_num.configure(text='')
        else:
            c = equation[-1]
            equation[-1] = c[:-1]
            input_num.configure(text=equation[-1])
    if len(Input.get("1.0", END)) > 1:
        Input.delete("1.0", END)
    Input.insert("1.0", input_num.cget("text"))
    get_eq()
    get_ans()



def get_eq():
    global equation
    ans = ''
    for i in equation:
        ans += str(i)
    if len(eq.get("1.0", END)) > 1:
        eq.delete("1.0", END)
    eq.insert("1.0", ans)


def dot_k(num):
    num_click('.')
    


def get_ans():
    global equation
    if equation == []:
        answer.configure(text='')
        return
    dots = 0
    c = equation[-1]
    for i in str(c):
        if i == '.':
            if dots >= 1:
                equation[-1] = c[:-1]
                input_num.configure(text=equation[-1])
                if len(Input.get("1.0", END)) > 1:
                    Input.delete("1.0", END)
                Input.insert("1.0", input_num.cget("text"))
            else:
                dots += 1
    if is_float(equation[0]):
        ans = float(equation[0])
    else: ans = int(equation[0])
    for i in range(2, len(equation), 2):
        if equation[-1] == '':
            continue
        if equation[i-1] == '+':
           ans += solve_zeros(equation[i])
        if equation[i-1] == '-':
           ans -= solve_zeros(equation[i])
        if equation[i-1] == '*':
           ans *= solve_zeros(equation[i])
        if equation[i-1] == '/':
           if not solve_zeros(equation[i], oper=12113):
               continue
           else:
                ans/= solve_zeros(equation[i], oper=234324)
    if len(str(ans)) > 16:
        ans = float(ans)
    input_num.configure(text=equation[-1])
    if len(Input.get("1.0", END)) > 2:
        Input.delete("1.0", END)
    Input.insert("1.0", input_num.cget("text"))
    answer.configure(text=str(ans))
    #if len(answer.cget("text")) > 15:
    #    out_of_range()


def is_float(num):
    if '.' in str(num):
        return True
    return False


def oper_click(oper):
    global equation
    if equation == []:
        equation.append(0)
    non_zero = False
    opers = ['+', '-', '*', '/']
    if equation[-1] not in opers:
        for i in equation[-1]:
            if int(i) != 0:
                non_zero = True
                break
        if not non_zero:
            if equation[-2] == '/':
                equation.pop(-1)
                equation.pop(-1)
    if equation[-1] not in opers and equation[-1] != '':
        equation.append(oper)
    else:
        equation[-1] = oper
    input_num.configure(text='')
    get_eq()
    if len(Input.get("1.0", END)) > 1:
       Input.delete("1.0", END)
    Input.insert("1.0", input_num.cget("text"))


def clear():
    global equation
    equation = []
    input_num.configure(text='')
    get_eq()
    get_ans()
    if len(Input.get("1.0", END)) > 1:
        Input.delete("1.0", END)
    Input.insert("1.0", input_num.cget("text"))


def num_click_k(num):
    num_click(num.char)



def num_click(num):
    global equation
    opers = ['+', '-', '*', '/']
    if equation == []:
        if num == '.':
            equation.append('0.')
        else: equation.append(num)
        input_num.configure(text=equation[-1])
    elif equation[-1] not in opers:
        if num == '.' and equation[-1] == '':
            equation.append('0.')
        else:
            final_num = equation[-1] + num
            equation[-1] = final_num
        input_num.configure(text=equation[-1])
    else:
        if num == '.':
            equation.append('0.')
        else: equation.append(num)
        input_num.configure(text=equation[-1])
    get_ans()
    get_eq()
    if len(Input.get("1.0", END)) > 1:
        Input.delete("1.0", END)
    Input.insert("1.0", input_num.cget("text"))


def out_of_range():
    c = answer.cget("text")
    answer.configure(text=[c[:16]])


def back_click(num):
    cross()


def esc_click(num):
    clear()


def oper_click_k(oper):
    oper_click(oper.char)


window = Tk()
window.title('Calculator')
window.resizable(0, 0)

for i in range(10):
    window.bind(i, num_click_k)


window.bind('+', oper_click_k)
window.bind('/', oper_click_k)
window.bind('-', oper_click_k)
window.bind('*', oper_click_k)

window.bind('.', dot_k)

window.bind('<BackSpace>', back_click)
window.bind('<Escape>', esc_click)

equation = []


input_num = Label(window, text='0', bg='white')

Input = scrolledtext.ScrolledText(height=1, width=30)
Input.grid(row=1, column=0, columnspan=100)

eq = scrolledtext.ScrolledText(height=1, bg='grey', width=30)
eq.grid(row=0, column=0, columnspan=100)



answer = Label(window, text='', font='Helvetica 18 bold')
answer.grid(row=2, column=0, columnspan=30)

link1 = Label(window, text="Click here to see the source code", fg="blue", cursor="hand2")
link1.grid(row=9, column=0, columnspan=2)
link1.bind("<Button-1>", lambda e: callback("https://www.github.com/swastik-machine-learning/python-GUI-calculator"))

# create number buttons
button_1 = Button(window, text='1', padx=40, pady=20, command=lambda: num_click('1'), activebackground='red', font='Helvetica 12')
button_2 = Button(window, text='2', padx=40, pady=20, command=lambda: num_click('2'), activebackground='red', font='Helvetica 12')
button_3 = Button(window, text='3', padx=40, pady=20, command=lambda: num_click('3'), activebackground='red', font='Helvetica 12')
button_4 = Button(window, text='4', padx=40, pady=20, command=lambda: num_click('4'), activebackground='red', font='Helvetica 12')
button_5 = Button(window, text='5', padx=40, pady=20, command=lambda: num_click('5'), activebackground='red', font='Helvetica 12')
button_6 = Button(window, text='6', padx=40, pady=20, command=lambda: num_click('6'), activebackground='red', font='Helvetica 12')
button_7 = Button(window, text='7', padx=40, pady=20, command=lambda: num_click('7'), activebackground='red', font='Helvetica 12')
button_8 = Button(window, text='8', padx=40, pady=20, command=lambda: num_click('8'), activebackground='red', font='Helvetica 12')
button_9 = Button(window, text='9', padx=40, pady=20, command=lambda: num_click('9'), activebackground='red', font='Helvetica 12')
button_0 = Button(window, text='0', padx=100, pady=20, command=lambda: num_click('0'), activebackground='red', font='Helvetica 12')
button_dot = Button(window, text='.', padx=40, pady=20, command=lambda: num_click('.'), activebackground='red', font='Helvetica 12')
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_0.grid(row=6, column=0, columnspan=2)
button_dot.grid(row=6, column=2)


# create operations
button_add = Button(window, text='+', padx=40, pady=20, command=lambda: oper_click('+'), activebackground='red', font='Helvetica 15')
button_sub = Button(window, text='-', padx=40, pady=20, command=lambda: oper_click('-'), activebackground='red', font='Helvetica 15')
button_mul = Button(window, text='*', padx=40, pady=20, command=lambda: oper_click('*'), activebackground='red', font='Helvetica 15')
button_div = Button(window, text='÷', padx=40, pady=20, command=lambda: oper_click('/'), activebackground='red', font='Helvetica 15')

button_add.grid(row=3, column=3)
button_sub.grid(row=4, column=3)
button_mul.grid(row=5, column=3)
button_div.grid(row=6, column=3)

button_clear = Button(window, text='Clear', command=clear, padx=90, pady=20, activebackground='red', font='Helvetica 12')
button_clear.grid(row=8, column=0, columnspan=2)

button_cross = Button(window, text='⌫ ', command=cross, padx=90, pady=20, activebackground='red', font='Helvetica 12')
button_cross.grid(row=8, column=2, columnspan=2)

window.mainloop()


exit
