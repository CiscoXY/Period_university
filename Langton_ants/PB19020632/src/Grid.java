package PB19020632.src;

import static PB19020632.src.Config.*;

import javafx.scene.shape.Rectangle;

public class Grid {
	int counter = 0; // *计数器
	Rectangle[][] grid;
	public Grid() {
		// * DRAW GRID
    	this.grid = new Rectangle[GRIDSIZE][GRIDSIZE];// *建立一个rectangle的数组

		int x = 0, y = 0;

		for (int i=0; i<grid[0].length; i++) {
			for (int j=0; j<grid.length; j++) {
				grid[i][j] = new Rectangle();

				grid[i][j].setFill(WHITE);
				grid[i][j].setStroke(OFFBLACK);
				grid[i][j].setStrokeWidth(.5);

				grid[i][j].setX(x);
				grid[i][j].setY(y);
				grid[i][j].setWidth(RECTSIZE);
				grid[i][j].setHeight(RECTSIZE);

				x+=RECTSIZE;
			}
			y+=RECTSIZE;
			x=0;
		}
	}

	// * Set all squares back to white
	public void resetGrid() {
		for(Rectangle[] i : this.grid) {
			for (Rectangle j : i) {
				j.setFill(WHITE);
				j.setStrokeWidth(.5);
			}
		}
		counter = 0;
	}
	// *转变[x][y]位置的格子颜色
	public void SwitchColor(int x, int y, boolean state){
		if(state){
			grid[x][y].setFill(WHITE);
		}
		else{
			grid[x][y].setFill(BLACK);
		}
	}
	// *如果[x][y]位置的格子是黑色的，那么返回一个true 否则返回false
	public boolean getBoolean(int x,int y){
		if(grid[x][y].getFill()==WHITE){
			return false;
		}
		else{
			return true;
		}
	}

}
