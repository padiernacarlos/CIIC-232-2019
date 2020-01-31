import matplotlib
matplotlib.rcParams['backend'] = 'TkAgg'
import tkinter as tk
import sys
import os
from PIL import ImageTk, Image
import pso_python.test_functions as tfun
import pso_python.pso_anim as panim
from tkinter import filedialog
import tkinter.ttk
from preprocesamiento.csv2libsvm import make_libsvm
from preprocesamiento.validate_gram_matrix import validate


class Aplicacion:
    def __init__(self):
        # ---------------------VENTANA PRINCIPAL--------------------------------
        self.root=tk.Tk()
        self.root.title('DCI-NET FRAMEWORK')
        self.root.geometry('800x500')
        self.base = tk.Frame()
        self.base.pack(expand=True)
        # ----------------------------------------------------------------------
        # ------------------------FRAMES----------------------------------------
        self.main_frame = MainFrame(self.base,os.getcwd())
        self.pso_frame = PsoFrame(self.base,os.path.join(os.getcwd(),'pso_python'))
        self.pre_frame = PreprocessingFrame(self.base,os.path.join(os.getcwd(),'preprocesamiento'))
#         self.abr_frame = ABRFrame(self.base,os.path.join(os.getcwd(),'ABR'))
#         self.working_frame = WorkingFrame(self.base,os.getcwd())
        self.main_frame.frm.pack(expand=True)
#
#         # ----------------------------------------------------------------------
#         # ------------------------ MENUS----------------------------------------
#
        self.main_menu = tk.Menu(self.root)

        self.mn_metaheuristicas = tk.Menu(self.main_menu,tearoff=False)
        self.mn_preprocessing = tk.Menu(self.main_menu,tearoff=False)
#         self.mn_ann = tk.Menu(self.main_menu)
#         self.mn_segm_imag = tk.Menu(self.main_menu)
#
        self.main_menu.add_command(label='Pagina principal', \
        command=self.func_wrapper(self.main_frame.show))
        # METAHEURISTICAS
        self.mn_metaheuristicas.add_command(label='PSO', command=self.func_wrapper(self.pso_frame.show))
        self.main_menu.add_cascade(label='Metaheuristicas', menu=self.mn_metaheuristicas)
        # PREPROCESAMIENTO
        self.main_menu.add_command(label='Preprocesamiento', \
        command=self.func_wrapper(self.pre_frame.show))
#         # REDES NEURONALES
#         self.mn_ann.add_command(label='Señales ABR', command=self.func_wrapper(self.abr_frame.show))
#         self.main_menu.add_cascade(label='Redes Neuronales', menu=self.mn_ann)
#         # SEGMENTACION DE IMAGENES
#         self.mn_segm_imag.add_command(label='U-net',command=self.func_wrapper(self.working_frame.show))
#         self.main_menu.add_cascade(label='Segmentacion de imagenes', menu=self.mn_segm_imag)
#
        self.main_menu.add_command(label='Salir', command=self.salir)
        # ----------------------------------------------------------------------
        self.root.config(menu=self.main_menu)
        self.root.mainloop()
#
#
#
    # Funciones varias
    def clear_window(self):
        for child in self.base.winfo_children():
            child.pack_forget()

    def func_wrapper(self,opcion):
        return lambda:[self.clear_window(),opcion()]

    def salir(self):
        sys.exit()

class GeneralFrame:
    def __init__(self,master,dir):
        self.frm = tk.Frame(master)
        self.frm.columnconfigure(0, weight=1)
    def hide(self):
        self.frm.pack_forget()
    def show(self):
        self.frm.pack(expand=True)
    def read_descripcion(self,dir):
        d_dir = os.path.join(dir,'descripcion.txt')
        with open(d_dir) as f:
            return f.read()
class MainFrame(GeneralFrame):
    def __init__(self,master,dir):
        super().__init__(master,dir)
        self.path = os.path.join(os.getcwd(),os.path.join('imgs','logo2.png'))
        self.img = ImageTk.PhotoImage(Image.open(self.path))
        self.logo = tk.Label(self.frm, image = self.img)
        self.saludo = tk.Label(self.frm, text = 'Somos DCI-NET')
        self.logo.grid(row=0,column=0)
        self.saludo.grid(row=1,column=0)
        self.saludo.config(font=('Times New Roman', 16))
