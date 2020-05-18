import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1. / np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """Actor (Policy) Model."""
        
    def __init__(self, state_size, action_size, seed, fc1_units=400, fc2_units=300):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.bn0 = nn.BatchNorm1d(state_size)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.bn1 = nn.BatchNorm1d(fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)
        self.reset_parameters()
        
        print("[MODEL INFO] Actor initialized with parameters : state_size={} action_size={} seed={} fc1_units={} fc2_units={}".format(state_size, action_size, seed, fc1_units, fc2_units))

    def forward(self, state):
        """Build an actor (policy) network that maps states -> actions."""
        states = self.bn0(state)
        x = F.relu(self.fc1(state))
        x = self.bn1(x) 
        x = F.relu(self.fc2(x))
        return F.tanh(self.fc3(x))

    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
        
class Critic(nn.Module):
    """Critic (Value) Model."""
        
    def __init__(self, state_size, action_size, seed, fcs1_units=400, fc2_units=300):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fcs1_units (int): Number of nodes in the first hidden layer
            fc2_units (int): Number of nodes in the second hidden layer
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        # Defining the first Critic neural network
        self.bn0 = nn.BatchNorm1d(state_size)
        self.fcs1 = nn.Linear(state_size, fcs1_units)
        self.bn1 = nn.BatchNorm1d(fcs1_units)
        self.fc2 = nn.Linear(fcs1_units+action_size, fc2_units)
        self.fc3 = nn.Linear(fc2_units, 1)
        # Defining the second Critic neural network
        self.bn0 = nn.BatchNorm1d(state_size)
        self.fcs4 = nn.Linear(state_size, fcs1_units)
        self.bn1 = nn.BatchNorm1d(fcs1_units)
        self.fc5 = nn.Linear(fcs1_units+action_size, fc2_units)
        self.fc6 = nn.Linear(fc2_units, 1)
        self.reset_parameters()
        
        print("[MODEL INFO] CRITIC initialized with parameters : state_size={} action_size={} seed={} fcs1_units={} fc2_units={}".format(state_size, action_size, seed, fcs1_units, fc2_units))

    def forward(self, state, action):
        """Build a critic (value) network that maps (state, action) pairs -> Q-values."""
        # Forward-Propagation on the first Critic Neural Network
        states = self.bn0(state)
        xs1 = F.relu(self.fcs1(state))
        xs1 = self.bn1(xs1)
        x1 = torch.cat((xs1, action), dim=1)
        x1 = F.relu(self.fc2(x1))
        x1 = self.fc3(x1)
        # Forward-Propagation on the second Critic Neural Network
        xs2 = F.relu(self.fcs4(state))
        xs2 = self.bn1(xs2)
        x2 = torch.cat((xs2, action), dim=1)
        x2 = F.relu(self.fc5(x2))
        x2 = self.fc6(x2)
        return x1, x2
    
    def Q1(self, state, action):
        """Build a critic (value) network that maps (state, action) pairs -> Q-values."""
        # Forward-Propagation on the first Critic Neural Network
        states = self.bn0(state)
        xs1 = F.relu(self.fcs1(state))
        xs1 = self.bn1(xs1)
        x1 = torch.cat((xs1, action), dim=1)
        x1 = F.relu(self.fc2(x1))
        x1 = self.fc3(x1)
        return x1
        
    def reset_parameters(self):
        self.fcs1.weight.data.uniform_(*hidden_init(self.fcs1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
        self.fcs4.weight.data.uniform_(*hidden_init(self.fcs4))
        self.fc5.weight.data.uniform_(*hidden_init(self.fc5))
        self.fc6.weight.data.uniform_(-3e-3, 3e-3)