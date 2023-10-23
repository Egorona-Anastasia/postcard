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
    changeFillColor(fieldId[y][x], color()) # встроенная функция, меняющая цвет клетки
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
# функции цветовых кнопок, вызывают цвета:
def button_1():
  global palette # уникальный номер каждого цвета
  palette = 1
  color()
  
def button_2():
  global palette
  palette = 2
  color()

def button_3():
  global palette
  palette = 3
  color()

def button_4():
  global palette
  palette = 4
  color()

def button_5():
  global palette
  palette = 5
  color()

def button_6():
  global palette
  palette = 6
  color()
  
def button_7():
  global palette
  palette = 7
  color()

def button_8():
  global palette
  palette = 8
  color()
  
def color(): # функция, возвращающая цвет, которым будут рисовать
  if palette == 1:
    return "red"
  elif palette == 2:
    return "orange"
  elif palette == 3:
    return "yellow"
  elif palette == 4:
    return "green"
  elif palette == 5:
    return "deep sky blue"
  elif palette == 6:
    return "blue"
  elif palette == 7:
    return "purple"
  elif palette == 8:
    return "black"
def main(): # основная функция программы
  windowSize(fieldWidth, fieldHeight+35) # размер окна
  canvasSize(fieldWidth, fieldHeight) # размер холста
  # кнопки, выполняющие команду изменения цвета:
  colorBtn_1 = button("", 1,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_1, bg = "red") 
  colorBtn_2 = button("", 30,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_2, bg = "orange")
  colorBtn_3 = button("", 60,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_3, bg = "yellow")
  colorBtn_4 = button("", 90,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_4, bg = "green")
  colorBtn_5 = button("", 120,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_5, bg = "deep sky blue")
  colorBtn_6 = button("", 150,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_6, bg = "blue")
  colorBtn_7 = button("", 180,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_7, bg = "purple")
  colorBtn_8 = button("", 210,
               fieldCellHeight*cellSize + 5, width=2,
               command = button_8, bg = "black")
  e = edit("Введите пожелание: ", 80, 50, font=("Arial", 10), justify = CENTER)
  print(e.text.get())
  initField() # вызов функции для создания поля из клеток
  onMouseClick(mouseClick, 1) # запуск обработки события нажатия мыши
  onMouseButtonMove(mouseLBMove, 1) # запуск обработки события нажатия и передвижения мыши
  run() # запуск
main() # запуск основной функции программы
