import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class App {
    private static Random random = new Random();

    public static void main(String[] args) {
        System.out.println("Tri par tas java");

        Headsort tri = new Headsort(generateRandomIntList(10));
        long startTime = System.nanoTime();
        List<Integer> listeTriee = tri.trierParTas();
        long endTime = System.nanoTime();
        double seconds = (endTime - startTime) / 1000000000.0;
        System.out.println(listeTriee + " \nTemps d'exécution : " + seconds);
    }

    public static List<Integer> generateRandomIntList(Integer size) {
        List<Integer> randomNumbers = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            randomNumbers.add(random.nextInt(100));
        }
        return randomNumbers;
    }
}
