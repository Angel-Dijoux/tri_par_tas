import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

class Headsort {
    private ArrayList<Integer> liste = new ArrayList<Integer>();

    // Constructor

    public Headsort(ArrayList<Integer> liste) {
        this.liste = liste;
    }

    // Methods

    public int gauche(int i) {
        return i * 2 + 1;
    }

    public int droite(int i) {
        return i * 2 + 2;
    }

    public int pere(int i) {
        return (i - 1) / 2;
    }

    public boolean est_tas() {
        for (int i = 1; i < this.liste.size();) {
            if (this.liste.get(this.pere(i)) < this.liste.get(i)) {
                return false;
            } else {
                return true;
            }
        }
        return false;
    }

    public Integer maximun(int i, int lim) {
        int maxi = i;
        int g = this.gauche(i);
        int d = this.droite(i);
        if (g < lim && this.liste.get(g) > this.liste.get(maxi)) {
            maxi = g;
        }
        if (d < lim && this.liste.get(d) > this.liste.get(maxi)) {
            maxi = d;
        }
        return maxi;
    }

    public void entasser(int i, int lim) {
        System.out.println(i + " In enttasser");
        int maxi = this.maximun(i, lim);
        if (maxi != i) {
            this.liste.set(this.liste.lastIndexOf(i), maxi);
            this.liste.set(this.liste.lastIndexOf(maxi), i);
            this.entasser(maxi, lim);
        }
    }

    public void ContruireTas() {
        ArrayList<Integer> newListe = new ArrayList<>(this.liste);
        Collections.reverse(newListe);
        for (int i = newListe.size() - 1; i >= 0; i--) {
            this.entasser(i, newListe.size());
        }
    }

    public ArrayList<Integer> Trier_par_tas() {
        this.ContruireTas();
        System.out.println("Finish");
        for (int i = liste.size() - 1; i > 0; i--) {
            this.liste.set(this.liste.indexOf(0), this.liste.get(i));
            this.liste.set(this.liste.indexOf(i), this.liste.indexOf(0));
            this.entasser(0, i);
        }
        return this.liste;
    }
}
