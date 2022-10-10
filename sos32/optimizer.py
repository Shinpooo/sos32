import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# import os
# os.environ["NEOS_EMAIL"] = ""


class Optimizer:
    def __init__(self, stateVars) -> None:
        self.model = pyo.ConcreteModel()
        self.stateVars = stateVars
        self.storages_variables = [int(state_var.numberOfBytes) for state_var in self.stateVars]
        self.model.StateVariableSet = pyo.RangeSet(0, len(self.storages_variables)-1)
        
    def createModel(self):
        self._createParams()
        self._createVariables()
        self._createConstraints()
        self._createObjective()

    def _createParams(self):
        self.model.s = pyo.Param(self.model.StateVariableSet, initialize={i: s for (i, s) in zip(
            self.model.StateVariableSet, self.storages_variables)})
        
    def _createVariables(self):
        self.model.X = pyo.Var(self.model.StateVariableSet, within=pyo.Binary)
        
    def _createConstraints(self):
        def C(model):
            return sum(model.X[i] * model.s[i] for i in model.StateVariableSet) <=  32

        self.model.C = pyo.Constraint(rule=C, doc='Max Slot Size')
        
    def _createObjective(self):
        def slot_size(model):
            return sum(model.X[i] * model.s[i] for i in model.StateVariableSet)
        
        self.model.objFct = pyo.Objective(rule=slot_size, sense=pyo.maximize)
        # self.model.objFct.pprint()
        
    def solve(self):
        # solver_manager = pyo.SolverManagerFactory('neos')
        # results = solver_manager.solve(self.model, opt="cbc")
        solver_manager = pyo.SolverFactory('glpk')
        results = solver_manager.solve(self.model)
        # results.write()
        variables = [pyo.value(self.model.X[i]) for i in self.model.X]
        packedStateVars = [self.stateVars[idx] for idx,i in enumerate(variables) if i == 1]
        return packedStateVars