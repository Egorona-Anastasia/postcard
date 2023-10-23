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
def changeField(clear = False): # изменение поля; параметр clear - очищение; поле не очищено
  newField = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)] # создаётся заготовка нового поля
  if not clear: # если поле не очищено
    for y in range(1,fieldCellHeight+1):
      for x in range(1,fieldCellWidth+1):
        count = - field[y][x] # изначально равно 0, но потом значение меняется
        for i in range(-1,2):
          for j in range(-1,2):
            if field[y+i][x+j]: count += 1
        if (field[y][x] == 1 and count == 2) or count == 3:
          newField[y][x] = 1
  for y in range(1,fieldCellHeight+1):
    for x in range(1,fieldCellWidth+1):
      if newField[y][x] != field[y][x]:
        toggleCell(x, y)

def toggleCell(x, y): # переключение цвета клетки
  field[y][x] = 1 - field[y][x]
  if field[y][x]:
    changeFillColor(fieldId[y][x], "black" ) # встроенная функция, меняющая цвет клетки
  else:
    changeFillColor(fieldId[y][x], "white") # встроенная функция, меняющая цвет клетки
def cellCoords(x, y): # координаты клетки
  x = x // cellSize + 1
  y = y // cellSize + 1
  return (x, y)

prevCell = (-1,-1) # предыдущая клетка
# функции обработки событий:
def mouseClick(event): # функция клика мыши, принимает на вход объект события - event
  global prevCell
  mouseLBMove(event)
  prevCell = (-1,-1)
  return
def mouseLBMove(event): # функция нажатия с передвижением мыши, принимает на вход объект события - event
  global prevCell
  x, y = cellCoords(event.x, event.y) # отслеживание координаты мыши, в функцию получения координат передаются координаты мыши
  if (x,y) != prevCell:
    toggleCell(x, y) # меняется цвет ячейки
    prevCell = (x, y) # меняется предыдущее значение ячейки
  return

def main(): # основная функция программы
  windowSize(fieldWidth, fieldHeight+35) # размер окна
  canvasSize(fieldWidth, fieldHeight) # размер холста
  e = edit("Введите пожелание: ", 80, 50, font=("Arial", 10), justify = CENTER)
  print(e.text.get())
  initField() # вызов функции для создания поля из клеток
  onMouseClick(mouseClick, 1) # запуск обработки события нажатия мыши
  onMouseButtonMove(mouseLBMove, 1) # запуск обработки события нажатия и передвижения мыши
  run() # запуск
main() # запуск основной функции программы
