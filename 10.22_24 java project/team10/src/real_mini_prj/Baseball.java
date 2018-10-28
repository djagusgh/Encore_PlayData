package real_mini_prj;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Event;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

import javax.crypto.SecretKeyFactorySpi;
import javax.jws.soap.SOAPBinding.Use;
import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;

import java.util.*;

class Baseball extends JFrame implements ActionListener {

	Dimension dim;
	JFrame frame;
	JPanel tot, message, user, panel1, panel2, panel3, panel, panel4, button_panel;
	JButton insert, submission, init, rank;
	JTextField name_text, t1, t2, t3;
	JScrollPane pane;
	JTable table;
	JLabel title, subtitle;

	long tic, toc;
	int time; // 실행시간

	int count = 0; // count : 게임횟수
	int pid = 1;

	String[] columns = { "회차", "숫자", "결과" };
	String[][] data = new String[9][3]; // 일단 크게 해놔

	static int[] computer = new int[3]; // 숫자야구 답(0~9 사이의 값 입력)

	public Baseball() {

		
		tic = System.currentTimeMillis();

		dim = new Dimension(400, 600);
		frame = new JFrame("숫자 야구 게임");
		// frame.setLocation();
		frame.setPreferredSize(dim);

		GridLayout layout = new GridLayout(5, 1);
		frame.setLayout(layout);

		tot = new JPanel();
		tot.setLayout(new BoxLayout(tot, BoxLayout.Y_AXIS));
		message = new JPanel();
		message.setLayout(new BoxLayout(message, BoxLayout.Y_AXIS));
		title = new JLabel("1 ~ 9 사이의 세 숫자를 입력하세요!");
		subtitle = new JLabel("6번까지 성공하지 못하면 정답을 알려줍니다.");
		
		title.setFont(new Font("arian", Font.BOLD, 18));
		subtitle.setFont(new Font("arian", Font.BOLD, 11));
		
		message.add(title);
		message.add(subtitle);
		message.setFont(new Font("굴림", Font.BOLD, 17));
		message.setPreferredSize(new java.awt.Dimension(120, 80));

		name_text = new JTextField();
		// 가운데 정렬, 한글자만 입력할 수 있게 설정
		t1 = new JTextField();
		t1.setDocument((new JTextFieldLimit(1)));
		t1.setHorizontalAlignment(JTextField.CENTER);
		t2 = new JTextField();
		t2.setDocument((new JTextFieldLimit(1)));
		t2.setHorizontalAlignment(JTextField.CENTER);
		t3 = new JTextField();
		t3.setDocument((new JTextFieldLimit(1)));
		t3.setHorizontalAlignment(JTextField.CENTER);

		user = new JPanel();
		user.setLayout(new BoxLayout(user, BoxLayout.X_AXIS));
		user.add(new JLabel("사용자명"));
		user.add(name_text);
		tot.add(user);
		tot.add(message);

		Font font = new Font("arian", Font.BOLD, 30);
		t1.setFont(font);
		t2.setFont(font);
		t3.setFont(font);

		panel1 = new JPanel();
		panel1.setLayout(new BoxLayout(panel1, BoxLayout.Y_AXIS));
		panel1.add(new JLabel("숫자 1 : "));
		panel1.add(t1);

		panel2 = new JPanel();
		panel2.setLayout(new BoxLayout(panel2, BoxLayout.Y_AXIS));
		panel2.add(new JLabel("숫자 2 : "));
		panel2.add(t2);

		panel3 = new JPanel();
		panel3.setLayout(new BoxLayout(panel3, BoxLayout.Y_AXIS));
		panel3.add(new JLabel("숫자 3 : "));
		panel3.add(t3);

		panel = new JPanel();
		panel.setLayout(new BoxLayout(panel, BoxLayout.X_AXIS));
		panel.add(panel1);
		panel.add(panel2);
		panel.add(panel3);

		panel4 = new JPanel();
		panel4.setLayout(new BoxLayout(panel4, BoxLayout.X_AXIS));
		panel4.setBackground(Color.orange);

		button_panel = new JPanel();

		insert = new JButton("입력");

		insert.setSize(70, 70);
		button_panel.add(insert, BorderLayout.CENTER);

		DefaultTableModel model = new DefaultTableModel(data, columns);
		table = new JTable(model);
		pane = new JScrollPane(table);

		// 테이블 가운데 정렬
		DefaultTableCellRenderer dtcr = new DefaultTableCellRenderer();
		dtcr.setHorizontalAlignment(SwingConstants.CENTER);
		TableColumnModel tcm = table.getColumnModel();

		for (int i = 0; i < tcm.getColumnCount(); i++) {
			tcm.getColumn(i).setCellRenderer(dtcr);
		}

		// 맨아래쪽 버튼 3개
		submission = new JButton("제출");

		submission.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {

				BaseballDTO bdto = new BaseballDTO();
				System.out.println("유저 컴포넌트 = " + user.getComponentCount());
				JTextField jtf = (JTextField) user.getComponent(1);
				bdto.setName(jtf.getText());
				System.out.println(bdto.getName() + " " + count);
				bdto.setCt(count);
				bdto.setTime(time);
				BaseballDAO bdao = new BaseballDAO();
				bdao.insertUS(bdto);

			}
		});

		init = new JButton("초기화");
		rank = new JButton("랭킹");

		panel4.add(submission);
		panel4.add(init);
		panel4.add(rank);

		// add actionListener
		insert.addActionListener(this);
		submission.addActionListener(this);
		submission.setEnabled(false); // 제출 전에는 랭크 등록 안되게!
		init.addActionListener(this);
		rank.addActionListener(this);

		// frame에 최종적으로 추가!
		frame.add(tot);
		frame.add(panel);
		frame.add(button_panel);
		frame.add(pane);
		frame.add(panel4);

		frame.pack();
		frame.setVisible(true);

		computer_random();
	}

	void init_table() {
		t1.setText("");
		t2.setText("");
		t3.setText("");
	}

	void computer_random() { // computer에 답 넣는 코드
		Random r = new Random();

		for (int i = 0; i < computer.length; i++) {
			int e = r.nextInt(9) + 1;
			computer[i] = e;
			for (int j = 0; j < i; j++) {
				if (computer[j] == computer[i]) {
					i--;
					break;
				}
			}
		}
		System.out.print("답은 : ");
		for (int i = 0; i < computer.length; i++) {
			System.out.print(computer[i]);
		}
		System.out.println("");
	}

	String count_baseball(int num1, int num2, int num3) {
		System.out.print("답은 : ");
		for (int i = 0; i < computer.length; i++) {
			System.out.print(computer[i]);
		}
		System.out.println("");

		int strike = 0;
		int ball = 0;
		String answer = "";
		int user[] = { num1, num2, num3 }; // 사용자가 입력
		// strike 갯수
		for (int i = 0; i < user.length; i++) {
			if (user[i] == computer[i]) {
				strike++;
			}
		}
		// ball 갯수

		if (computer[0] == user[1] || computer[0] == user[2]) {
			ball++;
		}
		if (computer[1] == user[0] || computer[1] == user[2]) {
			ball++;
		}
		if (computer[2] == user[0] || computer[2] == user[1]) {
			ball++;
		}

		answer = ball + "B " + strike + "S";

		return answer;
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();

		if (obj == insert) {
			String result = "";
			System.out.println("count = " + (count + 1));
			try {
				int num1 = Integer.parseInt(t1.getText());
				int num2 = Integer.parseInt(t2.getText());
				int num3 = Integer.parseInt(t3.getText());

				// count_ball_game 결과 리턴
				if (num1 == 0 || num2 == 0 || num3 == 0) {
					JOptionPane.showMessageDialog(this, "0은 입력하시면 안됩니다.");
				} else {
					count++;
					result = count_baseball(num1, num2, num3);
					// 리턴 값을 테이블에 저장
					String[] row = { String.valueOf(count), t1.getText() + t2.getText() + t3.getText(), result };
					data[count] = row;
					table.setValueAt(String.valueOf(count), count - 1, 0);
					table.setValueAt(t1.getText() + t2.getText() + t3.getText(), count - 1, 1);
					table.setValueAt(result, count - 1, 2);
				}

				if (result.equals("0B 3S")) {
					JOptionPane.showMessageDialog(this, "축하합니다. 정답을 맞추셨습니다!");
					count--;

					toc = System.currentTimeMillis();
					time = (int) (toc - tic) / 1000;
					System.out.println("실행 시간 = " + time);
					submission.setEnabled(true);

				}

			} catch (Exception e1) {
				JOptionPane.showMessageDialog(this, "문자, 빈 칸은 안됩니다. 숫자를 입력하세요!");
			} finally {
				if (count == 7) {
					JOptionPane.showMessageDialog(this,
							"아쉽네요. 정답은 " + computer[0] + computer[1] + computer[2] + "입니다.");
				}
				init_table();
			}

		} else if (obj == submission) { // 제출
			// 생성자에서 구현됨

		} else if (obj == init) { // 초기화
			// table 초기화, Random 숫자도 초기화!
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 3; j++) {
					table.setValueAt("", i, j);
				}
			}
			tic = System.currentTimeMillis();
			init_table();
			count = 0;
			computer_random(); // 답을 다시 만들어야 함!
			submission.setEnabled(false);

		} else if (obj == rank) { // 랭킹 확인
			new AllMemberFrame2();
		}
	}

	public static void main(String[] args) {
		new Baseball();
		/*
		 * SQL 코드  DROP TABLE US;
		 * 
		 * CREATE TABLE US ( name VARCHAR2(100) NOT NULL, cnt NUMBER NOT NULL, regdate
		 * date, time int );
		 * 
		 * INSERT INTO US(name,cnt, regdate, time) " + "VALUES(?,?, SYSDATE, ?)
		 * 
		 * SELECT * from US;
		 * 
		 */

	}

}