package real_mini_prj;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Vector;

public class BaseballDAO {
	public static final String USER = "SCOTT";
	public static final String PASSWORD = "TIGER";
	public static final String URL = "jdbc:oracle:thin:@localhost:1521:XE";
	public static final String DRIVER = "oracle.jdbc.driver.OracleDriver";

	public Vector allMembers() {
	
		Vector v = new Vector();
		Connection conn = null;
		try {
			Class.forName(DRIVER);
			conn = DriverManager.getConnection(URL, USER, PASSWORD);
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}catch (ClassNotFoundException e2) {
			// TODO Auto-generated catch block
			e2.printStackTrace();
		}
		PreparedStatement psmt = null;
		ResultSet rs = null;
		String sql = "select * from US WHERE rownum <= 5 ORDER BY cnt asc, time desc";
		try {
			psmt = conn.prepareStatement(sql);
			rs = psmt.executeQuery();
			int rank = 0;
			// 이름, 횟수
			while (rs.next()) {
				rank ++;
				Vector vRow = new Vector();
				vRow.add(rank);
				vRow.add(rs.getString("name"));
				vRow.add(rs.getInt("cnt"));
				vRow.add(rs.getString("regdate"));
				vRow.add(rs.getInt("time"));
				v.add(vRow);
				
			}
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return v;
	}	
	
	// 회원 저장
	public void insertUS(BaseballDTO bbd) {
		String sql = "INSERT INTO US(name,cnt, regdate, time) " + "VALUES(?,?, SYSDATE, ?)";

		Connection conn = null;
		PreparedStatement psmt = null;
		try {
			Class.forName(DRIVER);
			conn = DriverManager.getConnection(URL, USER, PASSWORD);
			psmt = conn.prepareStatement(sql);
			psmt.setString(1, bbd.getName());
			psmt.setInt(2, bbd.getCt());
			psmt.setInt(3, bbd.getTime());
			
			psmt.executeUpdate();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		} finally {
			// 6. 자원 해제
			if (psmt != null) {
				try {
					psmt.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			} // if psmt

			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			} // if conn
		}

	} // insert member
}
