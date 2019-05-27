from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2
import pathlib

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True,
                help="storedimages")
ap.add_argument("-q", "--query", required=True,
                help="queryimages")
ap.add_argument("-r", "--result-path", required=True,
                help="resultimages")
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))

query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
results = searcher.search(features)

cv2.imshow("Query", query)

for (score, resultID) in results:
    resultID = pathlib.PureWindowsPath(resultID).as_posix()
    print(args['result_path'] + "/" + resultID)
    result = cv2.imread(resultID)
    cv2.imshow("Result", result)
    cv2.waitKey(0)