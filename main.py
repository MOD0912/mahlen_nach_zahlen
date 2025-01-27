import customtkinter as ctk
import random
ctk.deactivate_automatic_dpi_awareness()

class RandomNumberGenerator:
    def __init__(self):
        self.operators = ['+', '-']
    
    def read_file(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
        lst = [] 
        lst2 = [] 
        lst3 = []
        for line in lines:
            if line == "ÃŸ\n":
                x = lst2.copy()
                lst.append(x)
                lst2.clear()
            else:
                lst2.append(line)
                lst2[-1] = lst2[-1].replace("\n", "")

        for i in lst:
            for j in i:
                for x in j:
                    if x not in lst3 and x != "Ã" and x != "Ÿ" and x != "\n":
                        lst3.append(x)


        print(lst3)

        self.dic = {}
        lst4 = [i for i in range(len(lst3))]
 

        for i in lst3:
            x = random.choice(lst4)
            lst4.remove(x)
            self.dic[x] = i
        for i in lst[0]:
            print(i)
        print(self.dic)
        return self.dic, lst[1]
        
    
    def generate_number(self, button, real_result, x, y):
        while True:
            number1 = random.randint(0, x)
            number2 = random.randint(0, y)
            operator = random.choice(self.operators)
            
            if operator == '+':
                result = number1 + number2
            else:
                result = number1 - number2
            
            if result == real_result:
                return [button, number1, operator, number2]
            
            
            
class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mahlen nach Zahlen")
        self.car = []
        
    def create_buttons(self, x, y, chosen_car, dic, color_dic, multiplier=1):
        self.x = x
        self.y = y
        
        self.buttons = []
        self.buttons_1 = []
        var = ctk.StringVar()
        var.set(" ")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        frame = ctk.CTkFrame(self)
        c_w = [i for i in range(0, self.x)]
        r_w = [i for i in range(0, self.y)]
        frame.grid_columnconfigure(c_w, weight=1)
        frame.grid_rowconfigure(r_w, weight=1)
        frame.grid(row=0, column=0, sticky="nsew")
        
        frame2 = ctk.CTkFrame(self)
        frame2.grid(row=1, column=0, sticky="nsew")
        
        
        
        
        for i in range(0, self.y):
            for j in range(0, self.x):
                try: 
                    color = color_dic[chosen_car[i//multiplier][j//multiplier]]
                    text = chosen_car[i//multiplier][j//multiplier]
                except:
                    color = "grey"
                    text = " "
                
                button = ctk.CTkButton(frame, text=text, fg_color="white", text_color=color, corner_radius=10, font=("Arial", 80), textvariable=var)
                button.configure(command=lambda i=button: self.button_click(i))
                button.grid(row=i%self.y, column=j, pady=5, padx=5, sticky="nsew")
                self.buttons_1.append(button)
            self.buttons.append(self.buttons_1)
        
        print(len(self.dic))
        
        col = 0
        row = 0
        lst = []
        for i in self.chosen_car:
            for j in i:
                if j not in lst:
                    lst.append(j)
        print()
        print(lst)
        print()
        
        c_w = [i for i in range(0, len(lst)//2)]
        frame2.grid_columnconfigure(c_w, weight=1)
        frame2.grid_rowconfigure((0, 1), weight=1)
        for j in dic
        for count, i in enumerate(lst):
                if col == len(lst)//2:
                    col = 0
                    row += 1
                button = ctk.CTkButton(frame2, text=dic.keys[count], fg_color="white", text_color="black", corner_radius=100, width=10)
                button.configure(command=lambda i=button: self.button_click(i))
                button.grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
                col += 1
            
        


class Application(GUI):
    def __init__(self):
        super().__init__()
        self.update()   
        
        
        self.bind("<Alt_L>", lambda e: self.suicide())
        self.randomgenerate = RandomNumberGenerator()
        self.dic, self.lst = self.randomgenerate.read_file("car.txt")
        self.color_dic = {
            "/": "black",
            "|": "black",
            "\\": "black",
            "(": "black",
            ")": "black",
            "}": "orange",
            "{": "pink",
            "'": "brown",
            '"': "blue",
            "[": "red",
            "]": "red",
            "=": "black",
            " ": "grey",
            "`": "black",
            "~": "black",
            "!": "grey",
            "@": "grey",
            "#": "grey",
            "$": "grey",
            "%": "grey",
            "^": "grey",
            "&": "grey",
            "*": "grey",
            "_": "black",
            "+": "grey",
            "-": "black",
            "´": "grey",
            "o": "blue",
            ".": "pink",
            "d": "pink",
            "b": "pink",
            "<": "gray",
            ">": "gray",
        }
        self.chosen_car = random.choice(self.lst)
        print(self.chosen_car)
        self.chosen_car = self.lst
        print(self.chosen_car)
        longest = 0
        print()
        print()
        for i in self.chosen_car:
            if len(i) > longest:
                longest = len(i)
            print(i)
        height = len(self.chosen_car)
        multiplier = 1
        x = longest * multiplier
        y = height * multiplier
        print(x, y)
        
        self.create_buttons(x, y, self.chosen_car, self.dic, self.color_dic, multiplier)
        self.updat()
        
    def updat(self):
        self.excep = False
        while True and not self.excep:
            self.update()
    
    def button_click(self, button):
        x = self.color_dic[button.cget("text")]
        print(button.cget("text"))
        print(x)
    
    def suicide(self):
        self.excep = True
        exit()
        
        
        
        
if __name__ == "__main__":
    app = Application()