import nao_nocv_2_1 as nao
from naoqi import ALProxy

def InitRobot():
    nao.InitProxy("192.168.0.117")

# local = 127.0.0.1
# marvin = 192.168.0.115
# bender = 192.168.0.117

robotIP= "192.168.0.117" 

def basicWave():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[-0.410393, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.410393, [3, -0.3, 0], [3, 0.166667, 0]], [-0.410393, [3, -0.166667, 0], [3, 0.166667, 0]], [-0.410393, [3, -0.166667, 0], [3, 0.166667, 0]], [-0.410393, [3, -0.166667, 0], [3, 0.333333, 0]], [-0.410393, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[-1.1937, [3, -0.0333333, 0], [3, 0.3, 0]], [-1.1937, [3, -0.3, 0], [3, 0.166667, 0]], [-1.1937, [3, -0.166667, 0], [3, 0.166667, 0]], [-1.1937, [3, -0.166667, 0], [3, 0.166667, 0]], [-1.1937, [3, -0.166667, 0], [3, 0.333333, 0]], [-1.1937, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.3, [3, -0.0333333, 0], [3, 0.3, 0]], [0.3, [3, -0.3, 0], [3, 0.166667, 0]], [0.3, [3, -0.166667, 0], [3, 0.166667, 0]], [0.3, [3, -0.166667, 0], [3, 0.166667, 0]], [0.3, [3, -0.166667, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[1.4632, [3, -0.0333333, 0], [3, 0.3, 0]], [1.4438, [3, -0.3, 0], [3, 0.166667, 0]], [1.4438, [3, -0.166667, 0], [3, 0.166667, 0]], [1.4438, [3, -0.166667, 0], [3, 0.166667, 0]], [1.4438, [3, -0.166667, 0], [3, 0.333333, 0]], [1.4632, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.190307, [3, -0.0333333, 0], [3, 0.3, 0]], [0.222947, [3, -0.3, 0], [3, 0.166667, 0]], [0.222947, [3, -0.166667, 0], [3, 0.166667, 0]], [0.222947, [3, -0.166667, 0], [3, 0.166667, 0]], [0.222947, [3, -0.166667, 0], [3, 0.333333, 0]], [0.190307, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.1, [3, -0.0333333, 0], [3, 0.3, 0]], [0.1, [3, -0.3, 0], [3, 0.166667, 0]], [0.1, [3, -0.166667, 0], [3, 0.166667, 0]], [0.1, [3, -0.166667, 0], [3, 0.166667, 0]], [0.1, [3, -0.166667, 0], [3, 0.333333, 0]], [0.1, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.41184, [3, -0.0333333, 0], [3, 0.3, 0]], [1.53485, [3, -0.3, 0], [3, 0.166667, 0]], [0.915509, [3, -0.166667, 0], [3, 0.166667, 0]], [1.53485, [3, -0.166667, 0], [3, 0.166667, 0]], [0.915509, [3, -0.166667, 0.124779], [3, 0.333333, -0.249558]], [0.41184, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[1.19371, [3, -0.0333333, 0], [3, 0.3, 0]], [1.25409, [3, -0.3, 0], [3, 0.166667, 0]], [1.25409, [3, -0.166667, 0], [3, 0.166667, 0]], [1.25409, [3, -0.166667, 0], [3, 0.166667, 0]], [1.25409, [3, -0.166667, 0], [3, 0.333333, 0]], [1.19371, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.303902, [3, -0.0333333, 0], [3, 0.3, 0]], [0.77, [3, -0.3, 0], [3, 0.166667, 0]], [0.77, [3, -0.166667, 0], [3, 0.166667, 0]], [0.77, [3, -0.166667, 0], [3, 0.166667, 0]], [0.77, [3, -0.166667, 0], [3, 0.333333, 0]], [0.303902, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[1.46242, [3, -0.0333333, 0], [3, 0.3, 0]], [-0.290414, [3, -0.3, 0], [3, 0.166667, 0]], [-0.290414, [3, -0.166667, 0], [3, 0.166667, 0]], [-0.290414, [3, -0.166667, 0], [3, 0.166667, 0]], [-0.290414, [3, -0.166667, 0], [3, 0.333333, 0]], [1.46242, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[-0.18397, [3, -0.0333333, 0], [3, 0.3, 0]], [-1.32306, [3, -0.3, 0], [3, 0.166667, 0]], [-1.32306, [3, -0.166667, 0], [3, 0.166667, 0]], [-1.32306, [3, -0.166667, 0], [3, 0.166667, 0]], [-1.32306, [3, -0.166667, 0], [3, 0.333333, 0]], [-0.18397, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.1, 1, 1.5, 2, 2.5, 3.5])
    keys.append([[0.105129, [3, -0.0333333, 0], [3, 0.3, 0]], [0.220835, [3, -0.3, 0], [3, 0.166667, 0]], [0.220835, [3, -0.166667, 0], [3, 0.166667, 0]], [0.220835, [3, -0.166667, 0], [3, 0.166667, 0]], [0.220835, [3, -0.166667, 0], [3, 0.333333, 0]], [0.105129, [3, -0.333333, 0], [3, 0, 0]]])

    motion = ALProxy("ALMotion", "192.168.0.117", 9559)
    motion.angleInterpolationBezier(names, times, keys)
#    except BaseException, err:
#      print err

def followMe(): 
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[-0.410411, [3, -0.0333333, 0], [3, 0.466667, 0]], [-0.410411, [3, -0.466667, 0], [3, 0.333333, 0]], [-0.410411, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.410411, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.410411, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[-1.19371, [3, -0.0333333, 0], [3, 0.466667, 0]], [-1.19371, [3, -0.466667, 0], [3, 0.333333, 0]], [-1.19371, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.19371, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.19371, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[0.3, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.3, [3, -0.466667, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0.333333, 0]], [0.3, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[1.45288, [3, -0.0333333, 0], [3, 0.466667, 0]], [1.4169, [3, -0.466667, 0], [3, 0.333333, 0]], [1.4169, [3, -0.333333, 0], [3, 0.333333, 0]], [1.4169, [3, -0.333333, 0], [3, 0.333333, 0]], [1.45288, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[0.223428, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.267932, [3, -0.466667, 0], [3, 0.333333, 0]], [0.267932, [3, -0.333333, 0], [3, 0.333333, 0]], [0.267932, [3, -0.333333, 0], [3, 0.333333, 0]], [0.223428, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[0.1, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.1, [3, -0.466667, 0], [3, 0.333333, 0]], [0.1, [3, -0.333333, 0], [3, 0.333333, 0]], [0.1, [3, -0.333333, 0], [3, 0.333333, 0]], [0.1, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[0.411828, [3, -0.0333333, 0], [3, 0.466667, 0]], [1.24613, [3, -0.466667, 0], [3, 0.333333, 0]], [1.24613, [3, -0.333333, 0], [3, 0.333333, 0]], [1.24613, [3, -0.333333, 0], [3, 0.333333, 0]], [0.411828, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.1, 1.5, 2, 2.5, 3, 3.5, 4.5])
    keys.append([[1.19807, [3, -0.0333333, 0], [3, 0.466667, 0]], [1.16585, [3, -0.466667, 0.0322223], [3, 0.166667, -0.0115079]], [0.834267, [3, -0.166667, 0], [3, 0.166667, 0]], [1.16585, [3, -0.166667, 0], [3, 0.166667, 0]], [0.834267, [3, -0.166667, 0], [3, 0.166667, 0]], [1.16585, [3, -0.166667, -0.0161111], [3, 0.333333, 0.0322223]], [1.19807, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.1, 1.5, 2, 2.5, 3, 3.5, 4.5])
    keys.append([[0.299676, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.76, [3, -0.466667, 0], [3, 0.166667, 0]], [0.25, [3, -0.166667, 0], [3, 0.166667, 0]], [0.76, [3, -0.166667, 0], [3, 0.166667, 0]], [0.26, [3, -0.166667, 0], [3, 0.166667, 0]], [0.74, [3, -0.166667, 0], [3, 0.333333, 0]], [0.299676, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[1.44186, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.59071, [3, -0.466667, 0], [3, 0.333333, 0]], [0.59071, [3, -0.333333, 0], [3, 0.333333, 0]], [0.59071, [3, -0.333333, 0], [3, 0.333333, 0]], [1.44186, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.1, 1, 1.5, 2, 2.5, 3, 3.5, 4.5])
    keys.append([[-0.225638, [3, -0.0333333, 0], [3, 0.3, 0]], [0.144862, [3, -0.3, 0], [3, 0.166667, 0]], [0.144862, [3, -0.166667, 0], [3, 0.166667, 0]], [0.1309, [3, -0.166667, 0], [3, 0.166667, 0]], [0.144862, [3, -0.166667, 0], [3, 0.166667, 0]], [0.1309, [3, -0.166667, 0], [3, 0.166667, 0]], [0.144862, [3, -0.166667, 0], [3, 0.333333, 0]], [-0.225638, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.1, 1.5, 2.5, 3.5, 4.5])
    keys.append([[0.103087, [3, -0.0333333, 0], [3, 0.466667, 0]], [0.572958, [3, -0.466667, 0], [3, 0.333333, 0]], [0.572958, [3, -0.333333, 0], [3, 0.333333, 0]], [0.572958, [3, -0.333333, 0], [3, 0.333333, 0]], [0.103087, [3, -0.333333, 0], [3, 0, 0]]])

    motion = ALProxy("ALMotion", "192.168.0.117", 9559)
    motion.angleInterpolationBezier(names, times, keys)
#except BaseException, err:
#    print err

if __name__=="__main__":
    InitRobot()
    basicWave()
    followMe()
