import tkinter as tk
import sys
import os
from PIL import ImageTk, Image

from PSO import pso

class Aplicacion:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('DCI-NET FRAMEWORK')
        self.root.geometry('500x500')
        self.base = tk.Frame()
        self.base.pack(expand=True)
        # FRAMES
        self.main_frame = MainFrame(self.base)
        self.pso_frame = PsoFrame(self.base)
        self.main_frame.frm.pack(expand=True)



        self.menus = {'Metaheuristicas':[('PSO',self.pso_frame.show)]
                    #                    ('Ant Colony',self.pso_frame.show)],
                    #    'Redes neuronales':[('Señales ABR',self.salir)]
                    }

        self.agregar_menus()
        self.root.mainloop()
    def agregar_menus(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        menubar.add_command(label='Pagina principal', command=lambda:[self.clear_window(),self.main_frame.show()])

        for titulo, opciones in self.menus.items():
            menu = tk.Menu(menubar, tearoff=0)
            for opcion in opciones:
                print(opcion[0],opcion[1])
                menu.add_command(label=opcion[0], command=lambda:[self.clear_window(),opcion[1]()])
            menubar.add_cascade(label=titulo, menu=menu)
        menubar.add_command(label='Salir', command=self.salir)
    def clear_window(self):
        #print(len(self.base.winfo_children()))
        for child in self.base.winfo_children():
            child.pack_forget()
    def salir(self):
        sys.exit()
class GeneralFrame:
    def __init__(self,master):
        self.frm = tk.Frame(master)
    def hide(self):
        self.frm.pack_forget()
    def show(self):
        self.frm.pack(expand=True)
class MainFrame(GeneralFrame):
    def __init__(self,master):
        super().__init__(master)
        self.path = os.path.join(os.getcwd(),'logo.png')
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.logo = tk.Label(self.frm, image = self.img)
        self.saludo = tk.Label(self.frm, text = 'Somos DCI-NET')
        self.logo.grid(row=0,column=0)
        self.saludo.grid(row=1,column=0)
        self.saludo.config(font=('Times New Roman', 16))
class PsoFrame(GeneralFrame):
    def __init__(self,master):
        super().__init__(master)
        # Titulo
        self.titulo = tk.Label(self.frm, text='Parametros PSO')
        self.titulo.grid(row=0, column=0)
        self.titulo.config(font=('Times New Roman', 16))
        # Numero de Particulas
        self.l_np = tk.Label(self.frm, text='Numero de Particulas')
        self.l_np.grid(row=1, column=0)
        self.l_np.config(padx=10, pady=10)
        self.np_cuadro=tk.Entry(self.frm)
        self.np_cuadro.insert(tk.END, 20)
        self.np_cuadro.grid(row=1, column=1)
        # C1
        self.l_c1 = tk.Label(self.frm, text='C1 (Factor cognitivo)')
        self.l_c1.grid(row=2, column=0)
        self.l_c1.config(padx=10, pady=10)
        self.c1_cuadro=tk.Entry(self.frm)
        self.c1_cuadro.insert(tk.END, 1)
        self.c1_cuadro.grid(row=2, column=1)
        # C2
        self.l_c2 = tk.Label(self.frm, text='C2 (Factor social)')
        self.l_c2.grid(row=3, column=0)
        self.l_c2.config(padx=10, pady=10)
        self.c2_cuadro=tk.Entry(self.frm)
        self.c2_cuadro.insert(tk.END, 1)
        self.c2_cuadro.grid(row=3, column=1)
        # W_max
        self.l_wmx = tk.Label(self.frm, text='Inercia maxima')
        self.l_wmx.grid(row=4, column=0)
        self.l_wmx.config(padx=10, pady=10)
        self.wmx_cuadro=tk.Entry(self.frm)
        self.wmx_cuadro.insert(tk.END, 0.9)
        self.wmx_cuadro.grid(row=4, column=1)
        # W_min
        self.l_wmn = tk.Label(self.frm, text='Inercia minima')
        self.l_wmn.grid(row=5, column=0)
        self.l_wmn.config(padx=10, pady=10)
        self.wmn_cuadro=tk.Entry(self.frm)
        self.wmn_cuadro.insert(tk.END, 0.4)
        self.wmn_cuadro.grid(row=5, column=1)
        # Numero de iteraciones
        self.l_mxi = tk.Label(self.frm, text='Numero maximo de iteraciones')
        self.l_mxi.grid(row=6, column=0)
        self.l_mxi.config(padx=10, pady=10)
        self.mxi_cuadro=tk.Entry(self.frm)
        self.mxi_cuadro.insert(tk.END, 50)
        self.mxi_cuadro.grid(row=6, column=1)
        # Angulo azimutal
        self.l_az = tk.Label(self.frm, text='Angulo azimutal')
        self.l_az.grid(row=7, column=0)
        self.l_az.config(padx=10, pady=10)
        self.az_cuadro=tk.Entry(self.frm)
        self.az_cuadro.insert(tk.END, 30)
        self.az_cuadro.grid(row=7, column=1)
        # Nivel de elevacion
        self.l_ele = tk.Label(self.frm, text='Nivel de elevacion')
        self.l_ele.grid(row=8, column=0)
        self.l_ele.config(padx=10, pady=10)
        self.ele_cuadro=tk.Entry(self.frm)
        self.ele_cuadro.insert(tk.END, 30)
        self.ele_cuadro.grid(row=8, column=1)
        # Funcion
        self.l_f = tk.Label(self.frm, text='Funcion a evaluar')
        self.l_f.grid(row=9, column=0)
        self.l_f.config(padx=10, pady=10)
        self.func = tk.StringVar(None)
        self.f_cuadro = tk.OptionMenu(self.frm,self.func,"Beale", "Esfera", "Goldstein")
        self.f_cuadro.grid(row=9, column=1)
        # Boton para ejecutar
        self.boton = tk.Button(self.frm, text="Ejecutar PSO",command=self.ejecutar_pso)
        self.boton.grid(row=10,columnspan=2)
        # Resultado
        self.label = tk.Label(self.frm)
        self.label.grid(row=11, column=0)
        self.label.config(padx=10, pady=10)
    def ejecutar_pso(self):
        flag = True
        try:
            np = int(self.np_cuadro.get())
            c1 = float(self.c1_cuadro.get())
            c2 = float(self.c2_cuadro.get())
            w_max = float(self.wmx_cuadro.get())
            w_min = float(self.wmn_cuadro.get())
            max_iter = int(self.mxi_cuadro.get())
            azim = int(self.az_cuadro.get())
            ele = int(self.ele_cuadro.get())
        except ValueError:
            flag = False
        if not self.func.get():
            flag = False
        if flag:
            with open(os.path.join(os.getcwd(),'PSO/parametros.txt'),'w') as f:
                f.write('Numero de Particulas='+str(np)+'\n')
                f.write('c1 (Factor cognitivo)='+str(c1)+'\n')
                f.write('c2 (Factor social)='+str(c2)+'\n')
                f.write('Inercia Maxima='+str(w_max)+'\n')
                f.write('Inercia minima='+str(w_min)+'\n')
                if self.func.get() == 'Beale':
                    f.write('Limite en x=5\n')
                    f.write('Limite en y=5\n')
                elif self.func.get() == 'Esfera':
                    f.write('Limite en x=10\n')
                    f.write('Limite en y=10\n')
                elif self.func.get() == 'Goldstein':
                    f.write('Limite en x=2\n')
                    f.write('Limite en y=2\n')
                f.write('Numero maximo de iteraciones='+str(max_iter)+'\n')
                f.write('Angulo azimutal='+str(azim)+'\n')
                f.write('Nivel de elevacion='+str(ele)+'\n')
                if self.func.get() == 'Beale':
                    f.write('Funcion=beale\n')
                elif self.func.get() == 'Esfera':
                    f.write('Funcion=sphere\n')
                elif self.func.get() == 'Goldstein':
                    f.write('Funcion=gold\n')
            self.label.config(text='Listo!')
            pso.pso_anim()

        else:
            self.label.config(text='Parametros no validos')


if __name__ == '__main__':
    Aplicacion()
