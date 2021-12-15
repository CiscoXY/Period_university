package PB19020632.src;

import java.net.URL;


import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;

import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;

import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;

import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;
import javafx.util.Duration;



public class Main_ui extends Application{

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader fx = new FXMLLoader(); // *定义加载器
        URL resource = getClass().getResource("GUI.fxml"); // *获取资源.getClassLoader()
        fx.setLocation(resource); // *定位资源
        // *fx.setBuilderFactory(new JavaFXBuilderFactory());
        AnchorPane root = (AnchorPane) fx.load();
        
        // *初始化Ant
        Ant ant1 = new Ant();
        // *初始化我要的按钮
        Button start_bt = (Button) root.lookup("#start_bt");
        Button pause_bt = (Button) root.lookup("#pause_bt");
        Button SetTime  = (Button) root.lookup("#SetTime");
        Button AntInitLocSet = (Button) root.lookup("#AntInitLocSet");
        Button Reset = (Button) root.lookup("#Reset");
        Label  CountShow    = (Label) root.lookup("#CountShow");
        Label  SpeedShow = (Label) root.lookup("#SpeedShow");
        TextField SpeedInput = (TextField) root.lookup("#SpeedInput");
        TextField AntXInput = (TextField) root.lookup("#AntXInput");
        TextField AntYInput = (TextField) root.lookup("#AntYInput");
        Slider Slider = (Slider) root.lookup("#Slider");


        // * 添加布局 把表格加载进来
        Grid mainGrid = new Grid();
        for(Rectangle[] i : mainGrid.grid) {
            for(Rectangle j : i) {
                root.getChildren().add(j);
            }
        }

        // * 设置timeline
        Timeline mainThread = new Timeline();
        mainThread.setRate(100);
        mainThread.setCycleCount(Timeline.INDEFINITE); // *循环次数
        mainThread.setAutoReverse(true);// * 每次循环重置

        // *设置要循环执行的事件 也就是要执行的主事件 
        EventHandler<ActionEvent> mainevent = new EventHandler<ActionEvent>(){
            @Override
            public void handle(ActionEvent event){
                int antx = ant1.GetX();
                int anty = ant1.GetY();
                boolean state = mainGrid.getBoolean(antx, anty);// *获得所在格子的布尔值
                mainGrid.SwitchColor(antx, anty,  state);// *转变所在格子的颜色
                ant1.action(state);// *蚂蚁移动
                mainGrid.counter ++;
                String text = Integer.toString(mainGrid.counter);
                CountShow.setText(text);
            }
        };
        // * 设置时间间隔
        Duration duration = new Duration(100);
        KeyFrame MainKy = new KeyFrame(duration,"mainky",mainevent);
        mainThread.getKeyFrames().addAll(MainKy);
        // * 完成主线程时间线的建立

        // * 设置更改时间的线程时间
        EventHandler<ActionEvent> TimeChange = new EventHandler<ActionEvent>(){
            @Override
            public void handle(ActionEvent event){

                //  *Integer.valueOf(SpeedInput.getText()))
                //  * 重设时间倍率
                double value = Double.valueOf(SpeedInput.getText());
                mainThread.setRate(value);
                SpeedShow.setText(SpeedInput.getText());
                Slider.setValue(value);
            }
        };
        // * Slider的事件
        Slider.valueProperty().addListener(new ChangeListener<Number>() {
            public void changed(ObservableValue<? extends Number> ov,
                Number old_val, Number new_val) {
                    mainThread.setRate(new_val.doubleValue());
                    SpeedShow.setText(String.format("%.0f", new_val));
                    SpeedInput.setText(String.format("%.0f", new_val));
            }
        });


        start_bt.setOnAction(e ->{
            mainThread.play();
            AntInitLocSet.setDisable(true); // *一旦开始演化，那么在未重置时便不可重新设置蚂蚁初始位置
        });
        pause_bt.setOnAction(e ->{
            mainThread.stop();
        });


        SetTime.setOnAction(TimeChange);


        AntInitLocSet.setOnAction(e ->{
            ant1.x = Integer.valueOf(AntXInput.getText())-1;
            ant1.y = Integer.valueOf(AntYInput.getText())-1;
            AntInitLocSet.setDisable(true);
        });

        Reset.setOnAction(e ->{
            mainThread.stop(); // * 先暂停时间线
            mainGrid.resetGrid();
            ant1.resetAnt();
            CountShow.setText(Integer.toString(mainGrid.counter));
            AntXInput.setText("");
            AntYInput.setText("");
            AntInitLocSet.setDisable(false); // *表明可以更改初始位置
        });



        primaryStage.setTitle("Langton's ant @author: 夏远林");
        Scene scene = new Scene(root);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
}
