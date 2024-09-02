import pyautogui
import time

sl = 0.5
data = [
    (44,34),  # ecnu icon
    (1000,505),  # 小程序内部随机点
    (782, 836),  # 水电缴费
    (967, 591),  # 温馨提示 确定

    (1162,122),    #查询系统
    (1161,186),    #选择区域
    (1168,254),    #楼栋
    (1165,332),    #楼层
    (1159,402),    #房间
    (972,506),     #下一步

    (1187,666),    #确定
    (970,844),      #target
]


#open ecnu
pyautogui.doubleClick(data[0]);
time.sleep(sl*2);
#user_input = input("输入任意按键，运行脚本：")
pyautogui.moveTo(data[1]);

#find 水电缴费
pyautogui.scroll(-100);
time.sleep(sl);
pyautogui.click(data[2]);
time.sleep(sl);

pyautogui.click(data[3]);
print("进入--水电缴费");


#select 查询系统
time.sleep(sl);
pyautogui.click(data[4]);
pyautogui.click(data[11]); 
pyautogui.click(data[10]);
print("进入--查询系统");

#select 区域
time.sleep(sl);
pyautogui.click(data[5]);
pyautogui.click(data[11]);
pyautogui.mouseDown(button='left');
pyautogui.moveRel(0, -120, duration=0.001);
pyautogui.mouseUp(button='left');
pyautogui.click(data[10]);
print("进入--区域");

#select 楼栋
time.sleep(sl);
pyautogui.click(data[6]);
pyautogui.click(data[11]);
pyautogui.mouseDown(button='left');
pyautogui.moveRel(0, -100, duration=0.001);
pyautogui.mouseUp(button='left');
pyautogui.click(data[10]);
print("进入--楼栋");

#select 楼层
time.sleep(sl);
pyautogui.click(data[7]);
pyautogui.click(data[11]);
pyautogui.mouseDown(button='left');
pyautogui.moveRel(0, -140, duration=0.001);
pyautogui.mouseUp(button='left');
pyautogui.click(data[11]);
pyautogui.mouseDown(button='left');
pyautogui.moveRel(0, -40, duration=0.001);
pyautogui.mouseUp(button='left');
pyautogui.click(data[10]);
print("进入--楼层");

#select 宿舍
time.sleep(sl);
pyautogui.click(data[8]);

for i in range(12):
    pyautogui.click(data[11]);
    pyautogui.mouseDown(button='left');
    pyautogui.moveRel(0, -140, duration=0.001);
    pyautogui.mouseUp(button='left');

pyautogui.click(data[10]);
print("进入--宿舍");

#下一步
pyautogui.click(data[9]);
print("edN");