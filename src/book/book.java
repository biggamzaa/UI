package book;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class book {
	class Member {
	    private String name;
	    private String age;
	    private String gender;

	    public Member(String name, String age, String gender) {
	        this.name = name;
	        this.age = age;
	        this.gender = gender;
	    }

	    @Override
	    public String toString() {
	        return "Member{" +
	                "name='" + name + "'" +
	                ", age='" + age + "'" +
	                ", gender='" + gender + "'" +
	                '}';
	    }
	}
	
	public class storeMember{
		private List<Member> members = new ArrayList<>();
		{
		        // 초기화 블록을 사용한 멤버 초기화
		        members.add(new Member("이영희", "22", "Female"));
		        members.add(new Member("박지수", "24", "Male"));
		 }
		public void displayMenu() {
	    	System.out.println("원하는 작업을 입력해주세요.");
	    	System.out.println("1. 조회");
	    	System.out.println("2. 추가");
	    	System.out.println("3. 수정");
	    	System.out.println("4. 삭제");
	    }
		
		public void listMembers() {
	        if (members.isEmpty()) {
	            System.out.println("등록된 멤버가 없습니다.");
	        } else {
	            System.out.println("등록된 멤버 목록:");
	            for (Member member : members) {
	                System.out.println(member);
	            }
	        }
	    }
	}
	
	
	
	public static void main(String[] args) {
		book bookInstance = new book();
		storeMember member = bookInstance.new storeMember();
		
		Scanner scanner = new Scanner(System.in);
		
		while (true) {
			member.displayMenu();
            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    member.listMembers();
                    break;
                case 2:
                    // 추가 기능
                    break;
                case 3:
                    // 수정 기능
                    break;
                case 4:
                    // 삭제 기능
                    break;
                default:
                    System.out.println("잘못된 선택입니다. 다시 입력해주세요.");
                    break;
            }
		}
	}

}
