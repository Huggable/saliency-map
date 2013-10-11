from src.saliency_map import SaliencyMap
from src.utils import OpencvIo
IMAGE_PATH = "C:/Users/admin/Desktop/wall.png"
oi = OpencvIo()
src = oi.imread(IMAGE_PATH)
sm = SaliencyMap(src)
oi.imshow_array([sm.map])