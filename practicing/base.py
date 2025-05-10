from abc import ABC

class Base(ABC):
  
  def initialize(self):
    raise NotImplementedError("initialize method is not implemented")
  
  def visualize(self):
    raise NotImplementedError("visualize method is not implemented")

  def update(self):
    raise NotImplementedError("update method is not implemented")
