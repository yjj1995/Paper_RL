# Introduction

## 1.

With the advent of 5G era, the explosive growth of smart devices especially Internet of Things (IoT) devices and intelligent phones promotes the development of applications such as virtual reality/augmented reality(VR/AR).

Users's demand for low (ultra-low) latency high quality services is more prominent than ever.  However,  the computing needs and power consumption of these applications often exceed the computing power and battery capabilities  that lacal mobile devices can provide. 



 [Online learning for offloading and autoscaling in
renewable-powered mobile edge computing]



为了处理这个棘手的难题，近年来出现了多接入边缘计算的新技术，引起了广泛的关注。

In order to deal with such a thorny problem, the novel technology of Multi-access edge computing (MEC) have emerged and caused widespread concern in recent years. 

借助边缘云，部署在蜂窝网络的基站(BS)可以为用户提供云计算功能

通过这样的方法，用户可以将计算密集型任务卸载到附件的MEC服务器进行计算来有效的降低用户设备的能耗和减少计算时延。

With the edge cloud's help, the base station (BS) deployed in the cellular networks can provide cloud-computing capabilities[1_2]. In this way, 

the users can offload the computationally intensive task to the the nearby MEC servers for computing  to effectively reduce the device energy consumption and the computational latency of the tasks. 

虽然MEC将计算转移到边缘云，并利用卸载技术和任务划分显著的提高了性能，但是对于实现更加合理的MEC系统方面依旧存在着一些挑战。首先，由于MEC服务器的计算资源有限，因此当多个用户请求卸载的时候，合理的计算资源分配十分必要；其次，在通信频繁的时代，不仅计算资源不足，而且信道等无线电资源也受到限制，如何利用有限的通信资源来传输更多的任务十分重要；因此，在MEC系统中, 对于资源分配和卸载决策的优化是提高系统的能量效率的关键因素。

Although MEC transfers the computations to the edge cloud and uses offloading techniques and task partitioning to significantly enhance the performance， there are still some challenges in achieving more reasonable MEC system.  

On the one hand, for multi-access edge system, due to the limited computing resources of MEC server, reasonable computing resource allocation is critical, on the another hand,  in an era of developed communications, not only the lack of computing resources such as channels are also limited, so how to utilize a limited communication resource to transfer more tasks is very important.  Therefore, optimization of resource allocation and offload decisions is a key factor to improve the energy efficiency in MEC system. 

为了降低MEC系统的能耗，目前大量的工作都是联合优化卸载决策和资源分配。

Recently, in order to reduce the energy consumpition of  the MEC system, a great deal of existing works focus on  jointly optimizing offloading decision and resource allocation. 



In [Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing],

作者采用了博弈论方法以分布式的方式解决了在多信道无线干扰环境下多接入边缘系统中的多用户计算卸载问题。

the authors adopt a game theoretic approach to solve the multi-user compution offloading problem in a multi-channel  wireless interference enviroment.

但是以上对MEC系统中联合优化卸载策略和资源分配的工作，











## 2.

为了提高MEC系统中能量效率，降低系统的能源消耗，所以对于MEC服务器和移动设备之间的无线电资源和计算资源的分配尤为关键，其中无线电资源影响着传输过程中的数据速率和能耗，而计算资源则决定了计算时间。

[5]Joint subcarrier and CPU time allocation for mobile edge computing

最近，针对卸载决策和资源优化的联合优化已经有了大量研究。

在

[6] Multiuser joint task offloading and resource optimization in proximate clouds

中， 作者针对多用户的场景，以最小化能耗为目的，优化了卸载策略和计算资源分配。



在 

[7]  Energy efficient computation offloading for multi-access mec enabled small cell networks

中，作者利用遗传算法解决了小型蜂窝网络中的卸载和资源分配的联合优化问题。

在

[8]  Offloading in mobile edge computing: Task allocation and computational frequency scaling 

中，作者通过共同就考虑任务分配决策和移动设备的CPU频率来优化单个移动设备的能耗。

## 3

在5G时代，无线电资源十分充足，为了提高无线电资源的利用率， 作为5G网络的主要通道访问技术，orthogonal frequency division multiple access (OFDMA)  的方法被广泛的运用到了MEC系统中用户设备和MEC服务器的无线通信上来。

在

[9] 

Energy-Efficient Joint Offloading and Wireless Resource Allocation Strategy in Multi-MEC Server Systems

中，作者考虑了一种基于OFDMA的多用户系统，对其中的任务分流策略和无线资源分配提出了双层优化方法。

在

[10]

Joint Subcarrier and Power Allocation for OFDMA Based Mobile Edge Computing
System

中， 作者研究了在基于OFDMA的MEC系统中的子载波和功率分配问题，目的是最小化系统的延迟，提高用户的体验。

## 4

上面提到的工作大多数都是集中在能量和资源约束下提高能量效率，或者是减少系统延迟，但是没有考虑用户任务对于时延的约束，同时也忽略了用户设备和MEC服务器的并行计算，即部分卸载方案。因此，我们针对这些问题，提出了在用户任务时延和MEC计算资源约束下的部分卸载以及资源分配策略（ORAS），该策略可以联合优化用户的卸载策略以及分配无线和计算资源，从而降低整个系统的能量消耗。

 However, due to the NP-hard features and nonconvexity of the joint problem, the optimal solution is difficult to obtain. So we propose an efficient iterative algorithm to find the optimal offloading and resource allocation strategy. More detailed instructions, The computing resource allocation strategy, the subcarrier allocation strategy, and the offload ratio are found in an alternating manner, and then the optimal solution is found through iteration. Numerical results show that the proposed algorithm is superior to traditional algorithms 











1，介绍MEC

2，提出优化能源消耗的论文。

3，进一步的OFMDA的出现，提高了系统的带宽利用率，引出论文。

4，提出他们的缺点，没有考虑时间延迟和部分协助的联合优化。

5，介绍我们的论文，将有点提出来

6, 展望，从实验可以看出，我们之后会对传输功率进行优化。













