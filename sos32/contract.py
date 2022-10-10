from sos32.slot import Slot
from prettytable.colortable import ColorTable, Themes

class Contract:
    def __init__(self, state_variables) -> None:
        self.state_variables = state_variables
        self.slots = []
        self.isOptimized = False
        self.next_optimal_position = 0
        self.init_slot_amount = max([int(var.slot) for var in self.state_variables]) + 1
        
    def optimize_storage(self):
        i = 0
        while ([var for var in self.state_variables if var.isStored is not True]):
            slot = Slot(i, self)
            slot.optimize_slot()
            self.slots.append(slot)
            i+=1
        self.isOptimized = True
        
    def show_results(self):
        x = ColorTable(theme=Themes.DEFAULT)
        x.field_names = ["Name", "Type", "Slot", "Slot Size", "Bytes"]
        for slot in self.slots:
            for var in slot.state_variables:
                x.add_row([var.name, var.label, slot.slot_id, slot.size, var.numberOfBytes])
        print(x)
        print("Without SOS32:", self.init_slot_amount, "slots")
        print("With SOS32:", len(self.slots),"slots")