package real_mini_prj;

import java.awt.Color;
import java.awt.Component;
import java.awt.Frame;
import java.util.Vector;

import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.SwingConstants;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableCellRenderer;
import javax.swing.table.TableColumnModel;

public class AllMemberFrame2 extends JFrame {
	JTable table;
	Vector vData;
	Vector vCol;

	public AllMemberFrame2() {
		setTitle("JTable 회원 예제");
		setSize(600, 400);
		BaseballDAO dao = new BaseballDAO();
		vData = dao.allMembers();
		vCol = new Vector();
		vCol.add("등수");
		vCol.add("이름");
		vCol.add("횟수");
		vCol.add("날짜");
		vCol.add("풀이시간(초)");
		DefaultTableModel model = new DefaultTableModel(vData, vCol);
		table = new JTable(model);
		JScrollPane pane = new JScrollPane(table);
		add(pane);
		setVisible(true);

		// 가운데

		DefaultTableCellRenderer dtcr = new DefaultTableCellRenderer();
		dtcr.setHorizontalAlignment(SwingConstants.CENTER);
		TableColumnModel tcm = table.getColumnModel();
		for (int i = 0; i < tcm.getColumnCount(); i++) {
			tcm.getColumn(i).setCellRenderer(dtcr);
		
		}
		
	
		
		
		
		
		
		//

	}
}