from sos32.optimizer import Optimizer

class Slot:
    def __init__(self, slot_id, contract):
        self.slot_id=slot_id
        self.state_variables=[]
        self.size=0
        self.contract = contract
        
    def optimize_slot(self):
        opti = Optimizer([var for var in self.contract.state_variables if var.isStored is not True])
        opti.createModel()
        packedVars = opti.solve()
        for var in packedVars:
            var.optimal_postion = self.contract.next_optimal_position
            self.contract.state_variables[var.position].optimal_postion = self.contract.next_optimal_position
            var.isStored = True
            self.contract.state_variables[var.position].isStored
            self.contract.next_optimal_position += 1
            
        self.state_variables.extend(packedVars)
        self.size=sum(int(state_var.numberOfBytes) for state_var in self.state_variables)