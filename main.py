import json
from deepface import DeepFace

# face matching

result= DeepFace.verify(img1_path="images/ed1.jfif", img2_path="images/Ed.jfif")
print(json.dumps(result,indent=2))


# face_analysis 
objs = DeepFace.analyze(
 img_path = "me1.jpeg"
)
print(json.dumps(objs,indent=2)) 

# find face in db
dfs= DeepFace.find(img_path="lana.jfif", db_path="./images")
print(dfs)

