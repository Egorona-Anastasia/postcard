from graph import *

cellSize = 10 # размер клетки
fieldCellWidth = 30 # ширина поля в клетках
fieldCellHeight = 30 # высота поля в клетках
fieldWidth = cellSize*fieldCellWidth*1.27 # ширина поля, на котором будет экран с клетками; это чтобы рабочее поле не увеличивать
fieldHeight = cellSize*fieldCellHeight*1.15 # высота поля, на котором будет экран с клетками; 1.3 - произвольный параметр

def cellRect(y, x): # функция, которая создаёт квадратную клеточку для поля
  return rectangle((x-1)*cellSize, (y-1)*cellSize, # функция, возвращающая квадрат по координатам двух противоположных углов
                   x*cellSize, y*cellSize)# вычитание x - 1 и y - 1 сделано, чтобы размер клетки всегда оставался 10

def initField(): # создание поля из клеток
  global field, fieldId # глобальные переменные - используются для изменения значения переменной в этой и других функциях
  field = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)] # квадратная матрица 32 * 32 из ячеек с нулями
  fieldId = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)] # квадратная марица 32 * 32 из ячеек с нулями - заготовка поля
  penColor("lightgray") # цвет контура клетки
  brushColor("white") # цвет заливки клетки
  for y in range(1,fieldCellHeight+1): # перебор значений для координаты y 
    for x in range(1,fieldCellWidth+1): # перебор начений для координаты x
       fieldId[y][x] = cellRect(y, x) # вызов функции создания клеточки внутри матрицы ячеек, ячейка матрицы теперь клетка поля
def main(): # основная функция программы
  windowSize(fieldWidth, fieldHeight+35) # размер окна
  canvasSize(fieldWidth, fieldHeight) # размер холста
  initField() # вызов функции для создания поля из клеток
  run() # запуск
main() # запуск основной функции программы
