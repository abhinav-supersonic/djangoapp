import java.util.*;
import java.util.stream.*;

class Test {

  public static void remove(ArrayList<String> list, int len) {


      List<String> list2 = list.stream()
                          .filter(s -> s.length() > len)
                          .collect(Collectors.toList());
     System.out.println(list2);
    }
 

  public static void main(String args[]) {
     ArrayList<String> list = new ArrayList<String>();
     list.add("tomato");
     list.add("cheese");
     list.add("chips");
     list.add("fruit");
     list.add("butter");
     list.add("tea");
     list.add("buns");
     list.add("pie");
    
     System.out.println(list);
     remove(list, 4);
     

  }
}