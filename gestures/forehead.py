# Choregraphe bezier export in Python.
import naoqi
import nao_nocv_2_1 as nao
import time
from naoqi import ALProxy
from naoqi import ALBroker


def forehead_wipe():
nao.InitProxy("192.168.0.117")
broker = ALBroker("pythonBroker", "127.0.0.1", 9998, "192.168.0.117", 9559)

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
keys.append([[-0.0261199, [3, -0.32, 0], [3, 0.24, 0]], [0.427944, [3, -0.24, 0], [3, 0.533333, 0]], [0.308291, [3, -0.533333, 0.0739191], [3, 0.226667, -0.0314156]], [0.11194, [3, -0.226667, 0.0588857], [3, 0.186667, -0.0484941]], [-0.013848, [3, -0.186667, 0], [3, 0.186667, 0]], [0.061318, [3, -0.186667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
keys.append([[-0.234743, [3, -0.32, 0], [3, 0.24, 0]], [-0.622845, [3, -0.24, 0], [3, 0.533333, 0]], [-0.113558, [3, -0.533333, -0.14425], [3, 0.226667, 0.0613061]], [-0.00617796, [3, -0.226667, 0], [3, 0.186667, 0]], [-0.027654, [3, -0.186667, 0.00511335], [3, 0.186667, -0.00511335]], [-0.036858, [3, -0.186667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
keys.append([[-0.866668, [3, -0.266667, 0], [3, 0.24, 0]], [-0.868202, [3, -0.24, 0], [3, 0.533333, 0]], [-0.822183, [3, -0.533333, 0], [3, 0.226667, 0]], [-0.992455, [3, -0.226667, 0], [3, 0.186667, 0]], [-0.966378, [3, -0.186667, 0], [3, 0.186667, 0]], [-0.990923, [3, -0.186667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
keys.append([[-0.957257, [3, -0.266667, 0], [3, 0.24, 0]], [-0.823801, [3, -0.24, 0], [3, 0.533333, 0]], [-1.00788, [3, -0.533333, 0], [3, 0.226667, 0]], [-0.925044, [3, -0.226667, 0], [3, 0.186667, 0]], [-1.24412, [3, -0.186667, 0], [3, 0.186667, 0]], [-0.960325, [3, -0.186667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1.52, 3.12, 3.8, 4.92])
keys.append([[0.132026, [3, -0.506667, 0], [3, 0.533333, 0]], [0.132026, [3, -0.533333, 0], [3, 0.226667, 0]], [0.132026, [3, -0.226667, 0], [3, 0.373333, 0]], [0.132026, [3, -0.373333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
keys.append([[0.863599, [3, -0.266667, 0], [3, 0.24, 0]], [0.858999, [3, -0.24, 0], [3, 0.533333, 0]], [0.888144, [3, -0.533333, -0.0165061], [3, 0.226667, 0.0070151]], [0.929562, [3, -0.226667, -0.0235543], [3, 0.186667, 0.0193977]], [1.017, [3, -0.186667, 0], [3, 0.186667, 0]], [0.977116, [3, -0.186667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
keys.append([[0.286815, [3, -0.266667, 0], [3, 0.24, 0]], [0.230059, [3, -0.24, 0.00872785], [3, 0.533333, -0.0193952]], [0.202446, [3, -0.533333, 0], [3, 0.226667, 0]], [0.406468, [3, -0.226667, 0], [3, 0.186667, 0]], [0.360449, [3, -0.186667, 0.0145729], [3, 0.186667, -0.0145729]], [0.31903, [3, -0.186667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1.52, 3.12, 3.8, 4.92])
keys.append([[0.386526, [3, -0.506667, 0], [3, 0.533333, 0]], [0.386526, [3, -0.533333, 0], [3, 0.226667, 0]], [0.386526, [3, -0.226667, 0], [3, 0.373333, 0]], [0.386526, [3, -0.373333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
keys.append([[1.28093, [3, -0.213333, 0], [3, 0.24, 0]], [1.39752, [3, -0.24, -0.030151], [3, 0.533333, 0.0670022]], [1.57239, [3, -0.533333, 0], [3, 0.226667, 0]], [1.24105, [3, -0.226667, 0.0186267], [3, 0.186667, -0.0153397]], [1.22571, [3, -0.186667, 0.0153397], [3, 0.186667, -0.0153397]], [0.840674, [3, -0.186667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
keys.append([[-0.128898, [3, -0.213333, 0], [3, 0.24, 0]], [-0.285367, [3, -0.24, 0], [3, 0.533333, 0]], [-0.15651, [3, -0.533333, -0.128857], [3, 0.226667, 0.0547641]], [0.754686, [3, -0.226667, -0.242834], [3, 0.186667, 0.199981]], [1.17193, [3, -0.186667, 0], [3, 0.186667, 0]], [0.677985, [3, -0.186667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1.36, 2.96, 3.64, 4.76])
keys.append([[0.166571, [3, -0.453333, 0], [3, 0.533333, 0]], [0.166208, [3, -0.533333, 0], [3, 0.226667, 0]], [0.166571, [3, -0.226667, 0], [3, 0.373333, 0]], [0.166208, [3, -0.373333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
keys.append([[0.0767419, [3, -0.213333, 0], [3, 0.24, 0]], [-0.59515, [3, -0.24, 0.0975941], [3, 0.533333, -0.216876]], [-0.866668, [3, -0.533333, 0], [3, 0.226667, 0]], [-0.613558, [3, -0.226667, -0.253109], [3, 0.186667, 0.208443]], [0.584497, [3, -0.186667, -0.249275], [3, 0.186667, 0.249275]], [0.882091, [3, -0.186667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
keys.append([[-0.019984, [3, -0.213333, 0], [3, 0.24, 0]], [-0.019984, [3, -0.24, 0], [3, 0.533333, 0]], [-0.615176, [3, -0.533333, 0.19018], [3, 0.226667, -0.0808265]], [-0.833004, [3, -0.226667, 0], [3, 0.186667, 0]], [-0.224006, [3, -0.186667, -0.00920487], [3, 0.186667, 0.00920487]], [-0.214801, [3, -0.186667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1.36, 2.96, 3.64, 4.76])
keys.append([[-0.058334, [3, -0.453333, 0], [3, 0.533333, 0]], [-0.0521979, [3, -0.533333, 0], [3, 0.226667, 0]], [-0.067538, [3, -0.226667, 0], [3, 0.373333, 0]], [-0.038392, [3, -0.373333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "192.168.0.117", 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err

return forehead_wipe_motion