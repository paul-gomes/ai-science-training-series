import matplotlib.pyplot as plt

#gpu 1

gpu_1 = [[0, 0.930, 0.983],[1, 0.973, 0.980],[2, 0.975, 0.988],[3, 0.979, 0.985],[4, 0.981, 0.989],
       [5, 0.981, 0.989],[6, 0.984, 0.988],[7, 0.983, 0.988],[8, 0.983, 0.990],[9, 0.985, 0.989],
       [10, 0.983, 0.989],[11, 0.986, 0.989],[12, 0.986, 0.990], [13, 0.986, 0.991], [14, 0.986, 0.990],
       [15, 0.986, 0.990]]



plt.plot([i[0] for i in gpu_1], [i[1] for i in gpu_1], lw=0.5, color='b', label='Train accuracy')
plt.plot([i[0] for i in gpu_1], [i[2] for i in gpu_1], lw=0.5, color='r', label='Test accuracy')
plt.title('Accuracy in each epochs (GPU 1)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid()
plt.legend()
plt.show()




#gpu 2
gpu_2 = [[0, 0.902, 0.975],[1, 0.956, 0.984],[2, 0.962, 0.982],[3, 0.965, 0.983],
         [4, 0.966, 0.983],[5, 0.965, 0.985],[6, 0.966, 0.984],[7, 0.966, 0.984],
         [8, 0.966, 0.984],[9, 0.967, 0.984],[10, 0.969, 0.986],[11, 0.969, 0.984],
         [12, 0.967, 0.985],[13, 0.968, 0.985],[14, 0.970, 0.985],[15, 0.968, 0.985]]

plt.plot([i[0] for i in gpu_1], [i[1] for i in gpu_2], lw=0.5, color='b', label='Train accuracy')
plt.plot([i[0] for i in gpu_1], [i[2] for i in gpu_2], lw=0.5, color='r', label='Test accuracy')
plt.title('Accuracy in each epochs (GPU 2)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid()
plt.legend()
plt.show()


#gpu 4
gpu_4 = [[0, 0.620, 0.734],[1, 0.702, 0.747],[2, 0.708, 0.744],[3, 0.711, 0.743],
         [4, 0.712, 0.745],[5, 0.712, 0.746],[6, 0.716, 0.753],[7, 0.716, 0.750],
         [8, 0.714, 0.747],[9, 0.717, 0.745],[10, 0.718, 0.751],[11, 0.716, 0.752],
         [12, 0.717, 0.748],[13, 0.718, 0.746],[14, 0.716, 0.749],[15, 0.718, 0.748]]

plt.plot([i[0] for i in gpu_1], [i[1] for i in gpu_4], lw=0.5, color='b', label='Train accuracy')
plt.plot([i[0] for i in gpu_1], [i[2] for i in gpu_4], lw=0.5, color='r', label='Test accuracy')
plt.title('Accuracy in each epochs (GPU 4)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid()
plt.legend()
plt.show()


gpu_8 = [[0, 0.108, 0.109],[1, 0.108, 0.107],[2, 0.106, 0.106],[3, 0.106, 0.106],
         [4, 0.107, 0.104],[5, 0.106, 0.104],[6, 0.106, 0.107],[7, 0.106, 0.105],
         [8, 0.107, 0.102],[9, 0.106, 0.105],[10, 0.106, 0.103],[11, 0.106, 0.109],
         [12, 0.106, 0.106],[13, 0.106, 0.100],[14, 0.106, 0.107],[15, 0.106, 0.105]]

plt.plot([i[0] for i in gpu_1], [i[1] for i in gpu_8], lw=0.5, color='b', label='Train accuracy')
plt.plot([i[0] for i in gpu_1], [i[2] for i in gpu_8], lw=0.5, color='r', label='Test accuracy')
plt.title('Accuracy in each epochs (GPU 8)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid()
plt.legend()
plt.show()
