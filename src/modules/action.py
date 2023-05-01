




class Action :
    
  def __init__(self) -> None:
    pass

  def do(self)-> bool :
    pass



class MoveArrow(Action) : 

  def __init__(self, arrow: str)->None :
<<<<<<< HEAD
    super()__init__()
=======
    super().__init__()
>>>>>>> main
    self.arrow = arrow

  def do(self)->bool :
    print('[x] - MOVING WITH ARROW')
    return False



class MoveCoords(Action) : 

  def __init__(self, x: int,y:int)->None :
<<<<<<< HEAD
    super()__init__()
=======
    super().__init__()
>>>>>>> main
    self.x = x
    self.y = y

  def do(self)->bool :
    return False



  

    






character = Character()
character.execute_Action(MoveArrow("Left"))
character.execute_Action(MoveCoords(45,34))
<<<<<<< HEAD
character.execute_Action(Action("Recole Ble"))
=======
character.execute_Agitction(Action("Recole Ble"))
>>>>>>> main

character.execute_strategy([MoveArrow("Left")])
character.execute_strategy([MoveArrow("Left"),MoveArrow("Right"),MoveArrow("Top"),MoveArrow("Left")])