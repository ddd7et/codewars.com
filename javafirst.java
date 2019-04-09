class javafirst
{  
        public static void main(String args[])
        {
           	String name = "P Favuzzi";
    		String[] parts = name.split(" ");
    
    		String part1 = parts[0]; // 004
    		String part2 = parts[1]; // 034556

    		char a = part1.charAt(0);
    		char b = part2.charAt(0);
    		System.out.println(a+"."+b);
    		String answer = a+"."+b;
    		return answer;

    		

        }
}