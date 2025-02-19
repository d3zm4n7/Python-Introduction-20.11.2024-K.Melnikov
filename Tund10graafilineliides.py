import numpy as np # diapozon znachenij x=[min,max]
import matplotlib.pyplot as plt #

#Ülesanne 1
def Vaal(color:str):
    x1=np.arange(0,10,1) #0,1,2,3,4,5,6,7,8,9
    y1=(2/27)*x1**2-3

    x2=np.arange(-10, 0.5,0.5)
    y2=0.04*x2**2-3

    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+6

    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6

    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2

    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5

    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6

    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3

    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)

    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)

    # sodaem rabochee prostranstvo dlja grafika
    plt.figure(facecolor="lightgreen") #cvet dlya figury
    plt.title("Vaal") #nazvanie figury
    plt.ylabel("Y") #Y
    plt.xlabel("X") #X
    plt.grid(True) #setka na pole

    ax=plt.axes()
    ax.set_facecolor("green")

    #colors=["c","m","y","k","r","g","b","w","w","w"]
    for i in range(1,11):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),color[0]+"-*") #colors[i-1]+"-*") #plt.plot(x1,y1,"b:o") x2...x10
    plt.show()



def prillid(color):
    # ?????????? ?????????? ?????
    x1 = np.arange(-9, -1, 1) #     x1 = np.linspace(-9, -1, 100) - gde 100 eto kolichestvo tochek
    y1 = -1/16*(x1+5)**2 + 2

    x2 = np.arange(1, 9, 1)
    y2 = -1/16*(x2-5)**2 + 2  

    x3 = np.arange(-9, -1, 1)
    y3 = 1/4*(x3+5)**2 - 3

    x4 = np.arange(1, 9, 1)
    y4 = 1/4*(x4-5)**2 - 3

    x5 = np.arange(-9, -6, 0.5)
    y5 = -(x5+7)**2 + 5

    x6 = np.arange(6, 9, 0.5)
    y6 = -(x6-7)**2 + 5

    x7 = np.arange(-1, 1, 0.5)
    y7 = -0.5*x7**2 + 1.5

    # ?????? ??? ?????? ? ???????
    x_vals = [x1, x2, x3, x4, x5, x6, x7]
    y_vals = [y1, y2, y3, y4, y5, y6, y7]

    colors = ["c", "m", "y", "k", "r", "g", "b"]

    # ?????? ??????
    plt.figure(facecolor="white")
    plt.title("???? (Prillid)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    for i in range(7):  # ??????????: 7 ????? ?????? 10
        plt.plot(x_vals[i], y_vals[i], color + "-*")

    plt.show()



# def prillid():
#     # ?????????? ?????????? ?????
#     x1 = np.linspace(-9, -1, 100)
#     y1 = -1/16*(x1+5)**2 + 2

#     x2 = np.arange(1, 9, 1)
#     y2 = -1/16*(x2-5)**2 + 2  # ?????????? x2 ?????? x1

#     x3 = np.arange(-9, -1, 1)
#     y3 = 1/4*(x3+5)**2 - 3

#     x4 = np.arange(1, 9, 1)
#     y4 = 1/4*(x4-5)**2 - 3

#     x5 = np.arange(-9, -6, 0.5)
#     y5 = -(x5+7)**2 + 5

#     x6 = np.arange(6, 9, 0.5)
#     y6 = -(x6-7)**2 + 5

#     x7 = np.arange(-1, 1, 0.5)
#     y7 = -0.5*x7**2 + 1.5

#     # ?????? ??? ?????? ? ???????
#     x_vals = [x1, x2, x3, x4, x5, x6, x7]
#     y_vals = [y1, y2, y3, y4, y5, y6, y7]

#     colors = ["c", "m", "y", "k", "r", "g", "b"]

#     # ?????? ??????
#     plt.figure(facecolor="white")
#     plt.title("???? (Prillid)")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.grid(True)

#     for i in range(7):  # ??????????: 7 ????? ?????? 10
#         plt.plot(x_vals[i], y_vals[i], colors[i] + "-*")

#     plt.show()

# prillid()



