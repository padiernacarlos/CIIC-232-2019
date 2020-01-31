import tkinter as tk
import sys
import os
from PSO import pso


class Aplicacion:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('DCI-NET FRAMEWORK')
        self.root.geometry('500x500')
        self.menus = {'Metaheuristicas':[('PSO',self.pso_param_frm)],
                        'Redes neuronales':[('Señales ABR',self.salir)]
                    }
        self.agregar_menus()

        # Seccion Metaheuristicas
        self.parametros_pso = {}
        self.root.mainloop()

    def agregar_menus(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        for titulo, opciones in self.menus.items():
            menu = tk.Menu(menubar, tearoff=0)
            for opcion in opciones:
                menu.add_command(label=opcion[0], command=opcion[1])
            menubar.add_cascade(label=titulo, menu=menu)
        menubar.add_command(label='Salir', command=self.salir)



    def pso_param_frm(self):


        params_f = tk.Frame(self.root)
        params_f.pack(expand=True)
        titulo = tk.Label(params_f, text="PARAMETROS PSO")
        titulo.grid(row=0, column=0)
        titulo.config(font=('Times New Roman', 16))

        # Numero de particulas
        label = tk.Label(params_f, text='Numero de Particulas')
        label.grid(row=1, column=0)
        label.config(padx=10, pady=10)
        np_cuadro=tk.Entry(params_f)
        np_cuadro.insert(tk.END, 20)
        np_cuadro.grid(row=1, column=1)
        # C1
        label = tk.Label(params_f, text='C1 (Factor cognitivo)')
        label.grid(row=2, column=0)
        label.config(padx=10, pady=10)
        c1_cuadro=tk.Entry(params_f)
        c1_cuadro.insert(tk.END, 1)
        c1_cuadro.grid(row=2, column=1)
        # C2
        label = tk.Label(params_f, text='C2 (Factor social)')
        label.grid(row=3, column=0)
        label.config(padx=10, pady=10)
        c2_cuadro=tk.Entry(params_f)
        c2_cuadro.insert(tk.END, 1)
        c2_cuadro.grid(row=3, column=1)
        # W_max
        label = tk.Label(params_f, text='Inercia maxima')
        label.grid(row=4, column=0)
        label.config(padx=10, pady=10)
        wmx_cuadro=tk.Entry(params_f)
        wmx_cuadro.insert(tk.END, 0.9)
        wmx_cuadro.grid(row=4, column=1)
        # W_min
        label = tk.Label(params_f, text='Inercia minima')
        label.grid(row=5, column=0)
        label.config(padx=10, pady=10)
        wmn_cuadro=tk.Entry(params_f)
        wmn_cuadro.insert(tk.END, 0.4)
        wmn_cuadro.grid(row=5, column=1)
        # Numero de iteraciones
        label = tk.Label(params_f, text='Numero maximo de iteraciones')
        label.grid(row=6, column=0)
        label.config(padx=10, pady=10)
        mxi_cuadro=tk.Entry(params_f)
        mxi_cuadro.insert(tk.END, 50)
        mxi_cuadro.grid(row=6, column=1)
        # Angulo azimutal
        label = tk.Label(params_f, text='Angulo azimutal')
        label.grid(row=7, column=0)
        label.config(padx=10, pady=10)
        az_cuadro=tk.Entry(params_f)
        az_cuadro.insert(tk.END, 30)
        az_cuadro.grid(row=7, column=1)
        # Nivel de elevacion
        label = tk.Label(params_f, text='Nivel de elevacion')
        label.grid(row=8, column=0)
        label.config(padx=10, pady=10)
        ele_cuadro=tk.Entry(params_f)
        ele_cuadro.insert(tk.END, 30)
        ele_cuadro.grid(row=8, column=1)
        # Funcion
        label = tk.Label(params_f, text='Funcion a evaluar')
        label.grid(row=9, column=0)
        label.config(padx=10, pady=10)
        func = tk.StringVar(None)
        f_cuadro = tk.OptionMenu(params_f,func,"Beale", "Esfera", "Goldstein")
        f_cuadro.grid(row=9, column=1)

        def ejecutar_pso():
            flag = True
            try:
                np = int(np_cuadro.get())
                c1 = float(c1_cuadro.get())
                c2 = float(c2_cuadro.get())
                w_max = float(wmx_cuadro.get())
                w_min = float(wmn_cuadro.get())
                max_iter = int(mxi_cuadro.get())
                azim = int(az_cuadro.get())
                ele = int(ele_cuadro.get())
            except ValueError:
                flag = False
            if not func.get():
                flag = False
            if flag:
                with open(os.path.join(os.getcwd(),'PSO/parametros.txt'),'w') as f:
                    f.write('Numero de Particulas='+str(np)+'\n')
                    f.write('c1 (Factor cognitivo)='+str(c1)+'\n')
                    f.write('c2 (Factor social)='+str(c2)+'\n')
                    f.write('Inercia Maxima='+str(w_max)+'\n')
                    f.write('Inercia minima='+str(w_min)+'\n')
                    if func.get() == 'Beale':
                        f.write('Limite en x=5\n')
                        f.write('Limite en y=5\n')
                    elif func.get() == 'Esfera':
                        f.write('Limite en x=10\n')
                        f.write('Limite en y=10\n')
                    elif func.get() == 'Goldstein':
                        f.write('Limite en x=2\n')
                        f.write('Limite en y=2\n')
                    f.write('Numero maximo de iteraciones='+str(max_iter)+'\n')
                    f.write('Angulo azimutal='+str(azim)+'\n')
                    f.write('Nivel de elevacion='+str(ele)+'\n')
                    if func.get() == 'Beale':
                        f.write('Funcion=beale\n')
                    elif func.get() == 'Esfera':
                        f.write('Funcion=sphere\n')
                    elif func.get() == 'Goldstein':
                        f.write('Funcion=gold\n')
                label.config(text='Listo!')
                pso.pso_anim()

            else:
                label.config(text='Parametros no validos')


        boton = tk.Button(params_f, text="Ejecutar PSO",command=ejecutar_pso)
        boton.grid(row=10,columnspan=2)
        label = tk.Label(params_f)
        label.grid(row=10, column=0)
        label.config(padx=10, pady=10)

        label = tk.Label(params_f)
        label.grid(row=11, column=0)
        label.config(padx=10, pady=10)





    def salir(self):
        sys.exit()







def main():
    app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
