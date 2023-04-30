


class Logs :
  def log_error(self,message: str)->None :
    file = open("logs/error.log", "a")
    file.write("\n"+message)
    file.close()

  def log_build(self,message: str)->None :
    file = open("logs/build.log", "a")
    file.write("\n"+message)
    file.close()

  def log_console(self,message: str)->None :
    print(message)