class PsoFrame(GeneralFrame):
    def __init__(self,master,dir):
        super().__init__(master,dir)
        # Titulo
        self.titulo = tk.Label(self.frm, text='Parámetros PSO')
        self.titulo.grid(row=0, column=0)
        self.titulo.config(font=('Times New Roman', 16))
        # Numero de Particulas
        self.l_np = tk.Label(self.frm, text='Número de Partículas')
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
        self.l_wmx = tk.Label(self.frm, text='Inercia máxima')
        self.l_wmx.grid(row=4, column=0)
        self.l_wmx.config(padx=10, pady=10)
        self.wmx_cuadro=tk.Entry(self.frm)
        self.wmx_cuadro.insert(tk.END, 0.9)
        self.wmx_cuadro.grid(row=4, column=1)
        # W_min
        self.l_wmn = tk.Label(self.frm, text='Inercia mínima')
        self.l_wmn.grid(row=5, column=0)
        self.l_wmn.config(padx=10, pady=10)
        self.wmn_cuadro=tk.Entry(self.frm)
        self.wmn_cuadro.insert(tk.END, 0.4)
        self.wmn_cuadro.grid(row=5, column=1)
        # Numero de iteraciones
        self.l_mxi = tk.Label(self.frm, text='Número máximo de iteraciones')
        self.l_mxi.grid(row=6, column=0)
        self.l_mxi.config(padx=10, pady=10)
        self.mxi_cuadro=tk.Entry(self.frm)
        self.mxi_cuadro.insert(tk.END, 50)
        self.mxi_cuadro.grid(row=6, column=1)
        # Angulo azimutal
        self.l_az = tk.Label(self.frm, text='Ángulo azimutal')
        self.l_az.grid(row=7, column=0)
        self.l_az.config(padx=10, pady=10)
        self.az_cuadro=tk.Entry(self.frm)
        self.az_cuadro.insert(tk.END, 30)
        self.az_cuadro.grid(row=7, column=1)
        # Nivel de elevacion
        self.l_ele = tk.Label(self.frm, text='Nivel de elevación')
        self.l_ele.grid(row=8, column=0)
        self.l_ele.config(padx=10, pady=10)
        self.ele_cuadro=tk.Entry(self.frm)
        self.ele_cuadro.insert(tk.END, 30)
        self.ele_cuadro.grid(row=8, column=1)
        # Funcion
        self.l_f = tk.Label(self.frm, text='Función a evaluar')
        self.l_f.grid(row=9, column=0)
        self.l_f.config(padx=10, pady=10)
        self.func = tk.StringVar(None)
        self.f_cuadro = tk.OptionMenu(self.frm,self.func,"Beale", "Esfera",
                                    "Goldstein","Rastrigin","Ackley","Rosenbrock")
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
            if self.func.get() == 'Beale':
                lims = {'x0':[-4.5,4.5],'x1':[-4.5,4.5]}
                func = tfun.beale
            elif self.func.get() == 'Esfera':
                lims = {'x0':[-10,10],'x1':[-10,10]}
                func = tfun.sphere
            elif self.func.get() == 'Goldstein':
                lims = {'x0':[-2,2],'x1':[-2,2]}
                func = tfun.gold
            elif self.func.get() == 'Ackley':
                lims = {'x0':[-5,5],'x1':[-5,5]}
                func = tfun.auckley
            elif self.func.get() == 'Rosenbrock':
                lims = {'x0':[-10,10],'x1':[-10,10]}
                func = tfun.rosenbrock
            elif self.func.get() == 'Rastrigin':
                lims = {'x0':[-5.12,5.12],'x1':[-5.12,5.12]}
                func = tfun.rastrigin
            self.label.config(text='Listo!')
            panim.pso_anim(np,w_max,w_min,max_iter,c1,
                            c2,azim,ele,lims,func,self.func.get())




        else:
            self.label.config(text='Parametros no validos')

