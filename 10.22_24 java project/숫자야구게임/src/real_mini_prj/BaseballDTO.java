package real_mini_prj;

import java.util.Date;

public class BaseballDTO {
	private String name;
	private int ct;
	private Date regdate;
	private int time;
	
	public BaseballDTO(String name, int ct, int time) {
		super();
		this.name = name;
		this.ct = ct;
		this.time = time;
	}
	public BaseballDTO() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getCt() {
		return ct;
	}
	public void setCt(int ct) {
		this.ct = ct;
	}
	
	public Date getRegDate() {
		return regdate;
	}
	public void setRegDate(Date regdate) {
		this.regdate = regdate;
	}
	public int getTime() {
		return time;
	}

	public void setTime(int time) {
		this.time = time;
	}

}
