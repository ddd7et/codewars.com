// https://www.codewars.com/kata/abbreviate-a-two-word-name/java

// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

//The output should be two capital letters with a dot seperating them.

//It should look like this:

//Sam Harris => S.H

//Patrick Feeney => P.F


public class AbbreviateTwoWords {

  public static String abbrevName(String name) {

    String[] parts = name.split(" ");
    
    String part1 = parts[0];
    String part2 = parts[1]; 

    char a = Character.toUpperCase(part1.charAt(0));
    char b = Character.toUpperCase(part2.charAt(0));
    String answer = a+"."+b;
    return answer;
  }
}