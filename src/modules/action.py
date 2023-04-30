




class Action :
    
  def __init__(self) -> None:
    pass

  def do(self)->bool :
    pass



class MoveArrow(Action) : 

  def __init__(self, arrow: str)->None :
    super()__init__()
    self.arrow = arrow

  def do(self)->bool :
    print('[x] - MOVING WITH ARROW')
    return False



class MoveCoords(Action) : 

  def __init__(self, x: int,y:int)->None :
    super()__init__()
    self.x = x
    self.y = y

  def do(self)->bool :
    return False



  

    






character = Character()
character.execute_Action(MoveArrow("Left"))
character.execute_Action(MoveCoords(45,34))
character.execute_Action(Action("Recole Ble"))

character.execute_strategy([MoveArrow("Left")])
character.execute_strategy([MoveArrow("Left"),MoveArrow("Right"),MoveArrow("Top"),MoveArrow("Left")])