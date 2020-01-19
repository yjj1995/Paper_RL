# Introduction_2

## 1.

 With the advent of 5G era, the explosive growth of smart devices especially Internet of Things (IoT) devices and intelligent phones promotes the development of applications such as virtual reality/augmented reality(VR/AR). This leads to Users’s demand for low (ultra-low) latency high quality services is more prominent than ever. However, the computing needs and power consumption of these applications often exceed the computing power and battery capabilities that lacal mobile devices can provide [1]. 

## 1.改

With the rapid development of Internet of Things (IoT),  the explosive growth of   various new applications(e.g., virtual reality, augmented reality, autonomous driving). Users’s demand for low (ultra-low) latency high quality services is more prominent than ever. However, due to the limited computing power and storage capacity of the user equipment, the user service requirements cannot be well satisfied, and power consumption of these applications often exceed battery capabilities that lacal mobile devices can provide [1]. 

In order to deal with such a thorny problem,  the new technology of Multi-access edge computing (MEC) have emerged in recent years, which caused widespread concern. MEC pushed the cloud services down to the vicinity of MDs located at the edge of network, the base station (BS) deployed in the cellular networks can provide cloud-computing capabilities  [2] [3]. The users can offload the computationally intensive task to the the nearby MEC servers for computing to effectively reduce the device energy consumption and the computational latency of the tasks. 

However, even if MEC transfers the computations to the edge cloud  cloud and uses offloading techniques and task partitioning to significantly enhance the performance, there are still some challenges in achieving more reasonable MEC system. On the one hand, for multi-access edge system, due to the limited computing resources of MEC server, reasonable computing resource allocation is critical. On the another hand, in an era of developed communications, not only the lack of computing resources such as channels are also limited, so how to utilize a limited communication resource to transfer more tasks is very important. Therefore, jointly optimizing resource allocation and offloading decision is a key factor to improve MEC system performance. 



## 引用文献



[5] 加权和的最小

作者提出了一种低复杂度次优算法共同优化，以最小化执行延迟和设备能耗的加权和。











In rencent years, there are many joint research on the offloading decisions and resource allocation in the MEC system. [5] [6]

 [5] Y. Mao, J. Zhang, and K. B. Letaief, “Joint task offloading scheduling and transmit power allocation for mobile-edge computing systems,” in IEEE Wireless Commun. and Netw. Conf. (WCNC), pp. 1–6, 2017. 

[6] N. Janatian, I. Stupia, and L. Vandendorpe, “Optimal resource allocation in ultra-low power fog-computing SWIPT-based networks,” in IEEE Wireless Commun. and Netw. Conf. (WCNC), pp. 1–6, 2018 

[5] [6] studied the optimization problem in single-user MEC systems. 

Mao at all, [5]研究了单用户MEC系统中的联合任务卸载调度和发射功率分配问题。
Janatian, [6]研究了基于超低功耗雾计算交换的同时基于无线信息和功率传输（SWIPT）的单用户MEC系统中的资源分配。

 For multiuser scenarios,  

[7] Energy Efficient Dynamic Offloading in Mobile Edge Computing for Internet of Things ,

 In this paper, we study the energy efficient task offloading in MEC. Specifically, we formulate it as a stochastic optimization problem, with the objective of minimizing the energy consumption of task offloading while guaranteeing the average queue length. 

[8]

 Energy Efficient and Low Delay Partial Offloading Scheduling and Power Allocation for MEC 

 In this paper, we investigate the problem of partial offloading scheduling and resource allocation for mobile edge computing systems with multiple independent tasks. Our goal is to minimize the weighted sum of the execution delay and energy consumption while guaranteeing the transmission power constraints of the tasks. The execution delay of tasks running in MEC and mobile edge devices are both considered. The energy consumption of both the tasks computing and task data transmission are considered as well. 

[9]Joint Computation Offloading and Resource Allocation for Min-Max Fairness in MEC Systems

 In this paper, we consider the joint computation offloading and resource allocation problem for an uplink MEC system under the min-max fairness criterion.  

In the meantime, in order to improve the utilization of radio resources, as the main channel access technology of 5G networks, the method of orthogonal frequency division multiple access (OFDMA) is widely applied to communication between user equipments and MEC servers in the MEC system. In [7], the author considers a multi-user system based on OFDMA, and proposes a bi-level optimization method of task shunting strategy and radio resource allocation. In [8], the authors studied subcarrier and power allocation issues in OFDMA-based MEC systems with the goal of minimizing system latency and improving user experience. Most of the work mentioned above only considers reducing system energy consumption or user delay under resource constraints. However, the sensitivity of the user task to time is not considered, and the collaborative computing of the user equipment and the MEC server is also ignored, that partial offloading scheme. We propose a partial offload and resource allocation strategy that includes task time constraints. However, due to the NPhard features and nonconvexity of the joint problem, the optimal solution is difficult to obtain. So we propose an efficient iterative algorithm to find the optimal offloading and resource allocation strategy. More detailed instructions, The computing resource allocation strategy, the subcarrier allocation strategy, and the offload ratio are found in an alternating manner, and then the optimal solution is found through iteration. Numerical results show that the proposed algorithm is superior to traditional algorithms. The rest of this paper is organized as follows. In section II, we described the system model and formulated the original problem. In section III, we introduce our proposed alogrithms. Simulation results are showed in section IV . Finally, we conclude the article in section V . 