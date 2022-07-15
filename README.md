# Deep-Reinforcement-Learning-DDPG-Continuous-Control

[//]: # (Image References)

[imageA]: https://github.com/timwu64/Deep-Reinforcement-Learning-DDPG-Robotic-Arms-Continuous-Control/blob/master/images/Untrained.gif "Untrained Agent"

[imageB]: https://github.com/timwu64/Deep-Reinforcement-Learning-DDPG-Robotic-Arms-Continuous-Control/blob/master/images/Trained.gif "Trained Agent"

[image2]: https://github.com/timwu64/Deep-Reinforcement-Learning-DDPG-Robotic-Arms-Continuous-Control/blob/master/images/image8.gif "Trained Agent2"

[image3]: https://github.com/timwu64/Deep-Reinforcement-Learning-Robotic-Continuous-Control/blob/master/images/crawler_2.png "Crawler 2"

## Introduction

For this project, I will apply RL for 
1. Robootic Arm: Use 20 identical DDPG agents to train to control 2 double-jointed arms to move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.
Before Training:
![Untrained Agent][imageA]

After Training:
![Trained Agent][imageB]

In the real world, there are identical copies of the agent. It has been shown that having multiple copies of the same agent sharing experience can accelerate learning. Shown below:


![Trained Agent2][image2]

2. Robotic Crawler : Use Twin-Delayed DDPG agent to train a 4 Legs Crawler to walk. Shown below:

![Crawler 2][image3]

## Project Starter Code

The original Udacity repo for this project can be found [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p2_continuous-control).

## Getting Started
### Descriptions
- `README.md` describe the environment, along with how to install the requirements.

### Code
- `Continuous_Control.ipynb` control and train a Deep Deterministic Policy Gradients (DDPG) agent
- `ddpg_agent.py` defines the Deep Deterministic Policy Gradients (DDPG) agent
- `model.py` defines the Deep Deterministic Policy Gradients (DDPG) network architecture

### Report
- `Report.pdf` describe the learning algorithm and the details of the implementation, along with ideas for future work.

### The Trained Agent
- `checkpoint_actor.pth` contains the weights for actor network, and `checkpoint_critic.pth` contains the weights for critic network for the Deep Deterministic Policy Gradients (DDPG) implementation (see `Report.pdf` for details)

### Installation
- `python` folder contains the installation dependencies

  Follow the instructions below to explore the environment on your own machine! You will also learn how to use the Python API to control your agent.

  The Step by Step installation example shown below:

1. Clone the DRLND Repository

    If you haven't already, please follow the instructions in the [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. These instructions can be found in README.md at the root of the repository. By following these instructions, you will install PyTorch, the ML-Agents toolkit, and a few more Python packages required to complete the project.

    (For Windows users) The ML-Agents toolkit supports Windows 10. While it might be possible to run the ML-Agents toolkit using other versions of Windows, it has not been tested on other versions. Furthermore, the ML-Agents toolkit has not been tested on a Windows VM such as Bootcamp or Parallels.

2. Download the Unity Environment

    For this project, you will not need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

      - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
      - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
      - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
      - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
      Then, place the file in the p1_navigation/ folder in the DRLND GitHub repository, and unzip (or decompress) the file.

    (For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (To watch the agent, you should follow the instructions to enable a virtual screen, and then download the environment for the Linux operating system above.)

3. Create and activate a new environment with Python 3.6
    
     ###### Linux or Mac:
     
      `conda create --name drlnd python=3.6`
      
      `source activate drlnd`

     ###### Windows:

      `conda create --name drlnd python=3.6`
      
      `activate drlnd`

4. Clone the following repository 

    `git clone https://github.com/udacity/deep-reinforcement-learning.git`

    and start to run the first cell of the  to install all the dependencies

    or you can install the dependencies as below (optional)
   
   `cd ./python`
   
   `pip install .`

### Explore the Environment and Run it
- After you have followed the instructions above, open `Continuous_Control.ipynb` and and follow the instructions to learn how to use the Python API to control the agent.


