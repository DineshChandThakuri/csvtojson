import com.google.gson.Gson;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;

public class Main {

    public static List<String> parentkeys;
    public static Map jsonData = new HashMap();



    public static void main(String[] args) {
        System.out.println("Hello World!");
        String thisLine = null;

        try {

            File file = new File("raw.csv");
            // open input stream test.txt for reading purpose.
            BufferedReader br = new BufferedReader(new FileReader(file));

            while ((thisLine = br.readLine()) != null) {
                System.out.println(thisLine);
                String[] temp = thisLine.split(",");
                if (jsonData.keySet().contains(temp[1])){
                    System.out.println("newTempArray = " + jsonData.get(temp[1]).getClass());
                    ArrayList<String> newTempArray = (ArrayList<String>) jsonData.get(temp[1]);
                    newTempArray.add(temp[0]);
                    jsonData.put(temp[1], newTempArray);
                }else {
                    jsonData.put(temp[1], new ArrayList<String>(Arrays.asList(temp[0])));
                }

            }
            parentkeys = new ArrayList<>(jsonData.keySet());
            System.out.println("parentkeys = " + parentkeys.toString());


            for (int i = 0; i < parentkeys.size(); i++) {
                System.out.println("parentkeys = " + parentkeys.get(i));
                ArrayList<Object> values = (ArrayList<Object>)jsonData.get(parentkeys.get(i));
                ArrayList<Object> replaceValues = new ArrayList<>();
                System.out.println("values = " + values);
                if (values != null){
                    for (Object val: values) {
                        if (parentkeys.contains(val)){
                            Map childParent = new HashMap();
                            childParent.put(val, jsonData.get(val));
                            jsonData.remove(val);
                            System.out.println("childParent = " + childParent);
                            replaceValues.add(childParent);
                        }else{
                            replaceValues.add(val);
                        }
                    }
                    jsonData.put(parentkeys.get(i), replaceValues);
                }else{
                    parentkeys.remove(parentkeys.get(i));
                }

            }
            System.out.println("parentkeys ============ " + parentkeys);


            Gson gson = new Gson();
            String json = gson.toJson(jsonData);
            System.out.println("JSONjsonData = " + json);

        } catch(Exception e) {
            e.printStackTrace();
        }
    }

}