class PreprocessingFrame(GeneralFrame):
        def __init__(self,master,dir):
            super().__init__(master,dir)
            csv2libd = ("Al pulsar este botón se te pedirá\n"
                        " seleccionar un archivo en formato\n"
                        " csv y se guardará el mismo archivo\n"
                        "en formato libsvm")
            valmatd = ("Al pulsar este botón se "
                        "validará\n que la matriz gramiana"
                        " este correcta")
            self.filename = ''

            self.csv2lib = tk.Label(self.frm, text = 'Formato csv a libsvm')
            self.csv2lib.grid(row=0,column=0,padx=20,pady=5)
            self.csv2lib.config(font=('Times New Roman', 16))
            self.csv2libd = tk.Label(self.frm, text = csv2libd)
            self.csv2libd.grid(row=1,column=0,padx=20,pady=20)
            self.csv2libd.config(font=('Times New Roman', 12))
            self.valmat = tk.Label(self.frm, text = 'Validar matriz gramiana')
            self.valmat.grid(row=0,column=1,padx=20,pady=5)
            self.valmat.config(font=('Times New Roman', 16))
            self.valmatd = tk.Label(self.frm, text = valmatd)
            self.valmatd.grid(row=1,column=1,padx=20,pady=20)
            self.valmatd.config(font=('Times New Roman', 12))
            self.csv_button = tk.Button(self.frm, text="Escoger archivo",
                                        command=self.get_file)
            self.csv_button.grid(row=2, column=0, padx=10, pady=10)
            self.filen = tk.Label(self.frm, text = '')
            self.filen.grid(row=3,column=0,padx=20,pady=5)
            self.filen.config(font=('Times New Roman', 11))
            self.csv2libd_idx = tk.Label(self.frm, text = 'Índice donde se encuentran etiquetas')
            self.csv2libd_idx.grid(row=4,column=0,padx=20,pady=2)
            self.csv2libd_idx.config(font=('Times New Roman', 10))
            self.idx_cuadro=tk.Entry(self.frm)
            self.idx_cuadro.insert(tk.END,'')
            self.idx_cuadro.grid(row=5, column=0)
            self.conv_button = tk.Button(self.frm, text="Convertir",
                                        command=self.convertir)
            self.conv_button.grid(row=6, column=0, padx=10, pady=10)
            self.res_label = tk.Label(self.frm, text = '')
            self.res_label.grid(row=7,column=0,padx=20,pady=5)
            self.res_label.config(font=('Times New Roman', 11))

            self.gmat_button = tk.Button(self.frm, text="Escoger dataset",
                                        command=self.get_dir)
            self.gmat_button.grid(row=2, column=1, padx=10, pady=10)
            self.dirnamen = tk.Label(self.frm, text = '')
            self.dirnamen.grid(row=3,column=1,padx=20,pady=5)
            self.dirnamen.config(font=('Times New Roman', 11))
            self.kernel = tk.StringVar(None)
            self.k_cuadro = tk.OptionMenu(self.frm,self.kernel,"Hermite", "Gegenbauer", "Linear","RBF")
            self.k_cuadro.grid(row=4, column=1)
            # self.csv2libd = tk.Label(self.frm, text = 'Índice donde se encuentran etiquetas')
            # self.csv2libd.grid(row=4,column=0,padx=20,pady=2)
            # self.csv2libd.config(font=('Times New Roman', 10))
            # self.idx_cuadro=tk.Entry(self.frm)
            # self.idx_cuadro.insert(tk.END,'')
            # self.idx_cuadro.grid(row=5, column=0)
            self.val_button = tk.Button(self.frm, text="Validar",command=self.validar)#,
                                        #command=self.convertir)
            self.val_button.grid(row=6, column=1, padx=10, pady=10)
            self.res_vlabel = tk.Label(self.frm, text = '')
            self.res_vlabel.grid(row=7,column=1,padx=20,pady=5)
            self.res_vlabel.config(font=('Times New Roman', 11))

            self.dirname = ''
            self.ds = ''


        def get_file(self):
            self.filename =  filedialog.askopenfilename(initialdir = "C:\\",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            self.filen.config(text=os.path.relpath(self.filename))

        def get_dir(self):
            self.dirname = filedialog.askdirectory(title = 'Choose the directory of the dataset')
            self.ds = os.path.basename(self.dirname)
            self.dirnamen.config(text=self.ds.capitalize())#os.path.relpath(self.dirname))


        def convertir(self):
            flag = True
            try:
                idx = int(self.idx_cuadro.get())
            except ValueError:
                flag = False

            pre, ext = os.path.splitext(self.filename)


            if ext != '.csv':
                flag = False


            if flag:
                make_libsvm(self.filename, idx)
                self.res_label.config(text='Listo')

            else:
                self.res_label.config(text='Parámetros no válidos')

        def validar(self):
            flag = True
            if not self.dirname:
                flag = False
            if not self.kernel.get():
                flag = False

            if flag:
                newwin = tk.Toplevel(self.frm)


                validate(self.dirname,self.kernel.get(),self.ds, newwin)
                self.res_vlabel.config(text='Listo')

            else:
                self.res_vlabel.config(text='Parámetros no válidos')


# class WorkingFrame(GeneralFrame):
#     def __init__(self,master,dir):
#         super().__init__(master,dir)
#         self.path = os.path.join(os.getcwd(),'imgs/working.png')
#         self.img = ImageTk.PhotoImage(Image.open(self.path))
#         self.logo = tk.Label(self.frm, image = self.img)
#         self.saludo = tk.Label(self.frm, text = 'Aun estamos trabajando en esta opcion')
#         self.logo.grid(row=0,column=0)
#         self.saludo.grid(row=1,column=0)
#         self.saludo.config(font=('Times New Roman', 16))
# class ABRFrame(GeneralFrame):
#     def __init__(self,master,dir):
#         super().__init__(master,dir)
#         # Titulo
#         self.titulo = tk.Label(self.frm, text='Señales ABR')
#         self.titulo.grid(row=0, column=0)
#         self.titulo.config(font=('Times New Roman', 16))
#         self.descripcion = tk.Label(self.frm,text=self.read_descripcion(dir))
#         self.descripcion.grid(row=1, column=0)
#         self.descripcion.config(font=('Times New Roman', 14))
#         self.boton = tk.Button(self.frm, text="Ejecutar",command=self.ejecutar_abr)
#         self.boton.grid(row=2,columnspan=2)
#         self.boton2 = tk.Button(self.frm, text="Mostrar resultados",command=self.mostrar_resultados)
#         self.boton2.grid(row=3,columnspan=2)
#     def ejecutar_abr(self):
#         print('Prueba')
#     def mostrar_resultados(self):
#         print('Prueba 2')
#
#
#
if __name__ == '__main__':
    Aplicacion()
