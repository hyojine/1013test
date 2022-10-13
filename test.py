import torch
import cv2
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
img = cv2.imread('aa.jpeg')
print(img.shape)

results = model(img)
results.save()

result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='person']
print(result)
print(len(result))

tmp_img = cv2.imread('aa.jpeg')

# cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), 
#                        (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), 
#                        (255,255,255))
# cv2.imwrite('result1.png', tmp_img)

# cropped0 = tmp_img[int(result[0][1]):int(result[0][3]), # ymin:ymax
# 				  int(result[0][0]):int(result[0][2]) # xmin:xmax
#                   ]
# cv2.imwrite('people1.png', cropped0)

# cropped1 = tmp_img[int(result[1][1]):int(result[1][3]), # ymin:ymax
# 				  int(result[1][0]):int(result[1][2]) # xmin:xmax
#                   ]
# cv2.imwrite('people2.png', cropped1)

# cropped2 = tmp_img[int(result[2][1]):int(result[2][3]), # ymin:ymax
# 				  int(result[2][0]):int(result[2][2]) # xmin:xmax
#                   ]
# cv2.imwrite('people3.png', cropped2)

for i in range(len(result)):
    cropped = tmp_img[int(result[i][1]):int(result[i][3]), # ymin:ymax
				  int(result[i][0]):int(result[i][2]) # xmin:xmax
                  ]
    i+=1
    filename = 'people%i.png'%i
    cv2.imwrite(filename, cropped)