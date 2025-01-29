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

        return lst
        
    
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
        self.active_button = None  
        
    def create_buttons(self, x, y, chosen_car, color_dic, multiplier=1):
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
        
        
        print("lst")
        counter = -1
        print(self.full_lst[5][1])
        for i in range(0, self.y):
            for j in range(0, self.x):
                counter+=1
                try:
                    text = self.full_lst[counter][1]
                    print(self.full_lst)
                except:
                    text = " "
                #color = color_dic[self.full_lst[counter][0]]
            
                button = ctk.CTkButton(frame, text=text, fg_color="white", text_color="black", corner_radius=10, font=("Arial", 80), width=10, height=80)
                button.configure(command=lambda i=button: self.button_click(i))
                button.grid(row=i%self.y, column=j, pady=5, padx=5, sticky="nsew")
                self.buttons_1.append(button)
            self.buttons.append(self.buttons_1)
        
        col = 0
        row = 0
        lst = []
        for i in self.chosen_car:
            for j in i:
                if j not in lst:
                    lst.append(j)
        c_w = [i for i in range(0, len(lst)//2)]
        frame2.grid_columnconfigure(c_w, weight=1)
        frame2.grid_rowconfigure((0, 1), weight=1)
        print("dic")
        print(self.dic)
        for count, i in enumerate(self.dic):
                if col == len(self.dic)//2:
                    col = 0
                    row += 1
                button = ctk.CTkButton(frame2, text=self.dic[count][1], fg_color="white", text_color="black", corner_radius=100, width=10)
                button.configure(command=lambda i=button: self.activate_button(i))
                button.grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
                col += 1
            
        
    def activate_button(self, button):
        if self.active_button != None:
            self.active_button.configure(fg_color="white")
        button.configure(fg_color="light blue")
        self.active_button = button
        
        
        
class Application(GUI):
    def __init__(self):
        super().__init__()
        self.update()   
        
        
        self.bind("<Alt_L>", lambda e: self.suicide())
        self.randomgenerate = RandomNumberGenerator()
        self.lst = self.randomgenerate.read_file("car.txt")
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
            ",": "gray",
            "Y": "gray",
        }
        self.chosen_car = random.choice(self.lst)
        print(self.chosen_car)
        longest = 0
        print()
        print()
        for i in self.chosen_car:
            if len(i) > longest:
                longest = len(i)
            print(i)
        print("self.chosen_car")
        print(self.chosen_car)
        for i in range(len(self.chosen_car)):
            while len(self.chosen_car[i]) < longest:
                self.chosen_car[i]+=" "
        height = len(self.chosen_car)
        multiplier = 1
        x = longest * multiplier
        y = height * multiplier
        print("x, y")
        print(x, y)
        
        self.dic = []
        self.full_lst = []
        counter = 0
        for i in self.chosen_car:
            print(i)
            counter += len(i)
        lst4 = [i for i in range(counter)]
        lst5 = []
        for w in self.chosen_car:
            for i in w:
                z = random.choice(lst4)
                
                if i in lst5:
                    jj = self.dic[lst5.index(i)][1]
                    self.full_lst.append([i, jj])
                    continue
                else:
                    self.full_lst.append([i, z])
                lst4.remove(z)
                lst5.append(i)
                self.dic.append([i, z])
                

        
        self.create_buttons(x, y, self.chosen_car, self.color_dic, multiplier)
        self.updat()
        
    def updat(self):
        self.excep = False
        while True and not self.excep:
            self.update()
    
    def button_click(self, button):
        print(button.cget("text"))
        for i in self.dic:
            val = int(button.cget("text"))
            if i[1] == val:
                right = i[0]
                break
        print(right)
        print(self.color_dic[right])
        if self.active_button != None and val == int(self.active_button.cget("text")):
            button.configure(text=right, text_color=self.color_dic[right])  
    
    def suicide(self):
        self.excep = True
        exit()
        
        
        
        
if __name__ == "__main__":
    app = Application()