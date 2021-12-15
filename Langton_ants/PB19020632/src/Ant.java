package PB19020632.src;

import static PB19020632.src.Config.*;

public class Ant {
    String Direction = "West"; // * 初始方向为西
    
    int x = ANTSTARTX; // *设置起始位置
    int y = ANTSTARTY;

    public void action(boolean state){
        // * 传入一个布尔值，如果是true那么说明蚂蚁所在的格子是黑色 如果是false那么说明蚂蚁所在的格子是白色
        // * 如果蚂蚁所在的格子是black，那么TurnRight 所在格子变为white
        // * 如果蚂蚁所在的格子是white, 那么TurnLeft 所在格子变为black
        if(state){
            TurnRight();
            MoveForward();
        }
        else{
            TurnLeft();
            MoveForward();
        }
    }
    
    public void resetAnt(){
        // * 蚂蚁的重置初始化
        Direction = "West";
        x = ANTSTARTX;
        y = ANTSTARTY;
    }
    public void TurnRight(){
        // * 右转的准则
        switch(Direction){
            case "West":
                Direction = "North";
                break;
            case "North":
                Direction = "East";
                break;
            case "East":
                Direction = "South";
                break;
            case "South":
                Direction = "West";
                break;
        }
    }
    public void TurnLeft(){
        // * 左转的准则
        switch(Direction){
            case "West":
                Direction = "South";
                break;
            case "South":
                Direction = "East";
                break;
            case "East":
                Direction = "North";
                break;
            case "North":
                Direction = "West";
                break;
        }
    }
    public void MoveForward(){
        // * 向前移动一步
        if(Direction == "West"){
            x --;
        }
        if(Direction == "East"){
            x ++;
        }
        if(Direction == "North"){
            y --;
        }
        if(Direction == "South"){
            y ++;
        }
        LocationRefresh();
    }
    public void LocationRefresh(){
        // *刷新坐标 进行重置，如超出了格子数，那么就要进行缩减或者增加
        if(x >= GRIDSIZE){
            x -= GRIDSIZE;
        }
        else if (x < 0){
            x += GRIDSIZE; 
        }
        if(y >= GRIDSIZE){
            y -= GRIDSIZE;
        }
        else if(y < 0){
            y += GRIDSIZE;
        }
    }
    public String GetDirection(){
        // *获取方向
        return Direction;
    }
    public int GetX(){
        // *获得x坐标
        return x;
    }
    public int GetY(){
        // *获得y坐标
        return y;
    }
}
