import java.util.ArrayList;
import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Tri par tas java");

        ArrayList<Integer> liste = new ArrayList<Integer>();

        liste.add(1);
        liste.add(4);
        liste.add(3);
        liste.add(6);

        Headsort Tri = new Headsort(liste);
        System.out.println(Arrays.asList(Tri.Trier_par_tas()));
    }
}
